# TDS3054 serial (with null modem) RS232 configured as 38400, 
# hardcopy configured to output PNG to RS232, 
# press hardcopy button 

# PNG format
# header:  89 50 4E 47 0D 0A 1A 0A 
#             P  N  G              
#
#          00 00 00 0D 49 48 44 52
#          [         ] I  H  D  R
#
# trailer: 49 45 4E 44 AE 42 60 82
#          I  E  N  D  [   CRC   ]


import argparse
import serial
from time import sleep
from datetime import datetime

header = b"\x89\x50\x4E\x47\x0D\x0A\x1A\x0A"
trailer = b"\x49\x45\x4E\x44\xAE\x42\x60\x82"
def hardcopy(fn='tds.png'):
    dat = b''
    while 1: 
        dat += ser.read(ser.in_waiting)
        if dat[-8:] == trailer:
            break
        sleep(0.5)
    with open(fn, mode='wb') as ofp:
        ofp.write(dat)

def main():
    global ser
    parser = argparse.ArgumentParser()
    parser.add_argument("-b", "--baudrate", type=int, default=38400, help="baudrate, default=%(default)s")
    parser.add_argument("-D", "--device", type=str, default="/dev/ttyUSB0", help="port name, default=%(default)s")
    args = parser.parse_args()
    ser = serial.Serial(args.device, args.baudrate, timeout=10)
    ser.reset_input_buffer()

    n = 1
    while 1:
        fn = 'tds-'+datetime.strftime(datetime.now(), '%m%d%y_%H%M%S')+'.png'
        hardcopy(fn)
        print(fn)
        n+=1

if __name__ == "__main__" :
    try:
        main()
    except KeyboardInterrupt:
        pass
