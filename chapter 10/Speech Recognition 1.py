# Example 10.17 Speech Recognition from an audio file
# pip install SpeechRecognition

# pip install pyaudio
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl
# pip install PyAudio‑0.2.11‑cp37‑cp37m‑win_amd64.whl

import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()
'''
recognize_bing(): Microsoft Bing Speech
recognize_google(): Google Web Speech API
recognize_google_cloud(): Google Cloud Speech - requires installation of the google-cloud-speech package
recognize_houndify(): Houndify by SoundHound
recognize_ibm(): IBM Speech to Text
recognize_sphinx(): CMU Sphinx - requires installing PocketSphinx
recognize_wit(): Wit.ai
'''
#mic = sr.Microphone()
#print(sr.Microphone.list_microphone_names())
#=================================================================
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
    #audio = r.record(source, duration=4)
    #audio = r.record(source, offset=4, duration=3)

print(type(audio))
print(r.recognize_google(audio))
