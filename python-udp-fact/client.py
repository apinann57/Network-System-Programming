import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 50055
MESSAGE = "3"

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "message:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))

try:
    data, server = sock.recvfrom(1024)
    print "response factorial:", data
except timeout:
    print "no response"
