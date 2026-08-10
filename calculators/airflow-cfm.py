#!/usr/bin/env python3
"""Airflow CFM calculator for HVAC field work.

Method 1: Temperature rise (electric heat)
  CFM = (kW × 3413) ÷ (ΔT × 1.08)

Method 2: Temperature drop (cooling)
  CFM = (BTUH ÷ (ΔT × 1.08))

Method 3: Total static pressure + fan curve (manual lookup)
"""

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Calculate airflow CFM from temperature differential"
    )
    sub = parser.add_subparsers(dest="method")

    # Electric heat method
    elec = sub.add_parser("electric", help="Electric heat CFM from kW and temp rise")
    elec.add_argument("--kw", type=float, required=True, help="Heat strip kW")
    elec.add_argument("--temp-rise", type=float, required=True,
                      help="Temperature rise across heater (°F)")

    # Cooling method
    cool = sub.add_parser("cooling", help="Cooling CFM from BTUH and temp drop")
    cool.add_argument("--btuh", type=float, required=True, help="Cooling capacity (BTUH)")
    cool.add_argument("--temp-drop", type=float, required=True,
                      help="Temperature drop across coil (°F)")

    # Velocity method
    vel = sub.add_parser("velocity", help="CFM from duct velocity and area")
    vel.add_argument("--fpm", type=float, required=True, help="Air velocity (FPM)")
    vel.add_argument("--area", type=float, required=True,
                      help="Duct cross-section area (sq in)")

    args = parser.parse_args()

    if args.method is None:
        parser.print_help()
        sys.exit(1)

    print(f"\n{'='*40}")
    print(f"  AIRFLOW CFM CALCULATION")
    print(f"{'='*40}")

    if args.method == "electric":
        cfm = (args.kw * 3413) / (args.temp_rise * 1.08)
        print(f"  Method: Electric heat")
        print(f"  Heat strips:    {args.kw} kW")
        print(f"  Temp rise:      {args.temp_rise}°F")
        print(f"{'='*40}")
        print(f"  CFM = {cfm:.0f}")

    elif args.method == "cooling":
        cfm = args.btuh / (args.temp_drop * 1.08)
        print(f"  Method: Cooling")
        print(f"  Capacity:       {args.btuh:,.0f} BTUH")
        print(f"  Temp drop:      {args.temp_drop}°F")
        print(f"{'='*40}")
        print(f"  CFM = {cfm:.0f}")

    elif args.method == "velocity":
        cfm = args.fpm * args.area / 144  # convert sq in to sq ft
        print(f"  Method: Velocity")
        print(f"  Velocity:       {args.fpm} FPM")
        print(f"  Duct area:      {args.area} sq in")
        print(f"{'='*40}")
        print(f"  CFM = {cfm:.0f}")

    print(f"{'='*40}")

    # Check typical ranges (400 CFM per ton for cooling)
    if args.method == "cooling" and args.btuh > 0:
        tons = args.btuh / 12000
        expected = tons * 400
        if abs(cfm - expected) / expected > 0.15:
            print(f"  ⚠  Expected ~{expected:.0f} CFM for {tons:.1f} tons (400 CFM/ton)")
        else:
            print(f"  ✓  Within expected range for {tons:.1f} tons")
    print()

    print("  NOTE: 1.08 is the air constant at sea level.")
    print("  Adjust for altitude if working above 2000 ft.")


if __name__ == "__main__":
    main()
