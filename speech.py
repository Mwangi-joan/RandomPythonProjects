import pyttsx3

engine = pyttsx3.init()
engine.say("This is a text to speech in Python!")
engine.runAndWait()
engine.stop()
