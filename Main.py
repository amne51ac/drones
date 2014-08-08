'''amne51ac and n1tr0'''
import mavlink, serial, socket
import serial.tools.list_ports
import pickle

HOST = ''
PORT = 50007

def listen():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    print 'Connected by', addr
    while 1:
        data = conn.recv(1024)
        if not data:
            break
        print pickle.loads(data)
        conn.sendall('Acknowledged')
    conn.close()
    pass

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

'''
#CODE FOR PHONE APP
#FOR PYTHONISTA
# coding: utf-8

import ui, location, socket

HOST = '172.20.10.7'
PORT = 50007

location.start_updates()

def button_action(sender):
	loc = location.get_location()
	label1 = sender.superview['label1']
	mode1 = sender.superview['mode1']
	if mode1.selected_index:
		label1.text = 'Drop package'
	else:
		label1.text = 'Place package'
	loc['mode'] = mode1.selected_index
	ret = transmit(loc)
	if ret:
		label1.text = str(ret)
		sender.enabled = False
	
def transmit(data):
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((HOST, PORT))
	s.sendall(str(data))
	return s.recv(1024)
	pass


ui.load_view('Drones').present('popover')
'''