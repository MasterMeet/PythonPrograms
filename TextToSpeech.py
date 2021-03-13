import speech_recognition as sr
f = open("FileOp.py","r+")

engine = pyttsx3.init()
vc = engine.getProperty('voices')
engine.setProperty('voices', vc[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

for line in f:
   speak(audio)
f.close()