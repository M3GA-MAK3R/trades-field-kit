# 📱 Mobile Quick Start

> Field-ready guide for HVAC & electrical techs. Bookmark this page.

---

## ⚡ In a Hurry?

| What you need | Tap this |
|--------------|----------|
| File a field issue | [New Issue](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=field-issue.yml) |
| Request a feature | [Request](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=feature-request.yml) |
| Browse field reference | [Umbrella Panels](https://github.com/M3GA-MAK3R/trades-field-kit/blob/main/docs/umbrella-panels.md) |
| Calculators | [Calculator Help](https://github.com/M3GA-MAK3R/trades-field-kit/tree/main/calculators) |
| Safety (LOTO) | [OSHA.gov](https://www.osha.gov/control-hazardous-energy) |

---

## 🛠️ Filing an Issue from Your Phone

### Step 1: Open the Repo

Open your browser and go to:

```
github.com/M3GA-MAK3R/trades-field-kit/issues/new
```

Or tap: [File Issue](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new/choose)

### Step 2: Pick a Template

You'll see two cards:

- **Equipment / Field Issue** — stuck on a service call, found wrong info, need help diagnosing
- **Feature / Reference Request** — want a new calculator, checklist, or diagram

Tap **Get started** on the one you need.

### Step 3: Fill the Form

The form has dropdowns and fields — no typing needed for most of it:

1. **Equipment Type** — tap dropdown, pick your system
2. **Brand & Model** — type from the nameplate (or skip)
3. **Refrigerant** — tap dropdown
4. **Symptom** — tap dropdown
5. **Field Readings** — fill in what you've measured (suction, head, superheat, subcooling, amps, voltage)
6. **What's Happening** — type a few sentences
7. **Power State** — confirm de-energized
8. **Safety Checkboxes** — tap to confirm

### Step 4: Submit

Tap **Submit new issue** at the bottom. Done.

---

## 📐 Quick Calculators (Terminal)

If you have Termux or a terminal on your phone:

```bash
# One-time setup
git clone https://github.com/M3GA-MAK3R/trades-field-kit.git
cd trades-field-kit

# Superheat
python3 calculators/superheat.py --suction-temp 55 --suction-pressure 120 --refrigerant R410A

# Subcooling
python3 calculators/subcooling.py --liquid-temp 95 --head-pressure 340 --refrigerant R410A

# Ohm's Law
python3 calculators/ohms-law.py --volts 240 --amps 15

# Voltage Drop
python3 calculators/voltage-drop.py --amps 15 --length 100 --wire-gauge 12

# Airflow CFM
python3 calculators/airflow-cfm.py electric --kw 10 --temp-rise 45
```

---

## 📋 Field Reference Flaps

The 8-panel Handy Helper Umbrella covers:

| # | Flap | When to Check |
|---|------|---------------|
| 1 | Safety First | Before any work — LOTO, PPE, wet-work |
| 2 | Refrigeration Cycle | Understanding system operation |
| 3 | Superheat & Subcooling | Charge diagnostics |
| 4 | Thermostat Wiring | Low-voltage troubleshooting |
| 5 | Contactor & Capacitor | Motor circuit testing |
| 6 | Heat Pump & Defrost | Heating mode issues |
| 7 | Electrical Formulas | Ohm's Law, voltage drop, wire sizing |
| 8 | Troubleshooting Flow | No-cool / no-heat decision trees |

Read all panels: [umbrella-panels.md](https://github.com/M3GA-MAK3R/trades-field-kit/blob/main/docs/umbrella-panels.md)

---

## 📥 Get the PDF

The printable 8-panel field reference:

[Handy Helper Umbrella PDF](https://github.com/M3GA-MAK3R/trades-field-kit/raw/main/Handy_Helper_Umbrella_Field_Reference.pdf)

Print it, fold it, keep it in your truck.

---

## 🤝 Contributing

- **Found a wrong value?** [File an issue](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=field-issue.yml)
- **Want a new calculator?** [Request a feature](https://github.com/M3GA-MAK3R/trades-field-kit/issues/new?template=feature-request.yml)
- **Want to contribute code?** Read [CONTRIBUTING.md](https://github.com/M3GA-MAK3R/trades-field-kit/blob/main/CONTRIBUTING.md)

---

## ⚠️ Safety

Always:
- **De-energize** and verify with a meter before touching equipment
- **Discharge capacitors** with a 20kΩ resistor
- **Check manufacturer specs** — this is a reference, not a manual
- **Follow local code** and OSHA lockout/tagout

[OSHA Lockout/Tagout](https://www.osha.gov/control-hazardous-energy)

---

*MIT License — free to use, modify, and share.*
