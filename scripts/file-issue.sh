#!/usr/bin/env bash
#
# file-issue.sh — Interactive CLI issue creator for trades-field-kit
# Prompts for field-tech info, assembles a structured issue body,
# and creates a GitHub issue via gh CLI.
#
# Usage:
#   ./file-issue.sh                    # interactive prompts
#   ./file-issue.sh --web              # open in browser with template chooser instead
#
set -euo pipefail

REPO="M3GA-MAK3R/trades-field-kit"

# --web flag: skip prompts, open browser to template chooser
if [[ "${1:-}" == "--web" ]]; then
  echo "Opening browser to issue template chooser..."
  gh issue create --repo "$REPO" --web
  exit 0
fi

# Check gh is installed
if ! command -v gh &>/dev/null; then
  echo "Error: GitHub CLI (gh) is not installed."
  echo "Install: https://cli.github.com/"
  exit 1
fi

echo ""
echo "========================================"
echo "  TRADES FIELD KIT — New Issue"
echo "========================================"
echo ""

# Equipment type
echo "Equipment Type:"
echo "  1) Central AC (split system)"
echo "  2) Heat Pump"
echo "  3) Furnace (gas)"
echo "  4) Furnace (electric)"
echo "  5) Mini-Split / Ductless"
echo "  6) Package Unit (Rooftop)"
echo "  7) Refrigeration (commercial)"
echo "  8) Other"
read -p "Select [1-8]: " equip_choice

case "$equip_choice" in
  1) equip="Central AC (split system)" ;;
  2) equip="Heat Pump" ;;
  3) equip="Furnace (gas)" ;;
  4) equip="Furnace (electric)" ;;
  5) equip="Mini-Split / Ductless" ;;
  6) equip="Package Unit (Rooftop)" ;;
  7) equip="Refrigeration (commercial)" ;;
  8) equip="Other" ;;
  *) equip="Other" ;;
esac

# Brand & Model
read -p "Brand & Model (from nameplate, or 'skip'): " brand_model
brand_model="${brand_model:-N/A}"

# Refrigerant
echo ""
echo "Refrigerant:"
echo "  1) R-410A"
echo "  2) R-32"
echo "  3) R-22"
echo "  4) R-134a"
echo "  5) R-454B"
echo "  6) Unknown / N/A"
read -p "Select [1-6]: " refrig_choice
case "$refrig_choice" in
  1) refrig="R-410A" ;;
  2) refrig="R-32" ;;
  3) refrig="R-22" ;;
  4) refrig="R-134a" ;;
  5) refrig="R-454B" ;;
  *) refrig="Unknown" ;;
esac

# Symptom
echo ""
echo "Primary Symptom:"
echo "  1) No cooling"
echo "  2) No heating"
echo "  3) Short cycling"
echo "  4) Tripping breaker"
echo "  5) Freezing up (coil ice)"
echo "  6) Noisy operation"
echo "  7) Leaking water / drain issue"
echo "  8) Not blowing air"
echo "  9) Running but not conditioning"
echo " 10) Error code / fault on board"
echo " 11) Other"
read -p "Select [1-11]: " symptom_choice
case "$symptom_choice" in
  1) symptom="No cooling" ;;
  2) symptom="No heating" ;;
  3) symptom="Short cycling" ;;
  4) symptom="Tripping breaker" ;;
  5) symptom="Freezing up (coil ice)" ;;
  6) symptom="Noisy operation" ;;
  7) symptom="Leaking water / drain issue" ;;
  8) symptom="Not blowing air" ;;
  9) symptom="Running but not conditioning" ;;
  10) symptom="Error code / fault on board" ;;
  *) symptom="Other" ;;
esac

# Title
read -p "Brief title for this issue: " title
title="${title:-$symptom — $equip}"

# Description
echo ""
echo "What's happening? (Describe the situation. Type on the next line,"
echo "press Enter twice when done.)"
description=""
while IFS= read -r line; do
  [[ -z "$line" ]] && break
  description="${description}${description:+$'\n'}${line}"
