import smbus
import os

bus = smbus.SMBus(1)

DEVICE_ADRESS = 0x50

SERPRINT_REG = 0xFA
AUTODOWN_REG = 0xFB
BACKGRND_REG = 0xFC

SERPRINT_BYTE = 0xCC
AUTODOWN_BYTE = 0x0F
BACKGRND_BYTE = 0x00


def dump():
	for i in range(0,0xFF):
		b = bus.read_byte_data(DEVICE_ADRESS, i)
		print hex(i), hex(b)

#dump()
os.system("i2cdump -y 1 0x50")
print "WRITE BYTE...", 
data = 0x0A
bus.write_byte_data(DEVICE_ADRESS, BACKGRND_REG, BACKGRND_BYTE)
print "\tDONE"
os.system("i2cdump -y 1 0x50")
#dump()
bus.close()

