# Contributing to Trades Field Kit

Thanks for helping make field work better for trades professionals. This guide covers how to contribute new calculators, checklists, diagrams, and reference content.

## Quick Start

1. Fork the repo
2. Create a branch: `git checkout -b add-shr-calculator`
3. Make your changes
4. Commit: `git commit -m "Add sensible heat ratio calculator"`
5. Push: `git push origin add-shr-calculator`
6. Open a Pull Request

## What We Accept

- New Python calculators (superheat, subcooling, psychrometrics, duct sizing, etc.)
- Field checklists for procedures not yet covered
- Mermaid or SVG diagrams for HVAC/electrical/plumbing
- Corrections to reference values (with source citations)
- Translations of checklists/templates
- New umbrella panel suggestions

## Safety First

All contributions must:
- Include a safety warning where relevant (de-energize, capacitor discharge, etc.)
- Cite sources for technical values (manufacturer manuals, NEC, OSHA, ASHRAE)
- Use "verify against manufacturer specs / local code" language for code-sensitive items
- Never instruct energized-work procedures without proper PPE/permit warnings

## Calculator Guidelines

- Python 3, no external dependencies (stdlib only)
- Include `--help` and argparse with clear descriptions
- Output a formatted result with interpretation (normal/high/low ranges)
- End with a "verify with manufacturer specs" disclaimer
- Test before submitting: `python3 calculator.py --help`

## Checklist Guidelines

- Markdown format
- Checkbox items with `- [ ]` syntax
- Group by step (thermostat → power → outdoor unit → refrigerant → airflow)
- Include a readings table template where relevant

## Diagram Guidelines

- Use Mermaid syntax for flowcharts and process diagrams
- Use ASCII art for simple schematic-style diagrams in umbrella panels
- Label all components and flow direction
- Include a component reference table below diagrams

## Code of Conduct

Be respectful. This is a community for trades professionals helping each other. No gatekeeping — we welcome techs at all experience levels.

## Questions?

Open an issue with the "Feature / Reference Request" template.
