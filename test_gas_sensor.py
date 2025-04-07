# Unit tests for gas_sensor.py (simulated for local testing)
import unittest
from unittest.mock import patch

import gas_sensor

class TestGasSensor(unittest.TestCase):

    @patch('gas_sensor.gas_sensor_pin')
    def test_read_sensor_voltage_with_mid_value(self, mock_adc):
        # Simulate mid-range ADC value
        mock_adc.read_u16.return_value = 32768  # halfway
        voltage = gas_sensor.read_sensor_voltage()
        expected_voltage = (32768 / 65535) * gas_sensor.VOLTAGE_REF
        self.assertAlmostEqual(voltage, expected_voltage, places=2)

    @patch('gas_sensor.gas_sensor_pin')
    def test_voltage_below_threshold(self, mock_adc):
        mock_adc.read_u16.return_value = 20000
        voltage = gas_sensor.read_sensor_voltage()
        self.assertLess(voltage, gas_sensor.THRESHOLD_VOLTAGE)

    @patch('gas_sensor.gas_sensor_pin')
    def test_voltage_above_threshold(self, mock_adc):
        mock_adc.read_u16.return_value = 60000
        voltage = gas_sensor.read_sensor_voltage()
        self.assertGreater(voltage, gas_sensor.THRESHOLD_VOLTAGE)

if __name__ == '__main__':
    unittest.main()
