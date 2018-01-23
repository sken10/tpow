"""check_ds18b20_skiprom_.py
"""
import tpow.usb9097
import tpow.device
import tpow.sensor
import cfg

bus = tpow.usb9097.USB9097(cfg.com_port)  # USB9097('COM3')

print("check ds18b20 by skip-rom protocol")
print("Assume only one 1-wire device on the bus.")

# do temperature conversion and get scratch-pad
spad = tpow.device.ds18b20_skip_rom(bus)
print("SPAD : " + " ".join(['%02X' % ord(a) for a in spad]))

# engineering value.
t = tpow.sensor.ds18b20_temp(spad)
print("%8.3f [degC]" % t)

