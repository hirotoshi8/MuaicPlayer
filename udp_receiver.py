# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:01:53 2018

@author: danny
"""

import socket

class udp_receiver:
    def __init__(self, _ip_address = "127.0.0.1", _port = 6000):
        self.ip_address = _ip_address
        self.port = _port
        self.socket = 0
    
    def create(self, ip_address_str, port):
        self.ip_address = ip_address_str
        self.port = port
        
        self.rev_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.rev_socket.bind((self.ip_address, self.port))
        
    def receive(self):
        print("wait for the data")
        data, addr = self.rev_socket.recvfrom(1024)
        print("Receive: ", data)
        return data, addr
        
    def run(self):
        self.create("127.0.0.1", 6000)
        
        while True:
            data, add = self.receive()    
        
class udp_sender:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
    def create(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
#    def run(self, _ip_address = "127.0.0.1", _port = 6000, send_data):
#        self.create()
#        #send_data = b"1"
#        self.client_socket.sendto(send_data,(_ip_address, _port))
            
if __name__ == '__main__':
    udp = udp_receiver()
    udp.run()
    