#!/usr/bin/env python3
"""Subcooling calculator for HVAC field work.

Subcooling = Saturated Liquid Temp - Liquid Line Temp (from PT chart)
"""

import argparse

from pt_data import SAT_TEMP_R410A, finite_float, interpolate_sat_temp

# Legacy approximate tables retained for compatibility, not revalidated here.
# Use a current manufacturer chart for R22/R134A field decisions.
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


def get_sat_temp(refrigerant: str, pressure: float) -> float:
    chart = REFRIGERANTS.get(refrigerant)
    if not chart:
        raise ValueError(f"No PT data for {refrigerant}")
    return interpolate_sat_temp(chart, pressure)


def main():
    parser = argparse.ArgumentParser(description="Calculate HVAC subcooling")
    parser.add_argument("--liquid-temp", type=finite_float, required=True,
                        help="Liquid line temperature (°F)")
    parser.add_argument("--head-pressure", type=finite_float, required=True,
                        help="Pressure at the liquid-line temperature measurement point (PSIG)")
    parser.add_argument("--refrigerant", type=str, default="R410A",
                        choices=list(REFRIGERANTS.keys()),
                        help="Refrigerant type")
    args = parser.parse_args()

    try:
        sat_temp = get_sat_temp(args.refrigerant, args.head_pressure)
    except ValueError as error:
        parser.error(str(error))

    subcooling = sat_temp - args.liquid_temp

    print(f"\n{'='*40}")
    print(f"  SUBCOOLING CALCULATION")
    print(f"{'='*40}")
    print(f"  Refrigerant:      {args.refrigerant}")
    print(f"  Liquid pressure:  {args.head_pressure} PSIG")
    print(f"  Sat. liquid temp: {sat_temp:.1f}°F (PT lookup/interpolation)")
    print(f"  Liquid line temp: {args.liquid_temp}°F")
    print(f"{'='*40}")
    print(f"  SUBCOOLING = {subcooling:.1f}°F")
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
