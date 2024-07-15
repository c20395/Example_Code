#Example 10.16 Speech Recognition through Microphone
#pip3 install pyaudio
#pip install googletrans==3.1.0a0

import speech_recognition as sr
print(sr.__version__)

r = sr.Recognizer()
with sr.Microphone() as source:
    print(source)
    audio_data = r.record(source, duration=5)
    #audio_data = r.listen(source,timeout=1,phrase_time_limit=10)
    print("Recognizing...")
    # convert speech to text
    text = r.recognize_google(audio_data)
    #text = r.recognize_google(audio_data, language="es-ES")
    print(text)
