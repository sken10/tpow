"""check_ds2438_skiprom.py
"""
import tpow.usb9097
import tpow.device
import tpow.sensor
import cfg

bus = tpow.usb9097.USB9097(cfg.com_port)  # USB9097('COM3')

print("check ds2438 by skip-rom protocol")
print("Assume only one 1-wire device on the bus.")

# do temperature conversion, A/D conversion and get scratch-pad
spad = tpow.device.ds2438_skip_rom(bus)
print("SPAD : " + " ".join(['%02X' % ord(a) for a in spad]))

# engineering value.
t, v = tpow.sensor.ds2438_temp_volt(spad)
hr = tpow.sensor.hih5030_humidity(t, v)
print("%8.3f [degC] %8.3f [V] %8.3f [%%] " % (t, v, hr))
