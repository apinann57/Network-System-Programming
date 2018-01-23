import socket
import math

UDP_IP = "127.0.0.1"
UDP_PORT = 50055
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))
while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    print "received message:", data
    print "factorial:", math.factorial(int(data))
    sock.sendto(str(math.factorial(int(data))),(addr))
