from sfpplus import *
from qsfp28 import *
import os
import sys


module=qsfp28()

SN = module.get_serial_number()
VN = module.get_vendor_name()
log=open(VN + '_' + SN + " module_info " + time.strftime('%H_%M_%d_%m_%Y.txt'),"w")
log.write("Serial Number: " +SN+'\n')
log.write("Vendor Name: " +VN+'\n')
VPN = module.get_vendor_PN()
log.write("Vendor Part Number: " +VPN+'\n')
REV = module.get_vendor_revision()
log.write("Vendor Revision: " +REV+'\n')
FW = module.get_fw_revision()
log.write("Firmware Revision: " +FW+'\n')
pwrclass = module.get_powerclass()
log.write("Power Class: " +str(pwrclass)+'\n')
cleicode = module.get_clei_code()
log.write("CLEI Code: " +cleicode+'\n')
datecode = module.get_date_code()
log.write("Date Code: " +datecode+'\n')
log.close()