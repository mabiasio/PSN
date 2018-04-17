from qsfp28 import *


module=qsfp28()
	
print module.get_serial_number()
module.high_power_enable()
print module.get_vendor_PN()
print module.get_vendor_revision()
print module.get_vendor_name()
print module.get_voltage()
print module.get_temperature()
print module.get_RX_power()
print module.get_TX_power()
print module.get_CDR_status()
#module.CDR_enable()
print module.get_CDR_status()
print module.get_powerclass()
#print module.get_CTLE()
#module.set_CTLE_fixed(1,1,1,1)
#print module.get_CTLE()
print module.get_RX_out_amplitude()
#module.set_RX_out_amplitude(2,1,2,1)
#print module.get_RX_out_amplitude()

#module.set_CTLE_adaptive_enable()

#module.set_CTLE_adaptive_disable()

#module.high_power_enable()
#
#
#print module.get_RX_power()
#print module.get_TX_power()
#module.set_CTLE_adaptive_disable()
#module.set_CTLE_fixed(1,1,1,1)
#print module.get_CTLE()
#module.CDR_enable()
#module.high_power_enable()
#time.sleep(10)
#print module.get_CDR_status()
#module.set_RX_out_amplitude(2,1,2,1)
#print module.get_RX_out_amplitude()
#module.high_power_disable()

