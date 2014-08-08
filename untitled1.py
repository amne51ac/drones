# -*- coding: utf-8 -*-
"""
Created on Sat Aug 02 15:25:25 2014

@author: amne51ac

All content licensed under GPL unless otherwise noted or required.
"""
import mavlink

class fifo(object):
    def __init__(self):
        self.buf = []
    def write(self, data):
        self.buf += data
        return len(data)
    def read(self):
        return self.buf.pop(0)

f = fifo()

# create a mavlink instance, which will do IO on file object 'f'
mav = mavlink.MAVLink(f)

# set the WP_RADIUS parameter on the MAV at the end of the link
mav.param_set_send(7, 1, "WP_RADIUS", 101)

# alternatively, produce a MAVLink_param_set object 
# this can be sent via your own transport if you like
m = mav.param_set_encode(7, 1, "WP_RADIUS", 101)

# get the encoded message as a buffer
b = m.get_msgbuf()

# decode an incoming message
m2 = mav.decode(b)

# show what fields it has
print("Got a message with id %u and fields %s" % (m2.get_msgId(), m2.get_fieldnames()))

# print out the fields
print(m2)