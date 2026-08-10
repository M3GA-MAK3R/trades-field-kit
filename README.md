# Trades Field Kit

A practical toolkit for HVAC, electrical, and skilled-trades field work. Born from the **Handy Helper Umbrella** concept — a field reference you can glance at when you're stuck troubleshooting, and that (theoretically) could be printed on umbrella panels to keep you dry during pressure-washing maintenance.

## What's Inside

```
trades-field-kit/
├── docs/
│   ├── umbrella-panels.md          # The 8-panel field reference content
│   ├── field-checklists/            # Printable checklists
│   │   ├── pm-checklist.md          # Planned maintenance
│   │   ├── pressure-washing.md      # Pressure washing safety & procedure
│   │   ├── no-cool.md               # No-cooling troubleshooting flow
│   │   ├── no-heat.md               # No-heat troubleshooting flow
│   │   └── electrical-safety.md     # LOTO & electrical safety
│   └── diagrams/                    # Mermaid/SVG diagram sources
│       ├── refrigeration-cycle.md
│       ├── thermostat-wiring.md
│       └── motor-circuit.md
├── calculators/                      # CLI calculators
│   ├── superheat.py
│   ├── subcooling.py
│   ├── ohms-law.py
│   ├── airflow-cfm.py
│   └── voltage-drop.py
├── templates/                        # Field documentation templates
│   ├── service-note.md
│   ├── customer-summary.md
│   └── parts-list.md
├── skill/                            # Perplexity Computer skill
│   └── trades-field-work.skill.md
└── references/
    └── sources.md                    # Public source citations
```

## Quick Start

### Calculators

```bash
# Superheat calculation
python3 calculators/superheat.py --suction-temp 55 --suction-pressure 120 --refrigerant R410A

# Subcooling calculation
python3 calculators/subcooling.py --liquid-temp 95 --head-pressure 340 --refrigerant R410A

# Ohm's Law
python3 calculators/ohms-law.py --volts 240 --amps 15

# Voltage drop
python3 calculators/voltage-drop.py --amps 15 --length 100 --wire-gauge 12
```

### The Handy Helper Umbrella PDF

A printable 8-panel field reference guide covering:
1. Safety First — LOTO, PPE, wet-work precautions
2. Refrigeration Cycle Diagram
3. Superheat & Subcooling Quick Guide
4. Thermostat Low-Voltage Wiring
5. Contactor & Capacitor Motor Circuits
6. Heat Pump Sequence & Defrost
7. Electrical Pocket Formulas
8. Troubleshooting Decision Flow

## Safety Disclaimer

This toolkit provides general reference information for educational purposes. Always:
- Verify against manufacturer specifications and local codes
- Follow OSHA lockout/tagout procedures
- Consult the NEC and local AHJ for code-compliant work
- De-energize and verify before working on electrical equipment

## License

MIT — free to use, modify, and share. See [references/sources.md](references/sources.md) for source attributions.

## Inspired By

- [Anthony's Cool School HVAC Training](https://hvac.anthonyscoolschool.com/) — hands-on HVAC education program
- [HVAC School](https://hvacrschool.com/) — practitioner-focused HVAC/R training resources
- [OSHA](https://www.osha.gov/control-hazardous-energy) — lockout/tagout standards
