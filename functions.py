try:
    version = "V-0.3.5"
    mail = 'YOUR MAIL ID'
    password = 'YOUR MAIL PASSWORD(DONT WORRY)'
    nversion = "V-beta-4"
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
    import wolframalpha
    import pyaudio
    import pyfiglet
    
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
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print("Recognizing...")
        try:    
            query = r.recognize_google(audio, language='en-IN')
            print(f"User Said:{query}")
        except Exception:
            query = r.recognize_sphinx(audio, language='en-US')
            print(f"User Said:{query}")
        except Exception as e:
            #print(e)
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
            result = pyfiglet.figlet_format("JARVIS")
            print("Loaded!")
            time.sleep(1)
            print(result)
            time.sleep(5)
            os.system("cls")
            print("Author:Harshit Shah")
            time.sleep(2)
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
    
    def calculate(question):
        try:
            client = wolframalpha.Client("42H99P-JYULKAR7QQ")
            answer = client.query(question)
            answer = next(answer.results).text
            speak(answer)
        except:
            speak("Sorry sir, I couldn't fetch your question's answer. Please try again.")
except Exception as error:
    if 'Keyboard Interrupt' in error:
        print("Assistant exited manually. Exiting JARVIS.")
        exit()
    else:
        print("An error occured while running the code. Submitting the error to Github and restarting....")
        file = open("Error.functions.py.log", "a")
        file.write(str(error))
        file.close()
        try:
            import requests
            import json
            import os
            token = "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"
            headers = {f"Authorization" : "token {token}"}
            data = {"title": "JARVIS Error Reporting System Reported An Error"}
            label = {"labels": ["Error"]}
            body = {"body": [error]}
            url = "https://api.github.com/repos/Hashah2311/JARVIS/issues"
            requests.post(url,data=json.dumps(data,label,body),headers=headers)
            os.system("run.cmd")
            #exit()
        except:
            print("Critical Crash!")
            exit()
