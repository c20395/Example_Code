# Example 10.35 Jarvis 1.py
# pip install wolframalpha
# pip install pyttsx3

import wolframalpha
client = wolframalpha.Client("XXX-XXXX")

import wikipedia

import PySimpleGUI as sg
sg.theme('LightGreen')

searchpanel = [[sg.InputText()],[sg.Button('Search'), sg.Button('Cancel')]]
resultspanel =[[sg.Text('Wolfram Result:', size =(20, 1))],
               [sg.Multiline("", key='Wolfram')],
               [sg.Text('Wikipedia Result:', size =(20, 1))],
               [sg.Multiline("", key='Wikipedia')],
               [sg.Frame('Search the Web:', searchpanel, font='Any 12', title_color='blue')],
              ]
layout = [[sg.Column(resultspanel)]]
window = sg.Window('Javis 1 ',location=(100, 100))
window.Layout(layout).Finalize()

#layout =[[sg.Text('Enter a command'), sg.InputText()],[sg.Button('Ok'), sg.Button('Cancel')]]
#window = sg.Window('PyDa', layout)

import pyttsx3
engine = pyttsx3.init()

searching = False
while True:
    event, values = window.read(timeout=20, timeout_key='timeout')
    if event == sg.WIN_CLOSED:      
        break
    elif event == 'Search':
        searching = True
    if event in (None, 'Cancel'):
        break
    if searching:
        wiki_res = wikipedia.summary(values[0], sentences=2)
        wolfram_res = next(client.query(values[0]).results).text
        engine.say(wiki_res)
        engine.say(wolfram_res)
        #sg.PopupNonBlocking("Wikipedia Result: "+wiki_res)
        window['Wolfram'].update(wolfram_res)   
        window['Wikipedia'].update(wiki_res)   

        engine.runAndWait()
        searching = False
        print (values[0])

window.close()
