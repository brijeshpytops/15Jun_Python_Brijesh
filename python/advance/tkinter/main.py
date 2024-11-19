import os
import time
import random
import pygame

musics_dir = os.path.join('musics')
musics = os.listdir(musics_dir)

pygame.mixer.init()

def loopMusics():
    while True:
        for music in musics:
            getMusic(music)
            
def suffledMusics():
    musics = random.shuffle(musics)
    for music in musics:
       getMusic(music)

def randomMusics():
    while True:
        music = random.choice(musics)
        getMusic(music)
        
def getMusic(music):
    pygame.mixer.music.load(os.path.join(musics_dir, music))
    pygame.mixer.music.play()
    
    if pygame.mixer.music.get_busy():
        time.sleep(1)

def optMusic():
    print("Choose a music option:")
    print("1. Loop music")
    print("2. Shuffle music")
    print("3. Random music")
    option = input("Enter a number: ")

    
    if option == '1':
        loopMusics()
    elif option == '2':
        suffledMusics()
    elif option == '3':
        randomMusics()
    else:
        print("Invalid option. Please try again.")

if __name__ == '__main__':
    optMusic()