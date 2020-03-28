import smbus

bus = smbus.SMBus(1)

HH10D_EEPROM = 0x51

sens = [0,0]
off = [0,0]

bus.write_byte(HH10D_EEPROM, 0x0A)                            # Startadresse auf 10 einstellen
for adress in range(2):                                # Beide Sensitivity Bytes auslesen
    sens[adress - 1] = bus.read_byte(HH10D_EEPROM)
    
for adresse in range(2):                                # Beide Offset Bytes auslesen
    off[adress - 1] = bus.read_byte(HH10D_EEPROM)
    
# Daten umwand
print  sens[0] + (sens[1] << 8)
print  off[0] + (off[1] << 8)


