name: "💡 Feature / Reference Request"
description: "Request a new calculator, checklist, diagram, or reference panel"
title: "[FEATURE] <what you want added>"
labels: ["enhancement", "triage"]
body:
  - type: markdown
    attributes:
      value: |
        ## Feature / Reference Request
        
        Suggest new content for the trades-field-kit: a new calculator, a field
        checklist for a specific procedure, a diagram, or a new umbrella panel.
        
  - type: dropdown
    id: category
    attributes:
      label: What type of request?
      options:
        - New calculator (Python CLI)
        - New field checklist
        - New diagram (Mermaid/SVG)
        - New umbrella panel / flap
        - Improvement to existing content
        - Bug fix (incorrect value or broken tool)
        - Other
    validations:
      required: true

  - type: input
    id: trade
    attributes:
      label: Trade Area
      placeholder: "e.g., HVAC, electrical, plumbing, refrigeration, general"
    validations:
      required: true

  - type: textarea
    id: description
    attributes:
      label: What do you need?
      description: Describe the feature or reference content you'd like added. Be as specific as possible.
      placeholder: |
        I need a calculator for sensible heat ratio (SHR) that takes entering/leaving
        wet bulb temps and CFM, and outputs total/sensible/latent capacity.
    validations:
      required: true

  - type: textarea
    id: use-case
    attributes:
      label: Field Use Case
      description: How would you use this in the field? What problem does it solve?
      placeholder: |
        When balancing a system, I need to verify the SHR matches the equipment
        selection. Currently I have to look it up on a psychrometric chart which
        I don't always carry.
    validations:
      required: false

  - type: checkboxes
    id: contribute
    attributes:
      label: Contribution
      options:
        - label: I'm willing to help build/test this
          required: false
        - label: I can provide reference values or manufacturer specs
          required: false
