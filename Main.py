'''amne51ac and n1tr0'''
import mavlink, serial, socket
import serial.tools.list_ports
import pickle
from pymavlink import mavutil

HOST = 'mavdrop.com'
PORT = 51337



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

def test():
m     return mavutil.mavlink_connection('com16', baud=57600)
    

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(100)
    s.connect((HOST, PORT))
    s.settimeout(None)
    
    while 1:
        data = s.recv(1024)
        if data:
            loc = pickle.loads(data)
            print loc
            break
    
    try:
        m = mavutil.mavlink_connection('com12', baud=57600)
    except:
        print 'Mavlink Error'
        return
    
    wplist = []
    
    wplist.append({'description':'set home',
                   'seq':0,
                   'frame':2,
                   'command':179,
                   'current':1,
                   'autocontinue':1,
                   'param1':1,
                   'param2':0,
                   'param3':0,
                   'param4':0,
                   'x':0,
                   'y':0,
                   'z':0,
                   })
    wplist.append({'description':'takeoff',
                   'seq':1,
                   'frame':2,
                   'command':22,
                   'current':0,
                   'autocontinue':1,
                   'param1':0,
                   'param2':0,
                   'param3':0,
                   'param4':0,
                   'x':0,
                   'y':0,
                   'z':0,
                   })
    wplist.append({'description':'fly to destination',
                   'seq':2,
                   'frame':2,
                   'command':16,
                   'current':0,
                   'autocontinue':1,
                   'param1':0,
                   'param2':0,
                   'param3':0,
                   'param4':0,
                   'x':loc['longitude'],
                   'y':loc['latitude'],
                   'z':20,
                   })
    if loc['mode'] == 0:
        wplist.append({'description':'land',
                       'seq':3,
                       'frame':2,
                       'command':21,
                       'current':0,
                       'autocontinue':1,
                       'param1':0,
                       'param2':0,
                       'param3':0,
                       'param4':0,
                       'x':0,
                       'y':0,
                       'z':0,
                       })'''
        wplist.append({'description':'release package',
                       'seq':4,
                       'frame':2,
                       'command':'',
                       'current':0,
                       'autocontinue':1,
                       'param1':'',
                       'param2':'',
                       'param3':'',
                       'param4':'',
                       'x':'',
                       'y':'',
                       'z':'',
                       })'''
        wplist.append({'description':'takeoff',
                       'seq':5,
                       'frame':2,
                       'command':22,
                       'current':0,
                       'autocontinue':1,
                       'param1':0,
                       'param2':0,
                       'param3':0,
                       'param4':0,
                       'x':0,
                       'y':0,
                       'z':0,
                       })
    else:
        wplist.append({'description':'lower',
                       'seq':3,
                       'frame':2,
                       'command':16,
                       'current':0,
                       'autocontinue':1,
                       'param1':0,
                       'param2':0,
                       'param3':0,
                       'param4':0,
                       'x':loc['latitude'],
                       'y':loc['longitude'],
                       'z':3,
                       })'''
        wplist.append({'description':'release package',
                       'seq':4,
                       'frame':2,
                       'command':'',
                       'current':0,
                       'autocontinue':1,
                       'param1':'',
                       'param2':'',
                       'param3':'',
                       'param4':'',
                       'x':'',
                       'y':'',
                       'z':'',
                       })'''
        wplist.append({'description':'raise',
                       'seq':5,
                       'frame':2,
                       'command':16,
                       'current':0,
                       'autocontinue':1,
                       'param1':0,
                       'param2':0,
                       'param3':0,
                       'param4':0,
                       'x':loc['latitude'],
                       'y':loc['longitude'],
                       'z':10,
                       })
    wplist.append({'description':'rtl',
                   'seq':6,
                   'frame':2,
                   'command':20,
                   'current':0,
                   'autocontinue':1,
                   'param1':0,
                   'param2':0,
                   'param3':0,
                   'param4':0,
                   'x':0,
                   'y':0,
                   'z':0,
                   })
    wplist.append({'description':'land',
                   'seq':7,
                   'frame':2,
                   'command':21,
                   'current':0,
                   'autocontinue':0,
                   'param1':0,
                   'param2':0,
                   'param3':0,
                   'param4':0,
                   'x':0,
                   'y':0,
                   'z':0,
                   })

    s.send('Acknowledge')
    
    for i in wplist:
        m.write(m.mav.mission_item_encode(m.target_system, m.target_component, i['seq'],
                                  i['frame'], i['command'], i['current'],
                                  i['autocontinue'], i['param1'], i['param2'],
                                  i['param3'], i['param4'], i['x'], i['y'],
                                  i['z'])
                      
    m.write()
    m.set_mode_auto()
    m.arducopter_arm()
    
    s.send('Enroute')
    
    while 1:
        data = s.recv(1024)
        if data:
            print data
            break

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