import serial
import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
#import tmp102

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

def readSerial():
    with serial.Serial('/dev/tty.usbmodem141101', baudrate=9600, timeout=3) as ser:
    #ser.write('text')
        b = ser.read(60)
        a = ser.readline()
        strData = str(b)
        aS = strData.split("'")
        print(aS)

if __name__ == '__main__':
    while 1:
        readSerial()