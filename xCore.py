from time import sleep_ms
from machine import I2C, Pin

class xCore:
    def __init__(self, freq=100000, scl=22, sda=21):
        self.i2c = I2C(scl=Pin(scl), sda=Pin(sda), freq=100000)

    def write_read(self, addr, reg, length, repeat=False):
        self.i2c.writeto(addr, bytearray([reg]), repeat)
        raw = self.i2c.readfrom(addr, length)
        return raw

    def write_bytes(self, addr, *args, repeat=False):
        self.i2c.writeto(addr, bytes(args))

    def write(self, addr, buf, repeat=True):
        self.i2c.writeto(addr, buf, repeat)

    def read(self, addr, length, repeat=False):
        raw = self.i2c.readfrom(addr, length)
        return raw

    def sleep(time):
        sleep_ms(time)
