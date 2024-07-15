#Example 10.18 Speech Recognition from MP4

import os
import speech_recognition as sr

cmd1 = "E:\\ffmpeg\\bin\\ffmpeg -i Goal-GAN.mp4 Bolna.mp3"
failure = os.system(cmd1)
if failure:
    print ('Execution of "%s" failed!\n' % cmd1)


cmd2 = "E:\\ffmpeg\\bin\\ffmpeg -i Bolna.mp3 Bolna.wav"
failure = os.system(cmd2)
if failure:
    print ('Execution of "%s" failed!\n' % cmd2)

r = sr.Recognizer()
audio = sr.AudioFile('Bolna.wav')

with audio as source:
    audio = r.record(source, duration=100)
print(r.recognize_google(audio))

file1 = open("Bolna.txt","w") 
file1.writelines(r.recognize_google(audio))
file1.close() #to change file access modes
