import time
import telnetlib
import os
import visa
rm = visa.ResourceManager()
rm.list_resources()
multimeter = rm.open_resource('GPIB0::12::INSTR')
print multimeter.query('*IDN?')
