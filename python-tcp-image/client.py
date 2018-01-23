#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
fileName = "image.jpg"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
print "send picture:", fileName
fileOpen = open(fileName,'rb')
l = fileOpen.read(1024)
while (l):
    print 'sending ..'
    s.send(l)
    l = fileOpen.read(1024)
fileOpen.close()
print "done sending"
s.close()

    

