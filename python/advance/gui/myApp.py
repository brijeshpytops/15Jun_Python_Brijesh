import os
import time
import random
import pygame

musics_dir = os.path.join('musics')
musics_ = os.listdir(musics_dir)

musics_list = []

if len(musics_) > 0:
    print("Available musics:")
    for music in musics_:
        if music.endswith('.mp3'):
            musics_list.append(music)

print(musics_list)


pygame.mixer.init()

def loopMusics():
    while True:
        for music in musics_list:
            getMusic(music)
            
def suffledMusics():
    random.shuffle(musics_list)
    for music in musics_list:
       getMusic(music)

def randomMusics():
    while True:
        music = random.choice(musics_list)
        getMusic(music)
        
def getMusic(music):
    pygame.mixer.music.load(os.path.join(musics_dir, music))
    pygame.mixer.music.play()
    
    if pygame.mixer.music.get_busy():
        time.sleep(1)

# def optMusic():
#     print("Choose a music option:")
#     print("1. Loop music")
#     print("2. Shuffle music")
#     print("3. Random music")
#     option = input("Enter a number: ")

    
#     if option == '1':
#         loopMusics()
#     elif option == '2':
#         suffledMusics()
#     elif option == '3':
#         randomMusics()
#     else:
#         print("Invalid option. Please try again.")

# if __name__ == '__main__':
#     optMusic()