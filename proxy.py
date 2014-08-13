# -*- coding: utf-8 -*-
"""
Retransmission Proxy for Drones project, use retrans function, listen is junk.

to be used on amne51ac AWS server

Created on Thu Aug 07 21:52:25 2014

@author: amne51ac

All content licensed under GPL unless otherwise noted or required.
"""
from pymavlink import mavutil

def listen():
    import socket, pickle
    PORT = 51337
    HOST = ''
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
        conn.send('Acknowledged')
    conn.close()
    pass

def retrans():
    import socket
    
    PORT = 51337
    HOST = ''
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    
    s.listen(1)
    sconn, saddr = s.accept()
    print 'Server %s connected' %str(saddr)
    sconn.send('Accepted')
    
    s.listen(1)
    mconn, maddr = s.accept()
    mconn.send('Accepted')
    sconn.send('Mobile Client Connected')
    print 'Client %s connected' %str(maddr)
    
    while 1:
        data = mconn.recv(1024)
        if data:
            sconn.send(data)
            print 'Requested'
            break
        
    while 1:
        data = sconn.recv(1024)
        if data:
            mconn.send(data)
            print 'Received'
            break
        
    while 1:
        data = sconn.recv(1024)
        if data:
            mconn.send(data)
            print 'Enroute'
            break
        
    while 1:
        data = mconn.recv(1024)
        if data:
            sconn.send(data)
            print 'Delivered'
            break
        
    mconn.close()
    sconn.close()
    
def communicate():
    m = mavutil.mavlink_connection('com14', baud=57600, autoreconnect=True)
    m.
    