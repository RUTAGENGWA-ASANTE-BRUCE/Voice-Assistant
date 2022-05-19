
import pyttsx3 as p
from selenium import webdriver
import speech_recognition as sr
import wikipedia


salva =p.init()
voices=salva.getProperty("voices")
salva.setProperty("rate",150)
salva.setProperty("voice",voices[1].id)

def speak(search):
    salva.say(search)
    salva.runAndWait()

speak("""  Hello bruce, How are you ?
                     """)

r=sr.Recognizer()
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)

if "what" and "about" and "you":
    speak("I had a good day sir.")
speak("what can I do for you ?")

with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("Listening")
    audio=r.listen(source)
    text2=r.recognize_google(audio)
    print(text)

if "information" in text2:
    speak("You need information about what ?")
    with sr.Microphone() as source:
     r.energy_threshold=10000
     r.adjust_for_ambient_noise(source,1.2)
     print("Listening")
     audio=r.listen(source)
     text3=r.recognize_google(audio)
     print(text3)
    speak(f"searching {text3}")
    

info=wikipedia.summary(text3)
my_list=info.split(".")
value=0
while True:
    speak(my_list[value])
    print(my_list[value])
    if value<my_list:
     value+=1
        
    salva.runAndWait()

    continue
salva.stop()
