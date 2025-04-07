class Pin:
    OUT = 1
    IN = 0
    def __init__(self, pin_number, mode=None):
        self.pin_number = pin_number
        self.mode = mode
        self._value = 0

    def value(self, val=None):
        if val is not None:
            self._value = val
        return self._value

class ADC:
    def __init__(self, pin):
        self.pin = pin

    def read_u16(self):
        # sim value for testing
        return 32768
