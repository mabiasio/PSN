
from sfp28 import *
import time
from Fluke_8846A import *
import os

module=sfp28()

time.sleep(1)
mm=Fluke_8846A(12)

print mm.get_voltage()

#module configuration
M_VN=module.get_vendor_name()
M_SN=module.get_serial_number()

module.mode_25G()



print 'Module under test id: ' + M_VN + ' ' + M_SN + '\n'
