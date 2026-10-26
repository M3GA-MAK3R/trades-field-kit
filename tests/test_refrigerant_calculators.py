"""Manufacturer anchor values plus lookup, CLI, and failure-path regressions."""

import importlib.util
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "calculators"))

from pt_data import SAT_TEMP_R410A, interpolate_sat_temp


def load_calculator(name):
    spec = importlib.util.spec_from_file_location(
        name, ROOT / "calculators" / f"{name}.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


SUPERHEAT = load_calculator("superheat")
SUBCOOLING = load_calculator("subcooling")


class PTLookupTests(unittest.TestCase):
    def test_manufacturer_anchor_values(self):
        # Independently copied from Honeywell AZ-20 v5, February 2019.
        # See references/sources.md for the full manufacturer URL.
        anchors = {
            10: -41.1, 100: 31.4, 120: 40.6, 140: 48.9, 200: 69.6,
            250: 83.7, 300: 95.9, 340: 104.7, 350: 106.8,
            400: 116.6, 430: 122.0, 450: 125.4, 500: 133.6,
            550: 141.2, 600: 148.2, 615: 150.2,
        }
        for module in (SUPERHEAT, SUBCOOLING):
            for pressure, expected in anchors.items():
                with self.subTest(module=module.__name__, pressure=pressure):
                    self.assertEqual(module.get_sat_temp("R410A", pressure), expected)

    def test_single_shared_r410a_table(self):
        self.assertIs(SUPERHEAT.SAT_TEMP_R410A, SUBCOOLING.SAT_TEMP_R410A)

    def test_chart_coverage_and_monotonicity(self):
        self.assertEqual(sorted(SAT_TEMP_R410A), list(range(10, 616, 5)))
        values = [SAT_TEMP_R410A[p] for p in sorted(SAT_TEMP_R410A)]
        self.assertTrue(all(a < b for a, b in zip(values, values[1:])))

    def test_all_exact_entries_preserved(self):
        for pressure, expected in SAT_TEMP_R410A.items():
            self.assertEqual(interpolate_sat_temp(SAT_TEMP_R410A, pressure), expected)

    def test_interpolation_not_nearest_neighbor(self):
        for module in (SUPERHEAT, SUBCOOLING):
            self.assertAlmostEqual(module.get_sat_temp("R410A", 122.5), 41.7)
            self.assertAlmostEqual(module.get_sat_temp("R410A", 121), 41.04)
            self.assertAlmostEqual(module.get_sat_temp("R410A", 342.5), 105.25)

    def test_reject_out_of_range_and_nonfinite_pressures(self):
        for pressure in (0, -10, 9.99, 615.01, 1000,
                         float("nan"), float("inf"), -float("inf")):
            for module in (SUPERHEAT, SUBCOOLING):
                with self.subTest(pressure=pressure, module=module.__name__):
                    with self.assertRaises(ValueError):
                        module.get_sat_temp("R410A", pressure)

    def test_unsupported_refrigerant(self):
        for module in (SUPERHEAT, SUBCOOLING):
            with self.assertRaises(ValueError):
                module.get_sat_temp("R32", 120)

    def test_empty_chart_rejected(self):
        with self.assertRaises(ValueError):
            interpolate_sat_temp({}, 120)

    def test_legacy_tables_also_bounded_and_interpolated(self):
        for module in (SUPERHEAT, SUBCOOLING):
            for refrigerant in ("R22", "R134A"):
                chart = module.REFRIGERANTS[refrigerant]
                low, high = sorted(chart)[:2]
                expected = (chart[low] + chart[high]) / 2
                self.assertAlmostEqual(
                    module.get_sat_temp(refrigerant, (low + high) / 2), expected
                )
                for pressure in (min(chart) - 1, max(chart) + 1):
                    with self.assertRaises(ValueError):
                        module.get_sat_temp(refrigerant, pressure)


class CLITests(unittest.TestCase):
    def run_cli(self, script, *args):
        # Run outside the repository so imports cannot rely on the current folder.
        return subprocess.run(
            [sys.executable, str(ROOT / "calculators" / script), *args],
            cwd=ROOT.parent, capture_output=True, text=True,
        )

    def test_superheat_corrected_example(self):
        result = self.run_cli("superheat.py", "--suction-temp", "52",
                              "--suction-pressure", "120")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SUPERHEAT = 11.4°F", result.stdout)
        self.assertIn("Honeywell", result.stdout)
        self.assertNotIn("NORMAL", result.stdout)
        self.assertNotIn("overcharge", result.stdout)

    def test_subcooling_corrected_example(self):
        result = self.run_cli("subcooling.py", "--liquid-temp", "95",
                              "--head-pressure", "340")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SUBCOOLING = 9.7°F", result.stdout)
        self.assertNotIn("NORMAL", result.stdout)
        self.assertNotIn("undercharge", result.stdout)

    def test_manufacturer_subcooling_example(self):
        result = self.run_cli("subcooling.py", "--liquid-temp", "115",
                              "--head-pressure", "430")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SUBCOOLING = 7.0°F", result.stdout)

    def test_cli_interpolation(self):
        result = self.run_cli("superheat.py", "--suction-temp", "52",
                              "--suction-pressure", "122.5")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("SUPERHEAT = 10.3°F", result.stdout)

    def test_invalid_inputs_fail_without_result_or_traceback(self):
        for script, temperature, pressure, label in (
            ("superheat.py", "--suction-temp", "--suction-pressure", "SUPERHEAT ="),
            ("subcooling.py", "--liquid-temp", "--head-pressure", "SUBCOOLING ="),
        ):
            for flag, value in (
                (pressure, "0"), (pressure, "616"), (pressure, "-1"),
                (pressure, "nan"), (pressure, "inf"), (pressure, "1e309"),
                (temperature, "nan"), (temperature, "inf"),
                (temperature, "-inf"), (temperature, "not-a-number"),
            ):
                args = {temperature: "52", pressure: "120", flag: value}
                flat = [f"{key}={value}" for key, value in args.items()]
                with self.subTest(script=script, flag=flag, value=value):
                    result = self.run_cli(script, *flat)
                    self.assertEqual(result.returncode, 2)
                    self.assertIn("error:", result.stderr)
                    self.assertNotIn("Traceback", result.stderr)
                    self.assertNotIn(label, result.stdout)

    def test_unsupported_refrigerant_cli(self):
        for script, temperature, pressure in (
            ("superheat.py", "--suction-temp", "--suction-pressure"),
            ("subcooling.py", "--liquid-temp", "--head-pressure"),
        ):
            result = self.run_cli(script, temperature, "52", pressure, "120",
                                  "--refrigerant", "R32")
            self.assertEqual(result.returncode, 2)
            self.assertNotIn("Traceback", result.stderr)

    def test_legacy_warning(self):
        result = self.run_cli("superheat.py", "--suction-temp", "52",
                              "--suction-pressure", "70", "--refrigerant", "R22")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Legacy approximate PT data; not revalidated", result.stdout)


if __name__ == "__main__":
    unittest.main()
