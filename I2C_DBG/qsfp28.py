import time
import math
import string
from aardvark_py import *
from array import array


class qsfp28:
    def __init__(self):
        self.addr = 0x50
        self.handle = aa_open(0)
        self.i2c_counter = 0
        if (self.handle <= 0):
            print "Unable to open Aardvark device on port 0"
            print "Error code = %d" % handle
            sys.exit()
        # Ensure that the I2C subsystem is enabled
        aa_configure(self.handle, AA_CONFIG_SPI_I2C)
        # Pull up resitors already present in the MCB
        aa_i2c_pullup(self.handle, AA_I2C_PULLUP_NONE)
        # I2C Master configuration
        aa_i2c_slave_disable(self.handle)
        # No Power supply provided by Aardwark module
        aa_target_power(self.handle, AA_TARGET_POWER_NONE)
        # I2C Bitrate
        aa_i2c_bitrate(self.handle, 100)

    def get_i2c_counter(self):
        return self.i2c_counter
		
    def get_serial_number(self):
        time.sleep(0.1)
        data_out = array('B', [127,0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out) #Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = "+ str(res)+"\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [196])
        data_in = array('B', [0 for i in range(16)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        SN=''
        for item in data_in:
            SN = SN + chr(item)
        return SN

    def get_vendor_PN(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [168])
        data_in = array('B', [0 for i in range(16)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        PN = ''
        for item in data_in:
            PN = PN + chr(item)
        return PN
			
    def get_vendor_revision(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [184])
        data_in = array('B', [0 for i in range(2)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        rev=''
        for item in data_in:
            rev = rev + chr(item)
        return rev
	
    def get_vendor_name(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [148])
        data_in = array('B', [0 for i in range(16)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        VN = ''
        for item in data_in:
            VN = VN + chr(item)
        return VN

		
    def get_voltage(self):
        time.sleep(0.1)
        data_out = array('B', [26])
        data_in = array('B', [0 for i in range(2)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        res = hex(data_in[0])+str(hex(data_in[1])[2:]).zfill(2) #forma 0x yy zz. If zz is composed by only one HEX value, zfill function will insert 0 on top of zz nibble
        tmp =int(res,0)
        return (tmp * 6.55)/65535

			
    def get_temperature(self):
        time.sleep(0.1)
        data_out = array('B', [22])
        data_in = array('B', [0 for i in range(2)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        string = hex(data_in[0])+str(hex(data_in[1])[2:]).zfill(2) #forma 0x yy zz. If zz is composed by only one HEX value, zfill function will insert 0 on top of zz nibble
        res=int(string,0)
        if res > 0x7fff:
            res -= 0x1000
        return (res * 1.0)/256

			
    def get_RX_power(self): #output value is in dBm
        time.sleep(0.1)
        data_out = array('B', [34])
        data_in = array('B', [0 for i in range(8)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        lane1= 10*math.log10((int((hex(data_in[0])+str(hex(data_in[1])[2:]).zfill(2)),16)+1)/10000.0)
        lane2= 10*math.log10((int((hex(data_in[2])+str(hex(data_in[3])[2:]).zfill(2)),16)+1)/10000.0)
        lane3= 10*math.log10((int((hex(data_in[4])+str(hex(data_in[5])[2:]).zfill(2)),16)+1)/10000.0)
        lane4= 10*math.log10((int((hex(data_in[6])+str(hex(data_in[7])[2:]).zfill(2)),16)+1)/10000.0)
        return [lane1,lane2,lane3,lane4]

	
    def get_TX_power(self):
        time.sleep(0.1)
        data_out = array('B', [50])
        data_in = array('B', [0 for i in range(8)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        lane1 = 10 * math.log10((int((hex(data_in[0]) + str(hex(data_in[1])[2:]).zfill(2)), 16) + 1) / 10000.0)
        lane2 = 10 * math.log10((int((hex(data_in[2]) + str(hex(data_in[3])[2:]).zfill(2)), 16) + 1) / 10000.0)
        lane3 = 10 * math.log10((int((hex(data_in[4]) + str(hex(data_in[5])[2:]).zfill(2)), 16) + 1) / 10000.0)
        lane4 = 10 * math.log10((int((hex(data_in[6]) + str(hex(data_in[7])[2:]).zfill(2)), 16) + 1) / 10000.0)
        return [lane1, lane2, lane3, lane4]

		
    def high_power_enable(self):
        time.sleep(0.1)
        data_out = array('B', [93,0x5])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "High Power mode enabled"


    def high_power_disable(self):
        time.sleep(0.1)
        data_out = array('B', [93, 0x0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "High Power mode disabled"

    def CDR_enable(self):
        time.sleep(0.1)
        data_out = array('B', [98, 0xFF])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "CDRs Enabled"
			
    def CDR_disable(self):
        time.sleep(0.1)
        data_out = array('B', [98, 0x00])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "CDRs Disabled"

    def get_CDR_status(self):
        time.sleep(0.1)
        data_out = array('B', [98])
        data_in = array('B', [0 for i in range(1)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        if hex(data_in[0]) == '0xff':
            return 'Enabled'
        else:
            return 'Disabled'

    def get_powerclass(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [129])
        data_in = array('B', [0 for i in range(1)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        PW=0
        if str(bin(data_in[0]))[2:].zfill(8)[0]=="0" and str(bin(data_in[0]))[2:].zfill(8)[1]=="0" and str(bin(data_in[0]))[2:].zfill(8)[6]=="0" and str(bin(data_in[0]))[2:].zfill(8)[7]=="0":
            PW=1
        if str(bin(data_in[0]))[2:].zfill(8)[0]=="1" and str(bin(data_in[0]))[2:].zfill(8)[1]=="0" and str(bin(data_in[0]))[2:].zfill(8)[6]=="0" and str(bin(data_in[0]))[2:].zfill(8)[7]=="0":
            PW=2
        if str(bin(data_in[0]))[2:].zfill(8)[0]=="0" and str(bin(data_in[0]))[2:].zfill(8)[1]=="1" and str(bin(data_inp[0]))[2:].zfill(8)[6]=="0" and str(bin(data_in[0]))[2:].zfill(8)[7]=="0":
            PW=3
        if str(bin(data_in[0]))[2:].zfill(8)[0]=="1" and str(bin(data_in[0]))[2:].zfill(8)[1]=="1" and str(bin(data_in[0]))[2:].zfill(8)[6]=="0" and str(bin(data_in[0]))[2:].zfill(8)[7]=="0":
            PW=4
        if str(bin(data_in[0]))[2:].zfill(8)[6]=="1" and str(bin(data_in[0]))[2:].zfill(8)[7]=="0":
            PW=5
        if str(bin(data_in[0]))[2:].zfill(8)[6]=="0" and str(bin(data_in[0]))[2:].zfill(8)[7]=="1":
            PW=6
        if str(bin(data_in[0]))[2:].zfill(8)[6]=="1" and str(bin(data_in[0]))[2:].zfill(8)[7]=="1":
            PW=7
        return PW
				
    def set_CTLE_fixed(self,a,b,c,d): #input are 4 int values, one for each lane example: module.set_CTLE_fixed(x,y,z,k)
        time.sleep(0.1)
        data_out = array('B', [127, 3])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [234,int(str(a)+str(b),16),int(str(c)+str(d),16)])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "Fixed CTLE peaking updated"

    def set_CTLE_adaptive_enable(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [193])
        data_in = array('B', [0 for i in range(1)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        if str(bin(data_in[0]))[2:].zfill(8)[4] == '1':
            time.sleep(0.1)
            data_out = array('B', [127,3])
            res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
            if (res < len(data_out)):
                print "I2C write error. Written bytes = " + str(res) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
                time.sleep(0.1)
            data_out = array('B', [241])
            data_in = array('B', [0 for i in range(1)])
            res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
            if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
                print "I2C read error. Error return code = " + str(res[0]) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
            time.sleep(0.1)
            data_out = array('B', [241, int((int(hex(data_in[0])[2:],16) | 0b00001111))])
            res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)
            if (res < len(data_out)):
                print "I2C write error. Written bytes = " + str(res) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
            print 'CTLE adaptive Enabled'
        else:
            print "Adaptive CTLE NOT supported"

			
    def set_CTLE_adaptive_disable(self):
        time.sleep(0.1)
        data_out = array('B', [127, 0])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 0
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [193])
        data_in = array('B', [0 for i in range(1)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        if str(bin(data_in[0]))[2:].zfill(8)[4] == '1':
            time.sleep(0.1)
            data_out = array('B', [127, 3])
            res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
            if (res < len(data_out)):
                print "I2C write error. Written bytes = " + str(res) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
            time.sleep(0.1)
            data_out = array('B', [241])
            data_in = array('B', [0 for i in range(1)])
            res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
            if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
                print "I2C read error. Error return code = " + str(res[0]) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
            time.sleep(0.1)
            data_out = array('B', [241, int((int(hex(data_in[0])[2:], 16) | 0b11110000))])
            res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)
            if (res < len(data_out)):
                print "I2C write error. Written bytes = " + str(res) + "\n"
                self.i2c_counter = self.i2c_counter + 1
                return "None"
            print 'CTLE adaptive Disabled'
        else:
            print "Adaptive CTLE NOT supported"



							
    def get_CTLE(self):
        time.sleep(0.1)
        data_out = array('B', [127, 3])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [234])
        data_in = array('B', [0 for i in range(2)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        return [str(hex(data_in[0]))[2:].zfill(2)[0],str(hex(data_in[0]))[2:].zfill(2)[1],str(hex(data_in[1]))[2:].zfill(2)[0],str(hex(data_in[1]))[2:].zfill(2)[1]]

    def get_RX_out_amplitude(self):
        time.sleep(0.1)
        data_out = array('B', [127, 3])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [238])
        data_in = array('B', [0 for i in range(2)])
        res = aa_i2c_write_read(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out, data_in)
        if (res[0] == 1) or (res[0] == 3) or (res[0] == 4) or (res[0] == 5) or (res[0] == 6):
            print "I2C read error. Error return code = " + str(res[0]) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        return [str(hex(data_in[0]))[2:].zfill(2)[0],str(hex(data_in[0]))[2:].zfill(2)[1],str(hex(data_in[1]))[2:].zfill(2)[0],str(hex(data_in[1]))[2:].zfill(2)[1]]

			
    def set_RX_out_amplitude(self,a,b,c,d):
        time.sleep(0.1)
        data_out = array('B', [127, 3])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)  # Set upper page to 3
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        time.sleep(0.1)
        data_out = array('B', [238, int(str(a) + str(b), 16), int(str(c) + str(d), 16)])
        res = aa_i2c_write(self.handle, self.addr, AA_I2C_NO_FLAGS, data_out)
        if (res < len(data_out)):
            print "I2C write error. Written bytes = " + str(res) + "\n"
            self.i2c_counter = self.i2c_counter + 1
            return "None"
        print "RX Out Amplitude updated"
		
		
