'''amne51ac and n1tr0'''
import pymavlink, serial
import serial.tools.list_ports


def comports():
    a = []
    b = serial.tools.list_ports.comports()
    
    while True:
        try:
            a.append(b.next())
        except:
            break
    
    return a

def connect():
    ser = serial.Serial(0, 57600, timeout=10)
    ser.write('')
    ser.read()
    ser.readline()
    ser.close()