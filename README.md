# gas-sensor

# Raspberry Pi Pico Gas Sensor Project

This project uses an MQ-series gas sensor connected to a Raspberry Pi Pico to monitor air quality and detect potentially hazardous gases.

## Features (Planned)
- Read analog values from the gas sensor.
- Convert raw values to voltage.
- Detect abnormal gas levels based on threshold.
- Visual alert using onboard LED.
- [Planned] Display readings on OLED screen or send to web dashboard.

## Remove MOCK MACHINE when deploying to PICO

## Hardware
- Raspberry Pi Pico
- MQ-2 Gas Sensor (analog output connected to GP26 / ADC0)
- Breadboard, jump wires, optional LED

## Status
**In progress** – basic reading logic implemented, calibration and alert system under development.

## Run
```bash
# Copy to Pico using Thonny or rshell
python3 gas_sensor.py
```

## Testing
Unit tests included to simulate sensor input and validate voltage conversion logic.

```bash
python3 test_gas_sensor.py
```