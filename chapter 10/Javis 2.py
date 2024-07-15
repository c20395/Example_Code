# Example 10.36 Jarvis conversation
# Modified based on:
# https://www.geeksforgeeks.org/personal-voice-assistant-in-python/
# pip install speechrecognition
# pip install playsound
# pip install gtts
# pip install selenium
# pip install pyaudio

# importing speech recognition package from google api
import speech_recognition as sr 
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 

import os # to save/open files 
import wolframalpha # to calculate strings into formula 
from selenium import webdriver # to control browser operations 
#driver = webdriver.Firefox(executable_path=r'E:\\geckodriver.exe')

num = 1
def assistant_speaks(output): 
	global num 

	# num to rename every audio file 
	# with different name to remove ambiguity 
	num += 1
	print("PerSon : ", output) 

	toSpeak = gTTS(text = output, lang ='en', slow = False) 
	# saving the audio file given by google text to speech 
	file = str(num)+".mp3 "
	toSpeak.save(file) 
	
	# playsound package is used to play the same file. 
	playsound.playsound(file, True) 
	os.remove(file) 



def get_audio(): 

	rObject = sr.Recognizer() 
	audio = '' 

	with sr.Microphone() as source: 
		print("Speak...") 
		
		# recording the audio using speech recognition 
		audio = rObject.listen(source, phrase_time_limit = 5) 
	print("Stop.") # limit 5 secs 

	try: 

		text = rObject.recognize_google(audio, language ='en-US') 
		print("You : ", text) 
		return text 

	except: 

		assistant_speaks("Could not understand your audio, PLease try again !") 
		return 0


def process_text(input): 
	try: 
		if 'search' in input: 
			# a basic web crawler using selenium 
			driver = webdriver.Chrome()
			driver.implicitly_wait(1)
			driver.maximize_window() 

			indx = input.lower().split().index('google') 
			query = input.split()[indx + 1:] 
			driver.get("https://www.google.com/search?q =" + '+'.join(query)) 
			return

		elif "calculate" in input.lower(): 
			
			# write your wolframalpha app_id here 
			app_id = "XXX-XXXX"
			client = wolframalpha.Client(app_id) 

			indx = input.lower().split().index('calculate') 
			query = input.split()[indx + 1:] 
			res = client.query(' '.join(query)) 
			answer = next(res.results).text 
			assistant_speaks("The answer is " + answer) 
			return

		elif 'open microsoft word' in input: 
			
			# another function to open 
			# different application availaible 
		        assistant_speaks("Opening Microsoft Word") 
		        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office\\Microsoft Word 2010.lnk')
		        return

		else: 
			assistant_speaks("....") 

	except : 

		assistant_speaks("I don't understand, please try again.") 

# Driver Code 
if __name__ == "__main__": 
	assistant_speaks("What's your name, Human?") 
	name ='Human'
	name = get_audio() 
	assistant_speaks("Hello, " + name + '.') 
	
	while(1): 

		assistant_speaks("What can i do for you?") 
		text = get_audio().lower() 

		if text == 0: 
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text): 
			assistant_speaks("Ok bye, "+ name+'.') 
			break

		# calling process text to process the query 
		process_text(text) 
