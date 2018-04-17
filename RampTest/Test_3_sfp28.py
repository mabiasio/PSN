import pymsgbox
from sfp28 import *
from Fluke_8846A import *
from KikusuiPBZ20 import *
from Agilent33600A import *
from DLI100G40G import *
import time
import os

module = sfp28()
psu = KikusuiPBZ20('10.58.241.170')
gen = Agilent33600A('10.58.241.171')
TE = DLI100G40G('10.58.241.161', '8090')
mm = Fluke_8846A(12)

# print PSU and Wafeform Generator IDs

psu.identification()
gen.identification()

gen.output_off(1)
gen.set_wfm(1, 'TRI')
gen.set_frequency(1, '23E-06')  # 23 uHZ
gen.set_amplitude(1, '3.8E-1')  # 380 mVPP

# PSU settings 3,3 VDC + external signal
psu.set_signal_source('BOTH')
psu.set_voltage('3.348')
psu.output_on()
time.sleep(1)

# module configuration
M_SN = module.get_serial_number()
M_VN = module.get_vendor_name()

print 'Module under test id: ' + M_VN + ' ' + M_SN + '\n'

# Pseudo-initialization sequence
time.sleep(0.5)
# module.mode_25G()
time.sleep(0.5)

log = open('Test_3_'+M_VN + '_' + M_SN + time.strftime('%H_%M_%d_%m_%Y.txt'), "w")
head = "LOS_status,Voltage_DDM,Temperature_DDM,RX1,BIAS1,TX1,Multimeter,TIMESTAMP" + '\n'
log.write(head)

pymsgbox.alert('Please check voltage level on Fluke Multimeter and Adjust it accordingly')

# Waveform generator output on
gen.output_on(1)

pymsgbox.alert('Set Properly Test Equipment')

now = time.strftime("%c")
print "Test Started at " + now

TE.start_counters()

for i in range(0, 750):  # minutes of test, test duration in minutes
    print "Minute n: " + str(i) + '\n'
    for k in range(1, 30):
        poll = module.poller()
        volt_mm = mm.get_voltage()
        timestamp = time.strftime('%H_%M_%S')
        log.write(poll + ',' + str(volt_mm) + ',' + timestamp + '\n')
        time.sleep(1.94)

TE.stop_counters()
traffic_res = TE.get_results()
print "Alarms on DLI Test Set"
print TE.get_alarms()
print "Events on DLI Test Set"
TE.get_events()
print "I2C Errors occured"
print module.get_i2c_counter()
TE.logout()
log.close()
# psu.output_off()
gen.output_off(1)
psu.close()
gen.close()

now = time.strftime("%c")
print "Test Finished at " + now