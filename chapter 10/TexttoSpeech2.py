#Example 10.15 Text to Speech 2
#pip install pyttsx3
#pip install googletrans==3.1.0a0

import pyttsx3

file_name = 'Bolna.txt'
text = open(file_name).read()

engine = pyttsx3.init()
engine.say(text)
engine.runAndWait()
