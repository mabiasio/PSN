import time
import math
import string
from aardvark_py import *
from array import array

addr = 0x50
handle = aa_open(0)
if (handle <= 0):
    print "Unable to open Aardvark device on port 0"
    print "Error code = %d" % handle
    sys.exit()
# Ensure that the I2C subsystem is enabled
aa_configure(handle, AA_CONFIG_SPI_I2C)
# Pull up resitors already present in the MCB
aa_i2c_pullup(handle, AA_I2C_PULLUP_NONE)
# I2C Master configuration
aa_i2c_slave_disable(handle)
# No Power supply provided by Aardwark module
aa_target_power(handle, AA_TARGET_POWER_NONE)
# I2C Bitrate
aa_i2c_bitrate(handle, 100)

# Salvo il serial Number
time.sleep(0.04)
data_out = array('B', [127, 0])
res = aa_i2c_write(handle, addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
if (res < len(data_out)):
    print "I2C write error. Written bytes = " + str(res) + "\n"
time.sleep(0.04)
data_out = array('B', [196])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
    print "I2C read error. Error return code = " + str(res[0]) + "\n"
SN = ''
for item in data_in:
    SN = SN + chr(item)

# Salvo il vendor name
time.sleep(0.04)
data_out = array('B', [127, 0])
res = aa_i2c_write(handle, addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
if (res < len(data_out)):
    print "I2C write error. Written bytes = " + str(res) + "\n"
time.sleep(0.04)
data_out = array('B', [148])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
    print "I2C read error. Error return code = " + str(res[0]) + "\n"
VN = ''
for item in data_in:
    VN = VN + chr(item)

print 'Module under test id: ' + VN + ' ' + SN + '\n'
log=open(VN + '_' + SN + " eeprom_dump " + time.strftime('%H_%M_%d_%m_%Y.txt'),"w")
log.write("Lower Page 00 \n")


time.sleep(1)

#Leggo la lower page 0

data_out = array('B', [0])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [16])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [32])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [48])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [64])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [80])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [96])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [112])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

log.write("Upper Page 00 \n")

data_out = array('B', [128])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [144])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [160])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [176])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [192])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [208])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [224])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [240])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

log.write("Upper Page 01 \n")

time.sleep(0.04)
data_out = array('B', [127, 1])
res = aa_i2c_write(handle, addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 1
if (res < len(data_out)):
    print "I2C write error. Written bytes = " + str(res) + "\n"
time.sleep(0.04)

data_out = array('B', [128])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [144])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [160])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [176])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [192])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [208])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [224])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [240])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

log.write("Upper Page 02 \n")

time.sleep(0.04)
data_out = array('B', [127, 2])
res = aa_i2c_write(handle, addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 1
if (res < len(data_out)):
    print "I2C write error. Written bytes = " + str(res) + "\n"
time.sleep(0.04)

data_out = array('B', [128])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [144])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [160])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [176])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [192])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [208])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [224])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [240])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

log.write("Upper Page 03 \n")

time.sleep(0.04)
data_out = array('B', [127, 3])
res = aa_i2c_write(handle, addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 1
if (res < len(data_out)):
    print "I2C write error. Written bytes = " + str(res) + "\n"
time.sleep(0.04)

data_out = array('B', [128])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [144])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [160])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [176])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [192])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [208])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [224])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

data_out = array('B', [240])
data_in = array('B', [0 for i in range(16)])
res = aa_i2c_write_read(handle, addr, AA_I2C_NO_FLAGS, data_out, data_in)
tmp = ''
for item in data_in:
    tmp = tmp + str(hex(item))+','
tmp = tmp+'\n'
log.write(tmp)

log.close()