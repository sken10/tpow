"""check_search_roms.py

"""
import tpow.usb9097
import tpow.device
import cfg

def bin2int(buf):
    """
    input  : [0, 1, 0, 1, 1, 0, 1, 0 ...]  # 64 bit binary (MSB fisrt)
    output : [0x5A, ...] # 8 byte data
    """
    def _n(x):
        return int(''.join(['%d' % a for a in x]), 2)
    return [_n(buf[j:j+8]) for j in range(0, len(buf), 8)]
    
    
bus = tpow.usb9097.USB9097(cfg.com_port)  # USB9097('COM3')
xx = tpow.usb9097.search_roms(bus)
for bits_lsb_first in xx: # bits (LSB-first)
    bits_msb_first = [a for a in reversed(bits_lsb_first)]
    rom_big_endian = bin2int(bits_msb_first)
    print(" ".join(["%02X" % a for a in rom_big_endian]))
