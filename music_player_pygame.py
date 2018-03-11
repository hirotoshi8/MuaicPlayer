# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:44:36 2018

@author: danny
"""

import pygame.mixer
import time

def run_mixer():
    # mixerモジュールの初期化
    pygame.mixer.init()
    
    # 音楽ファイルの読み込み
    pygame.mixer.music.load(r"./materials/decision5.mp3")
    # 音楽再生、および再生回数の設定(-1はループ再生)
    pygame.mixer.music.play(1)
    
    time.sleep(1)
    # 再生の終了
    pygame.mixer.music.stop()

#if 0    
def run_Sound():
        # mixerモジュールの初期化
    pygame.mixer.init()
    
    # 音楽ファイルの読み込み
    pygame.mixer.Sound(r"./materials/decision5.mp3")
    
    pygame.mixer.Sound.play()
    
    time.sleep(60)
    # 再生の終了
    pygame.mixer.music.stop()
#endif
    
if __name__ == '__main__':
    run_mixer()
    