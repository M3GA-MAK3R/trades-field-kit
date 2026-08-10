#!/usr/bin/env python3
"""Superheat calculator for HVAC field work.

Superheat = Suction Line Temp - Saturated Suction Temp (from PT chart)
"""

import argparse

# Approximate saturated temperatures (°F) for common refrigerants
# Based on PT charts — always verify with actual PT chart for accuracy
SAT_TEMP_R410A = {
    # pressure (PSIG): temp (°F)
    100: 36, 110: 43, 120: 49, 130: 54, 140: 59, 150: 64,
    160: 68, 170: 73, 180: 77, 190: 81, 200: 85,
}
SAT_TEMP_R22 = {
    60: 34, 65: 37, 70: 41, 75: 44, 80: 47, 85: 50,
    90: 53, 95: 56, 100: 59, 105: 62, 110: 65,
}
SAT_TEMP_R134A = {
    20: 23, 25: 29, 30: 35, 35: 40, 40: 45, 45: 49,
    50: 54, 55: 58, 60: 62, 65: 66, 70: 70,
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
    # Find closest pressure in chart
    closest = min(chart.keys(), key=lambda p: abs(p - pressure))
    return chart[closest]


def main():
    parser = argparse.ArgumentParser(description="Calculate HVAC superheat")
    parser.add_argument("--suction-temp", type=float, required=True,
                        help="Suction line temperature (°F)")
    parser.add_argument("--suction-pressure", type=float, required=True,
                        help="Suction pressure (PSIG)")
    parser.add_argument("--refrigerant", type=str, default="R410A",
                        choices=list(REFRIGERANTS.keys()),
                        help="Refrigerant type")
    args = parser.parse_args()

    sat_temp = get_sat_temp(args.refrigerant, args.suction_pressure)
    if sat_temp is None:
        print(f"Error: No PT data for {args.refrigerant}")
        return

    superheat = args.suction_temp - sat_temp

    print(f"\n{'='*40}")
    print(f"  SUPERHEAT CALCULATION")
    print(f"{'='*40}")
    print(f"  Refrigerant:      {args.refrigerant}")
    print(f"  Suction pressure: {args.suction_pressure} PSIG")
    print(f"  Sat. suction temp: {sat_temp}°F (from PT chart)")
    print(f"  Suction line temp: {args.suction_temp}°F")
    print(f"{'='*40}")
    print(f"  SUPERHEAT = {superheat:.1f}°F")
    print(f"{'='*40}")

    if superheat > 20:
        print("  ⚠  HIGH — Possible undercharge, restriction, or low airflow")
    elif superheat < 5:
        print("  ⚠  LOW — Possible overcharge or overfeeding metering device")
    elif 8 <= superheat <= 14:
        print("  ✓  NORMAL range (8-14°F)")
    else:
        print("  →  Borderline — check manufacturer specs")
    print()

    print("  NOTE: Approximate PT values. Always verify with")
    print("  manufacturer PT chart for accurate diagnostics.")


if __name__ == "__main__":
    main()
