import serial
import signal
import time

#device_rpi = '/dev/ttyUSB0'
device_mac = '/dev/cu.wchusbserial1420'
arduino_sd = serial.Serial(device_mac, 115200)

file = open('audio.txt', 'wb')

while 1:
    file.write(arduino_sd.readline())

def exit_handler():
    print('My application is ending!')
    file.close()

signal.signal(signal.SIGINT, exit_handler)

