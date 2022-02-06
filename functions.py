version = "V-0.0.2"
mail = 'YOUR MAIL ID'
password = 'YOUR MAIL PASSWORD(DONT WORRY)'
import time
import sys
import os
import pyttsx
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser
import requests 
import bs4
import re
import json
from googlesearch import search
from urllib2 import urlopen

engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis. Please tell me how may I help you!")      
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Now Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(query)
    except Exception as e:    
        print("Say that again please...")  
        return "None"
    return query
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(mail, password)
    server.sendmail(mail, to, content)
    server.close()

def intro():
    speak("Hello Sir or Mam! I am JARVIS. nice to meet you!")

def animation():
    os.system("cls")
    load_str = "STARTING JARVIS..."
    ls_len = len(load_str)
    print(version)
  
    animation = "|/-\\"
    anicount = 0
      
    counttime = 0        

    i = 0                     
  
    while (counttime != 100):

        time.sleep(0.1)

        load_str_list = list(load_str) 
          
        x = ord(load_str_list[i])

        y = 0                             
  
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]

        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1

    if os.name =="nt":
        os.system("cls")
        print("Loaded!")
        time.sleep(1)
        os.system("cls")
        print("Author:Harshit Shah")
        time.sleep(1)
        os.system("cls")