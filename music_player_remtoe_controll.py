# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:44:36 2018

@author: danny
"""
import music_player_pygame
import udp_communicator

    
if __name__ == '__main__':
    udp = udp_communicator.udp_receiver()    
    udp.create("127.0.0.1", 6000)
        
    while True:
        data, add = udp.receive()
        music_player_pygame.run_mixer()
