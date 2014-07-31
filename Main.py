'''amne51ac and n1tr0'''
import pymavlink, serial
import serial.tools.list_ports

class Drones():
    
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
        '''
        ser = serial.Serial('/dev/ttyS1', 19200, timeout=1)
        ser.write('')
        x = ser.read()
        s = ser.read(10)
        line = ser.readline()
        
        ser.close()
        '''