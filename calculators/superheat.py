#!/usr/bin/env python3
"""Superheat calculator for HVAC field work.

Superheat = Suction Line Temp - Saturated Suction Temp (from PT chart)
"""

import argparse

from pt_data import SAT_TEMP_R410A, finite_float, interpolate_sat_temp

# Legacy approximate tables retained for compatibility, not revalidated here.
# Use a current manufacturer chart for R22/R134A field decisions.
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


def get_sat_temp(refrigerant: str, pressure: float) -> float:
    chart = REFRIGERANTS.get(refrigerant)
    if not chart:
        raise ValueError(f"No PT data for {refrigerant}")
    return interpolate_sat_temp(chart, pressure)


def main():
    parser = argparse.ArgumentParser(description="Calculate HVAC superheat")
    parser.add_argument("--suction-temp", type=finite_float, required=True,
                        help="Suction line temperature (°F)")
    parser.add_argument("--suction-pressure", type=finite_float, required=True,
                        help="Suction pressure (PSIG)")
    parser.add_argument("--refrigerant", type=str, default="R410A",
                        choices=list(REFRIGERANTS.keys()),
                        help="Refrigerant type")
    args = parser.parse_args()

    try:
        sat_temp = get_sat_temp(args.refrigerant, args.suction_pressure)
    except ValueError as error:
        parser.error(str(error))

    superheat = args.suction_temp - sat_temp

    print(f"\n{'='*40}")
    print(f"  SUPERHEAT CALCULATION")
    print(f"{'='*40}")
    print(f"  Refrigerant:      {args.refrigerant}")
    print(f"  Suction pressure: {args.suction_pressure} PSIG")
    print(f"  Sat. suction temp: {sat_temp:.1f}°F (PT lookup/interpolation)")
    print(f"  Suction line temp: {args.suction_temp}°F")
    print(f"{'='*40}")
    print(f"  SUPERHEAT = {superheat:.1f}°F")
    print(f"{'='*40}")

    print("  Compare with the equipment manufacturer's target for")
    print("  the metering device, operating mode, and conditions.")
    print("  This result alone does not diagnose charge or authorize adjustment.")
    if args.refrigerant == "R410A":
        print("  PT source: Honeywell Genetron AZ-20 chart (Feb 2019).")
    else:
        print("  WARNING: Legacy approximate PT data; not revalidated.")
    print("  Interpolated values are estimates. Verify against manufacturer")
    print("  documentation; see references/sources.md for data limitations.")


if __name__ == "__main__":
    main()
