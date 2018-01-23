import time

def read_rom(bus):
    """Get ROMID of single 1-winre device on the bus.
    
    Returns
    -------
    romid : list of single bytes, ROMID.
    
    """
    bus.cmd_reset()         # 0xE3, 0xC1
    bus.dat_write([0x33])   # read-rom
    romid = bus.dat_read(8) # little-endian (family + SN[6] + CRC)
    return romid
    
    
def ds18b20_skip_rom(bus):
    """Get temperature of single ds18b20.
    
    Returns
    -------
    spad: list of single bytes, SCRATCHPAD.
    
    """
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0x44])               # skip-rom, convert-T
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0xBE])               # skip-rom, read-scratchpad
    spad = bus.dat_read(9)
    return spad
    
    
def ds18b20_match_rom(bus, id_big):
    """Get temperature of ds18b20 which has ROMID id_big.
    
    Parameters
    ----------
    id_big: string, ROMID in hexadecimal string (big endian),
                    like "A3 00 00 07 4C B9 6D 28".
    
    Returns
    -------
    spad : list of single bytes, SCRATCHPAD.
    
    """
    id = [int(a, 16) for a in reversed(id_big.split())]
    assert(id[0] == 0x28)  # id[] (little endian)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0x44])       # match-rom, id, convert-t
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0xBE])       # match-rom, id, read-scratchpad
    spad = bus.dat_read(9)
    return spad
    
    
def ds2438_skip_rom(bus):
    """Get temperature and volt of single ds2438.
    
    Returns
    -------
    spad : list of single bytes, SCRATCHPAD.
    
    """
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0x44])               # skip-rom, convert-T
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0xB4])               #  skip-rom, convert-V
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0xB8, 0x00])         # skip-rom, recall-memory-page-0
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0xCC, 0xBE, 0x00])         # skip-rom, read-SP-0
    spad = bus.dat_read(9)
    return spad
    
    
def ds2438_match_rom(bus, id_big):
    """Get temperature and volt of ds2438 which has ROMID id_big.
    
    Parameters
    ----------
    id_big: string, ROMID in hexadecimal string (big endian),
                    like "A3 00 00 07 4C B9 6D 28".
    
    Returns
    -------
    spad : list of single bytes, SCRATCHPAD.
    
    """
    id = [int(a, 16) for a in reversed(id_big.split())]
    assert(id[0] == 0x26)  # id[] (little endian)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0x44])       # match-rom, id, convert-t
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0xB4])       # match-rom, id, convert-V
    time.sleep(1.0)
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0xB8, 0x00]) # match-rom, id, recall-memory-page-0
    bus.cmd_reset()                           # 0xE3, 0xC1
    bus.dat_write([0x55] + id + [0xBE, 0x00]) # match-rom, id, read-SP-0
    spad = bus.dat_read(9)
    return spad
    
    
