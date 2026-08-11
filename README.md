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
├── scripts/                          # CLI helper scripts
│   └── file-issue.sh                # Interactive issue filing from terminal
├── skill/                            # Perplexity Computer skill
│   └── trades-field-work.skill.md
└── references/
    └── sources.md                    # Public source citations
```

## Quick Links

- **Mobile Quick Start:** [docs/MOBILE-QUICKSTART.md](docs/MOBILE-QUICKSTART.md) — bookmark on your phone
- **File an Issue:** [New Issue](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new/choose)
- **PDF Field Reference:** [Handy Helper Umbrella PDF](Handy_Helper_Umbrella_Field_Reference.pdf)

## Filing Issues

Three ways to file an issue — pick what works from your phone or desk:

### 1. Interactive CLI Script (best for terminal/Termux)

```bash
# Clone and run the interactive script
./scripts/file-issue.sh
```

Walks you through equipment type, symptom, readings, and power state
with numbered menus. Assembles a structured issue and submits via `gh`.

### 2. Markdown Template (CLI)

```bash
gh issue create --repo M3GA-MAK3R/trades-field-kit \
  --template field-issue-cli.md
```

Opens your editor pre-filled with the field issue template. Edit, save, quit.

Note: YAML interactive forms (dropdowns/checkboxes) do NOT work with the
`gh` CLI — only the markdown template does.

### 3. Browser / GitHub Mobile App

- **Template chooser:** [github.com/M3GA-MAK3R/trades-field-kit/issues/new/choose](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new/choose)
- **Direct to field issue form:** [github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=field-issue.yml](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=field-issue.yml)

The browser and mobile app render the YAML forms as interactive dropdowns,
checkboxes, and required fields — the full experience.

### Or open in browser from CLI

```bash
gh issue create --repo M3GA-MAK3R/trades-field-kit --web
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
