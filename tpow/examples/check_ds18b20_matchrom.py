"""check_ds18b20_matchrom
"""
import tpow.usb9097
import tpow.device
import tpow.sensor
import cfg

bus = tpow.usb9097.USB9097(cfg.com_port)  # USB9097('COM3')

print("check ds18b20 by match-rom protocol")

# get romid
#
id_big = [a for a in reversed(tpow.device.read_rom(bus))]
id_big = " ".join(['%02X' % ord(a) for a in id_big]) #
print("ROMID : " + id_big)

# apply match_rom protocol to identify the device.
# do temperature conversion and get scratch-pad
# 
spad = tpow.device.ds18b20_match_rom(bus, id_big)
print("SPAD : " + " ".join(['%02X' % ord(a) for a in spad]))

# engineering value.
#
t = tpow.sensor.ds18b20_temp(spad)
print("%8.3f [degC]" % t)

