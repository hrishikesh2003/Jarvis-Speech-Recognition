import pyttsx3
import speech_recognition as sr
import os 
import webbrowser as wb
 
def my_speak(message):
    engine= pyttsx3.init()
    engine.say('{}' .format(message))
    engine.runAndWait()
    
    
def myCommand():
    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print('You said: ' + command + '/n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        assistant(myCommand())
        
    return command    
    
    
def assistant(command):
    
    if 'open YouTube' in command:
        chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
        url = 'https://www.youtube.com'
        wb.get(chrome_path).open(url)


    if 'hi' in command:
        my_speak('Hello')
        
    
    if 'what is your name' in command:
        my_speak(' I am Toto')
            
        
   
my_speak('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())   
    
my_speak(message)    