import speech_recognition as sr
import pyttsx3 
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice",voices[2].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()    

def take_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "alexa" in command:
            command = command.replace("alexa"," ")
            print(command)
    return command

def run_alexa():
    command = take_command()
    print(command)
    if "play" in command:
        song = command.replace("play"," ")
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif "time" in command:
        time = datetime.datetime.now().strftime("%I:%M:%S %p")
        talk("The time is "+time)
    elif "who is" in command:
        person = command.replace("who is"," ")
        info = wikipedia.summary(person,1)
        print(info)
        talk(info) 
    elif "date" in command:
        talk("Check the calander")
    elif "joke" in command:
        talk(pyjokes.get_joke())
    else:
        talk("plsea soa agin")
        
while True:
   run_alexa()
        