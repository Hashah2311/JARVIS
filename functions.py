version = "V-0.1.5"
mail = 'YOUR MAIL ID'
password = 'YOUR MAIL PASSWORD(DONT WORRY)'
nversion = "V-beta-2"
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
import urllib

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
        time.sleep(2.5)
        os.system("cls")

def news():
    speak("Searching For News...")
    news_headlines = []
    res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3c7091dbbd9547cca52fcd852572d7a9&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    speak(news_headlines[:5])

def joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    jokes = res["joke"]
    speak(jokes)

def advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    advice = res['slip']['advice']
    speak(advice)

def unmute_mic():
    os.system("env\python.exe mic\process.py")

def updates():
    link = f"https://www.github.com/Hashah2311/JARVIS/releases/tag/{nversion}"
    try:
        urllib.request.urlopen(link)
        speak("Updates Available!")
        speak("Opening update page in browser")
        webbrowser.open(link)
    except urllib.error.HTTPError:
        speak("No new update available currently")