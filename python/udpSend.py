#!/usr/bin/env python3

"""
udpSend.py
Simple UDP send program
Raghuram
BMSCE June 2019
https://wiki.python.org/moin/UdpCommunication
"""

import socket

Server_IP = "127.0.0.1"
Server_PORT = 60003
MESSAGE = "Hello World!"

print("UDP target IP:", Server_IP)
print("UDP target port:", Server_PORT)
print("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

sock.sendto(bytes(MESSAGE,'utf-8'), (Server_IP, Server_PORT))
