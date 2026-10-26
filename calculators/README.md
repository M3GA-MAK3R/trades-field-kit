# Field Calculators

Small terminal tools for educational field calculations, not automatic diagnoses.
Use Python 3.10 or newer; the calculators and regression tests need no third-party packages.

## Usage

Run from the repository root:

```bash
# Superheat: 52 - 40.6 = 11.4°F
python3 calculators/superheat.py --suction-temp 52 --suction-pressure 120 --refrigerant R410A

# Subcooling: 104.7 - 95 = 9.7°F
python3 calculators/subcooling.py --liquid-temp 95 --head-pressure 340 --refrigerant R410A

# Ohm's Law
python3 calculators/ohms-law.py --volts 240 --amps 15

# Copper voltage drop; length is one-way feet
python3 calculators/voltage-drop.py --amps 15 --length 100 --wire-gauge 12

# Airflow from electric heat
python3 calculators/airflow-cfm.py electric --kw 10 --temp-rise 45
```

Use `python3 calculators/<script>.py --help` for available arguments.
These are CLI tools, not interactive phone-browser calculators.

## Refrigerant Data and Limits

- **R410A:** Both refrigerant calculators use one shared
  [Honeywell Genetron AZ-20 PT table](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-genetron-aZ20-pressure-temp-chart-tech-tool1.pdf)
  in [pt_data.py](pt_data.py), covering 10–615 PSIG at 5-PSIG intervals.
  Values between entries use linear interpolation.
- **Invalid inputs:** Pressures outside the selected table's range and non-finite
  temperatures or pressures produce an error and nonzero exit status.
  Values are not silently snapped to an endpoint or extrapolated.
- **R22:** Shared data from the R22 column of
  [Honeywell's AZ-20 / R-22 chart](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-genetron-aZ20-genetronr22-pressure-temp-chart-tech-tool1.pdf)
  (2011), at 5°F intervals, inverted to pressure keys.
  Supported range: 0.6–381.7 PSIG (-40–150°F); vacuum values are not supported.
- **R134A:** Shared pressure-based data from Appendix E, Genetron 134a, of
  [Honeywell's N13 / 134a retrofit guide](https://prod-edam.honeywell.com/content/dam/honeywell-edam/pmt/oneam/en-us/refrigerants/documents/pmt-am-solstice-n13-commercial-refrigeration-retrofit-tech-guide1.pdf)
  (December 2017). Supported range: 0–280 PSIG (-14.9–154.7°F).
  These are R134a entries, not the guide's N13 blend data.
- **Interpretation:** Compare results with the equipment manufacturer's target
  for the metering device, mode, measurement location, and operating conditions.
  A calculated value alone does not establish normal operation, diagnose charge,
  or authorize adjustment.
- **Other refrigerants:** R32, R454B, and other unlisted refrigerants are not
  supported. Do not substitute R410A data.

The existing `--head-pressure` flag is retained for compatibility. For subcooling,
use pressure at the liquid-line temperature measurement point, not an unrelated
discharge reading. The same paired-location requirement applies to superheat.
See [sources and limitations](../references/sources.md) and
[safety/authorization boundaries](../docs/SAFETY.md).

## Regression Tests

```bash
python3 -m unittest discover -s tests -v
```

Tests cover manufacturer R410A/R22/R134A anchor values, shared-table consistency,
interpolation, range boundaries, invalid inputs, CLI results, and failure exit
codes. They do not certify other calculators or replace equipment-specific
validation. Content checks guard selected safety boundaries and skill-copy parity,
not the complete technical accuracy of the reference library.
GitHub Actions runs the suite on Python 3.10–3.14.
