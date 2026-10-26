#!/usr/bin/env python3
"""Superheat calculator for HVAC field work.

Superheat = Suction Line Temp - Saturated Suction Temp (from PT chart)
"""

import argparse

from pt_data import (
    PT_SOURCES, REFRIGERANTS, SAT_TEMP_R410A, finite_float, interpolate_sat_temp,
)


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
                        help="Pressure at the suction-line temperature measurement point (PSIG)")
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
    source_name, source_url = PT_SOURCES[args.refrigerant]
    print(f"  PT source: {source_name}.")
    print(f"  {source_url}")
    print("  Interpolated values are estimates. Verify against manufacturer")
    print("  documentation; see references/sources.md for data limitations.")


if __name__ == "__main__":
    main()
