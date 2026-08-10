# Thermostat Low-Voltage Wiring Diagram (Mermaid)

```mermaid
graph LR
    TSTAT[Thermostat] -->|R - Red 24V| BOARD[Control Board / Terminal Block]
    TSTAT -->|Y - Yellow| CONTACTOR[Contactor Coil]
    TSTAT -->|G - Green| BLOWER[Blower Relay]
    TSTAT -->|W - White| HEAT[Heat Strips / Gas Valve]
    TSTAT -->|O - Orange| RV[Reversing Valve Solenoid]
    TSTAT -->|C - Blue| XFORMER[Transformer Common]
    
    BOARD -->|24V| FLOAT[Float Switch]
    FLOAT -->|24V if no water| CONTACTOR
    CONTACTOR -->|240V| COMP[Compressor]
    CONTACTOR -->|240V| CFAN[Condenser Fan]
    
    XFORMER[Transformer 240V→24V] -->|R| TSTAT
    XFORMER -->|C| TSTAT
    
    style TSTAT fill:#20808D,stroke:#28251D,color:#fff
    style CONTACTOR fill:#DA7101,stroke:#28251D,color:#fff
    style XFORMER fill:#01696F,stroke:#28251D,color:#fff
```

## Terminal Reference

| Terminal | Color | Function |
|----------|-------|----------|
| R / RH / RC | Red | 24V power (heat/cool) |
| C | Blue | Common return |
| Y / Y1 | Yellow | Cooling call → contactor |
| G | Green | Fan / blower |
| W / W1 | White | Heating call |
| O | Orange | Reversing valve — energize in COOL (most brands) |
| B | Dark Blue | Reversing valve — energize in HEAT (Ruud/Rheem) |
| W2 | White (2nd) | Auxiliary / 2nd-stage heat |
| Y2 | Yellow (2nd) | 2nd-stage cooling |

## Reversing Valve Brand Reference

| Brand | Energize In | Terminal |
|-------|-----------|----------|
| Carrier, Trane, Goodman, most | Cooling | O |
| Ruud, Rheem | Heating | B |

## Float Switch Wiring

- **Break R method:** Kills thermostat + defrost board (most common)
- **Break Y method:** Kills cooling only (thermostat stays active)
- Always verify which method is used before troubleshooting
