# reading values from an MQ-series gas sensor and prints the voltage
# need to do actual calibration and add the threshold detection logic

try:
    from machine import ADC, Pin
except ImportError:
    from mock_machine import ADC, Pin # mock for local testing
import time

# initialise ADC for gas sensor input will be conncted to GP26 / ADC0 pins
gas_sensor_pin = ADC(Pin(26))

# maybe led????
led = Pin(25, Pin.OUT)

#  placeholders for now — to be refined after calibration
VOLTAGE_REF = 3.3  # voltage for Pico
THRESHOLD_VOLTAGE = 1.8  # threshold for gas detection

def read_sensor_voltage():
    """
    Reads the analog value from the gas sensor and converts it to voltage.
    Returns:
        float: voltage value corresponding to sensor reading.
    """
    raw_value = gas_sensor_pin.read_u16()
    voltage = (raw_value / 65535) * VOLTAGE_REF
    return voltage

def main():
    print("Starting Gas Sensor Monitor...")
    try:
        while True:
            voltage = read_sensor_voltage()
            print(f"[DEBUG] Sensor Voltage: {voltage:.2f} V")
            
            if voltage > THRESHOLD_VOLTAGE:
                print("⚠️ Warning: Gas levels high!")
                led.value(1)
            else:
                led.value(0)

            time.sleep(1)
    except KeyboardInterrupt:
        print("Program stopped manually.")

if __name__ == "__main__":
    main()
