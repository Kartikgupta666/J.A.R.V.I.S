import pyttsx3

engine = pyttsx3.init()
engine.setProperty('rate' , 140)


def speak(text):

    engine.say(text)

    engine.runAndWait()
    
