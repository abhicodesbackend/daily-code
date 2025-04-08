#!/usr/bin/env python3

"""
udpRecv.py
Simple UDP receive program
Raghuram
BMSCE June 2019
https://wiki.python.org/moin/UdpCommunication
"""

import socket

Server_IP = "127.0.0.1"
Server_PORT = 60003

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((Server_IP, Server_PORT))

while True:
    try:
        print("Listening...")
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        print(f"received message - {addr}: {data}")
    except IOError as err:
        print(f"Error***: {err}")
    except KeyboardInterrupt as err:
        print("KBD intr exiting...")
        exit()
