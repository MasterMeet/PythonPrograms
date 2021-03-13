import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
vc = engine.getProperty('voices')
engine.setProperty('voices', vc[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish():
    name = "Master"
    hour = datetime.datetime.now().hour
    if 12 > hour >= 6:
        speak(f"Good Morning {name}!")
    elif 18 > hour >= 12:
        speak(f"Good Afternoon {name}!")
    elif 22 > hour >= 18:
        speak(f"Good Evening {name}!")
    else:
        speak(f"Good Night {name}!")
    speak("I am Your Assistant ! How can I help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing........")
        com = r.recognize_google(audio, language='en-in')
        print(f"User said{com}")
        return "None"

        if 'open youtube' in com:
            speak("Opening Youtube...")
            webbrowser.open("www.youtube.com")
        elif 'open google' in com:
            speak("Opening Google...")
            webbrowser.open("www.google.com")
        else:
            speak("Command Not Found!")



wish()
take_command()