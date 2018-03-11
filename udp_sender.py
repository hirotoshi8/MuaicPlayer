# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 19:32:52 2018

@author: danny
"""

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
send_data = b"1"
client.sendto(send_data,("127.0.0.1",6000))