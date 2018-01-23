
This folder contains some test procedures.
Configure name of com port in cfg.py for your environment.

        com_port = 'COM3'

test procedures
===============

check_read_rom.py
    Print one ROMID of 1-wire device.
    Only one device on the bus is assumed.
    
check_ds18b20_skiprom.py
    Print temperature data of DS18B20.
    Only one device on the bus is assumed.
    
check_ds2438_skiprom.py
    Print temperature, volt, humidity of DS2438 + HIH-5030.
    Only one device on the bus is assumed.
    
check_search_roms.py
    Print all ROMID of 1-wire dvices on the bus.
    
check_ds18b20_matchrom.py
    Print temperature data of DS18B20.
    the device is identified by the ROMID.
    
check_ds2438_matchrom.py
    Print temperature, volt, humidity of DS2438 + HIH-5030.
    the device is identified by the ROMID.
    
