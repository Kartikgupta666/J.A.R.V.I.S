import os
import eel
# from playsound import playsound


# def play():
#     music = "f:\\downloads\\synthesis.wav"
#     playsound(music)


def gui():
    eel.init("Source")
    # play()
    os.system('start msedge.exe --app="http://localhost:5500/Source/index.html"')
    eel.start('index.html' , mode=None , host='localhost' , block=True)