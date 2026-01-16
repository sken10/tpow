"""usb9097.py
"""
import serial

class USB9097:
    """ Minimal DS2480B control and 1-wire data transfer.
    
    DS2480B control
        0xE3 : command-mode
        0xE1 : data-mode
        0xC1 : reset
        0x81/0x91 : sigle-bit-write-0/1
    """
    _MODE_CMD = 0xE3
    _MODE_DAT = 0xE1
    
    def __init__(self, port, timeout=3):
        """
        port : string, name of serial port (ex. 'COM3').
        timeout : float, [sec] timeout.
        """
        self.uart = serial.Serial(port=port, timeout=timeout)
        self.clear()
        self.mode = USB9097._MODE_CMD
        self.cmd_reset()
        
    def clear(self):
        self.uart.send_break()
        self.uart.reset_input_buffer()
        self.uart.reset_output_buffer()
        
    def set_mode(self, mode):
        if mode != self.mode:
            self.uart.write([mode])
            self.mode = mode
        
    def close(self):
        self.uart.close()
        
    def cmd_reset(self):
        self.set_mode(USB9097._MODE_CMD)
        self.uart.write([0xC1]) # reset-pulse
        r = self.uart.read()
        if r != b'\xCD':
            "ERROR"
        
    def cmd_write_bit(self, v):
        self.set_mode(USB9097._MODE_CMD)
        if v != 0:
            self.uart.write([0x91]) # "on" bit
        else:
            self.uart.write([0x81]) # "off" bit
        val = self.uart.read(1)
        return val[0] & 1
        
    def cmd_read_bit(self):
        return self.cmd_write_bit(1)
        
    def dat_write(self, buf):
        def _w(v):
            self.uart.write([v])
            if v == 0xE3:
                self.uart.write([v])
            return self.uart.read(1)
        self.set_mode(USB9097._MODE_DAT)
        return [_w(a) for a in buf]
        
    def dat_read(self, n):
        self.set_mode(USB9097._MODE_DAT)
        self.uart.write([0xFF]*n)
        data = self.uart.read(n)
        return [bytes([a]) for a in data]
        
def search_roms(bus):
    """basic rom search algorithm.
    
    Returns
    -------
    ans : list of romid
          romid : list of int (0 or 1) , LSB first.
    
    ex. [[0, 0, 0, 1, ... ], [0, 0, 0, ...], ....]
    
    """
    ans = []
    
    def _re_select(buf):
        bus.cmd_reset()
        bus.dat_write([0xF0]) # search-rom
        for s in buf:
            d, c = bus.cmd_read_bit(), bus.cmd_read_bit()
            bus.cmd_write_bit(s)
        
    def _search(buf):
        if len(buf) == 64:
            ans.append(buf)
            return
        d, c = bus.cmd_read_bit(), bus.cmd_read_bit()
        if (d, c) == (0, 0): # both 0 and 1.
            # select zero's branch
            bus.cmd_write_bit(0)
            _search(buf + [0])
            # select one's branch
            _re_select(buf)
            d, c = bus.cmd_read_bit(), bus.cmd_read_bit()
            bus.cmd_write_bit(1)
            _search(buf + [1])
        elif (d, c) == (0, 1): # 0 only
            bus.cmd_write_bit(0)
            _search(buf + [0])
        elif (d, c) == (1, 0): # 1 only
            bus.cmd_write_bit(1)
            _search(buf + [1])
        else:
            pass
        
    bus.cmd_reset()
    bus.dat_write([0xF0]) # search-rom
    _search([])
    return ans
    
