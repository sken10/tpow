"""check_read_rom.py

get ROMID of 1-wire device.
assume only one 1-wire device on the bus.

"""
import tpow.usb9097
import tpow.device
import cfg

bus = tpow.usb9097.USB9097(cfg.com_port)  # USB9097('COM3')
id_little = tpow.device.read_rom(bus)
id_big = [a for a in reversed(id_little)]
print(" ".join(['%02X' % ord(a) for a in id_big]))

