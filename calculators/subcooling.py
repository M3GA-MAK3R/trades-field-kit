#!/usr/bin/env python3
"""Subcooling calculator for HVAC field work.

Subcooling = Saturated Liquid Temp - Liquid Line Temp (from PT chart)
"""

import argparse

# Approximate saturated temperatures (°F) for common refrigerants
SAT_TEMP_R410A = {
    250: 71, 300: 87, 350: 100, 400: 113, 450: 125, 500: 136,
    550: 146, 600: 156,
}
SAT_TEMP_R22 = {
    150: 80, 175: 90, 200: 100, 225: 109, 250: 118, 275: 126,
    300: 135, 350: 150,
}
SAT_TEMP_R134A = {
    100: 80, 125: 90, 150: 99, 175: 108, 200: 117, 225: 125,
    250: 133, 275: 141, 300: 148,
}

REFRIGERANTS = {
    "R410A": SAT_TEMP_R410A,
    "R22": SAT_TEMP_R22,
    "R134A": SAT_TEMP_R134A,
}


def get_sat_temp(refrigerant: str, pressure: float) -> float | None:
    chart = REFRIGERANTS.get(refrigerant)
    if not chart:
        return None
    closest = min(chart.keys(), key=lambda p: abs(p - pressure))
    return chart[closest]


def main():
    parser = argparse.ArgumentParser(description="Calculate HVAC subcooling")
    parser.add_argument("--liquid-temp", type=float, required=True,
                        help="Liquid line temperature (°F)")
    parser.add_argument("--head-pressure", type=float, required=True,
                        help="Head/discharge pressure (PSIG)")
    parser.add_argument("--refrigerant", type=str, default="R410A",
                        choices=list(REFRIGERANTS.keys()),
                        help="Refrigerant type")
    args = parser.parse_args()

    sat_temp = get_sat_temp(args.refrigerant, args.head_pressure)
    if sat_temp is None:
        print(f"Error: No PT data for {args.refrigerant}")
        return

    subcooling = sat_temp - args.liquid_temp

    print(f"\n{'='*40}")
    print(f"  SUBCOOLING CALCULATION")
    print(f"{'='*40}")
    print(f"  Refrigerant:      {args.refrigerant}")
    print(f"  Head pressure:    {args.head_pressure} PSIG")
    print(f"  Sat. liquid temp: {sat_temp}°F (from PT chart)")
    print(f"  Liquid line temp: {args.liquid_temp}°F")
    print(f"{'='*40}")
    print(f"  SUBCOOLING = {subcooling:.1f}°F")
    print(f"{'='*40}")

    if subcooling > 20:
        print("  ⚠  HIGH — Possible overcharge or liquid line restriction")
    elif subcooling < 5:
        print("  ⚠  LOW — Possible undercharge or condenser airflow issue")
    elif 8 <= subcooling <= 12:
        print("  ✓  NORMAL range (8-12°F)")
    else:
        print("  →  Borderline — check manufacturer specs")
    print()

    print("  NOTE: Approximate PT values. Always verify with")
    print("  manufacturer PT chart for accurate diagnostics.")


if __name__ == "__main__":
    main()
