# TDS3054 serial (with null modem) RS232 configured as 38400, 
# hardcopy configured to output PNG to RS232

# PNG format
# header:  89 50 4E 47 0D 0A 1A 0A 
#             P  N  G              
#
#          00 00 00 0D 49 48 44 52
#          [         ] I  H  D  R
#
# trailer: 49 45 4E 44 AE 42 60 82
#          I  E  N  D  [   CRC   ]



import serial

ser = serial.Serial("COM5", 38400, timeout=5)

def hardcopy(fn='tds.png'):
    with open(fn, mode='wb') as ofp:
        dat = ser.read_all()
        ofp.write(dat)
