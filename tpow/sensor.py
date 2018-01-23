import struct

def ds18b20_temp(spad):
    """Decode temperature from the SCRATCHPAD of DS18B20.
    
    Parameters
    ----------
    spad : list of single bytes, SCRATCHPAD.
    
    Returns
    -------
    t : float, [degC] temperature.
    
    """
    t = struct.unpack('>h', spad[1] + spad[0])[0]/16.0 # [degC]
    return t

def ds2438_temp_volt(spad):
    """Decode temperature and volt from the SCRATCHPAD of DS2438.
    
    Parameters
    ----------
    spad : list of single bytes, SCRATCHPAD.

    Returns
    -------
    t : float, [degC] temperature.
    v : float, [V] volts.
    
    """
    t = struct.unpack('>h', spad[2] + spad[1])[0]/256.0 # [degC]
    v = struct.unpack('>h', spad[4] + spad[3])[0]*0.010 # [V]
    return t, v
    
def hih5030_humidity(t, v):
    """Humidity
    
    Parameters
    ----------
    t : float, [degC] temperature.
    v : float, [V] volts.
    
    
    Returns
    -------
    h : float, [%] humidity (relative).
    
    """
    h1,v1 =   0.0, 0.50*(5/3.3)
    h2,v2 = 100.0, 2.25*(5/3.3)
    h70 = h1 + (v - v1)*(h2 - h1)/(v2 - v1) # [%] at 70degC
    
    h1,v1 =   0.0, 0.6*(5/3.3)
    h2,v2 = 100.0, 2.6*(5/3.3)
    h00 = h1 + (v - v1)*(h2 - h1)/(v2 - v1) # [%] at 0degC
    
    h = h00 + (t - 0.0)*(h70 - h00)/(70.0 - 0.0)
    
    return h
