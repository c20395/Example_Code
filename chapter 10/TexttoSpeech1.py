#Example 10.14 Text to Speech
#pip install pyttsx3

import pyttsx3

text = "Welcome to London!"

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
