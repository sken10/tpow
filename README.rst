**********************************************************
Tiny 1-wire utility. 100% pure python, USB9097 specific.
**********************************************************

    porvides
    
    * Minimal 1-wire protocols for USB9097.
    * Basic rom search algorithm (use recursion).
    
    has dependencies and limitations
    
    * 100% pure python, requires ``pyserial`` to control UART.
    * support external power mode only. parasite power mode is not supported.
    * tested on Windows10 PC + USB9097 (1-wire adapter).
    
Adapters/Sensors/Devices
========================
    
    * USB9097 (1-wire adater with Vcc supply, PCsensor.com ShenZhen/China)
    * DS18B20, DS2438 (Dallas/Maxim)
    * Humidity Sensor HIH-5030 + DS2438Z+ (TaaraLabs Estonia)
    
Usage
======

Check ``examples/`` folder which contains some tests.
``pip tpow`` will install it under ``Lib/site-packages/tpow``.
If you can not find ``examples/``, download source package ``*.tar.gz`` and check it.


Get a ROMID (one 1-wire device on the bus)

::

    import tpow.usb9097
    
    bus = tpow.usb9097.USB9097('COM3')
    bus.cmd_reset()        # 0xE3, 0xC1
    bus.dat_write([0x33])  # read-rom  
    ans = bus.dat_read(8) # little-endian (family + SN[6] + CRC)
    print(['%02X'%ord(a) for a in reversed(ans)]) # big-endian

Get all ROMID's (search all ROM's on the bus)

::

    import tpow.usb9097
    
    bus = tpow.usb9097.USB9097('COM3')
    xx = tpow.usb9097.search_roms(bus)
    for x in xx:
        print(x)
        

Get temperature / ds18b20

::

    import tpow.usb9097
    import tpow.device
    import tpow.sensor
    
    bus = tpow.usb9097.USB9097('COM3')
    
    # do temperature conversion and get scratch-pad
    spad = tpow.device.ds18b20_skip_rom(bus)
    
    # decode temperature
    t = tpow.sensor.ds18b20_temp(spad)
    
    print("SPAD : " + " ".join(['%02X' % ord(a) for a in spad]))
    print("%8.3f [degC]" % t)
    


Todo
====
    * check temperature conversion completed status.
      (currently, wait 1 sec for each temperature conversion)
    * check operation finished status bit.
    * check CRC.
    * refine data type of parameters (bytes, string, list of single bytes...)
    
License
========
    Copyright (c) 2018 Kenich SHIRAKAWA
    This is licensed under MIT license.
    See Licence.txt for more information.


Links
======

    `1-wire adapter USB9097 (PCsensor) <http://pcsensor.com/1-wire-series.html>`_

    `Humidity Senosr (TaaraLabs) <https://taaralabs.eu/1-wire-humidity-temperature-sensor/>`_