done
description="${description:-No description provided.}"

# Steps taken
echo ""
echo "Steps already taken? (Press Enter twice when done, or type 'none')"
steps=""
while IFS= read -r line; do
  [[ -z "$line" || "$line" == "none" ]] && break
  steps="${steps}${steps:+$'\n'}- ${line}"
done
steps="${steps:-None}"

# Readings (optional)
echo ""
read -p "Enter any field readings? (y/n): " want_readings
readings_block=""
if [[ "$want_readings" == "y" || "$want_readings" == "Y" ]]; then
  read -p "  Suction pressure (PSIG or 'skip'): " val; val="${val:-—}"
  read -p "  Head pressure (PSIG or 'skip'): " val2; val2="${val2:-—}"
  read -p "  Suction line temp (°F or 'skip'): " val3; val3="${val3:-—}"
  read -p "  Liquid line temp (°F or 'skip'): " val4; val4="${val4:-—}"
  read -p "  Superheat (°F or 'skip'): " val5; val5="${val5:-—}"
  read -p "  Subcooling (°F or 'skip'): " val6; val6="${val6:-—}"
  read -p "  Outdoor ambient (°F or 'skip'): " val7; val7="${val7:-—}"
  read -p "  Delta-T (°F or 'skip'): " val8; val8="${val8:-—}"
  read -p "  Compressor amps (A or 'skip'): " val9; val9="${val9:-—}"
  read -p "  Capacitor MFD comp (or 'skip'): " val10; val10="${val10:-—}"
  read -p "  Capacitor MFD fan (or 'skip'): " val11; val11="${val11:-—}"
  read -p "  Voltage L1-L2 (V or 'skip'): " val12; val12="${val12:-—}"

  readings_block="
## Field Readings

| Measurement | Value |
|------------|-------|
| Suction pressure | ${val} PSIG |
| Head pressure | ${val2} PSIG |
| Suction line temp | ${val3} °F |
| Liquid line temp | ${val4} °F |
| Superheat | ${val5} °F |
| Subcooling | ${val6} °F |
| Outdoor ambient | ${val7} °F |
| Delta-T | ${val8} °F |
| Compressor amps | ${val9} A |
| Cap MFD (comp) | ${val10} |
| Cap MFD (fan) | ${val11} |
| Voltage L1-L2 | ${val12} V |
"
fi

# Power state
echo ""
echo "Power State:"
echo "  1) De-energized and locked out"
echo "  2) De-energized, not locked out"
echo "  3) Still energized"
read -p "Select [1-3]: " power_choice
case "$power_choice" in
  1) power="De-energized and locked out" ;;
  2) power="De-energized, not locked out" ;;
  3) power="STILL ENERGIZED" ;;
  *) power="Not specified" ;;
esac

# Location
read -p "General location (city/state, or 'skip'): " location
location="${location:-Not provided}"

# Assemble body
body="## Equipment
- **Type:** ${equip}
- **Brand & Model:** ${brand_model}
- **Refrigerant:** ${refrig}

## Symptom
${symptom}

## Description
${description}

## Steps Already Taken
${steps}
${readings_block}
## Power State
${power}

## Location
${location}

---
*Filed via trades-field-kit CLI script. Verify all values against manufacturer specs, NEC, and local code.*

**Safety:** Always de-energize and verify with a meter before touching equipment.
"

# Write body to temp file
body_file=$(mktemp)
echo "$body" > "$body_file"

echo ""
echo "========================================"
echo "  Issue Preview"
echo "========================================"
echo "Title: $title"
echo "---"
cat "$body_file"
echo "========================================"
echo ""

read -p "Submit this issue? (y/n): " confirm
if [[ "$confirm" != "y" && "$confirm" != "Y" ]]; then
  echo "Cancelled. Issue body saved to: $body_file"
  exit 0
fi

gh issue create \
  --repo "$REPO" \
  --title "$title" \
  --body-file "$body_file" \
  --label "field-issue,triage"

rm -f "$body_file"
echo ""
echo "Issue created. View at: https://github.com/${REPO}/issues"
