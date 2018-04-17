from aardvark_py import *
from array import array

data_out=array('B',[196])
data_in=array('B',[0 for i in range (16)])

handle = aa_open(0)
if (handle <= 0):
    print "Unable to open Aardvark device on port 0"
    print "Error code = %d" % handle
    sys.exit()

# Ensure that the I2C subsystem is enabled
aa_configure(handle, AA_CONFIG_SPI_I2C)


aa_i2c_pullup(handle, AA_I2C_PULLUP_NONE)

aa_i2c_slave_disable(handle)

aa_target_power(handle, AA_TARGET_POWER_NONE)

bitrate = aa_i2c_bitrate(handle, 400)
print "Bitrate set to 100 kHz"
#aa_i2c_read_ext (handle, 0x50, 0x00, data_in)

data = aa_i2c_write_read (handle,0x50,0x00,data_out,data_in)

print data[0]
print data_in
print data_in[2]
for item in data_in:
    print chr(item)

# Close the device
aa_close(handle)