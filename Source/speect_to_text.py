import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Use the microphone as the source for input
def listen():
    with sr.Microphone() as source:
        print("Please say something:")
        # Listen for the user's input
        audio = recognizer.listen(source)
        # recognizer.energy_threshold = 300
        recognizer.dynamic_energy_threshold = True
        # recognizer.pause_threshold = 0.8

        try:
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            return "Google Web Speech API could not understand the audio"
        except sr.RequestError as e:
            return e