from chat import chat 
from speect_to_text import listen
from voice import speak

from gui import gui



if __name__ == "__main__" :
    gui()
    query = listen()
    sunai = False
    if sunai is False :
        
            if "mark" in query:
                speak("yes sir . i'm here")
                sunai = True
                
                query = listen()
                result = chat(query)

                speak(result)
    else:
        quit()