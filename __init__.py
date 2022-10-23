try:

    mail = 'YOUR MAIL ID'
    password = 'YOUR MAIL PASSWORD(DONT WORRY)'
    version = "V-0.5.0"
    nversion = "V-beta-5.5"

    def dependencies():
        try:
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
            import json
            import urllib
            import wolframalpha
            import pyfiglet
            import pyautogui as gui
        except ImportError:
            import os
            os.system("cls")
            print("Installing Dependencies")
            env = "env\python.exe"
            os.system(f"{env} -m pip install bs4 datetime pipwin psutil pyautogui pyfiglet pypiwin32 requests speechRecognition wheel Wikipedia wolframalpha")
            os.system(f"{env} -m pip uninstall pyttsx")
            os.system(f"{env} -m pip install git+https://github.com/jpercent/pyttsx.git")
            os.system(f"{env} -m pipwin install pocketsphinx")
            os.system(f"{env} -m pipwin install Pyaudio")
            os.system("cls")
            os.system(f"{env} __main__.py")

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
    import json
    import urllib
    import wolframalpha
    import pyfiglet
    import pyautogui as gui

    def speak(audio):
        engine = pyttsx.init('sapi5')
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[1].id)
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
        time.sleep(2)
        os.system('cls')

    def takeCommand():
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            print("Now Listening...")
            r.pause_threshold = 1
            audio = r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            print("Recognizing...")
        try:    
            query = r.recognize_google(audio, language='en-IN')
            print(f"User Said:{query}")
        except sr.RequestError:
            query = r.recognize_sphinx(audio, language='en-US')
            print(f"User Said:{query}")
        except sr.UnknownValueError:
            print("Say that again please...")
            time.sleep(1)
            os.system('cls')
            return 'none'
        return query

    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(mail, password)
        server.sendmail(mail, to, content)
        server.close()

    def animation():
        #A = "[----------]"
        #B = "[#---------]"
        #C = "[##--------]"
        #D = "[###-------]"
        #E = "[####------]"
        #F = "[#####-----]"
        #G = "[######----]"
        #H = "[#######---]"
        #I = "[########--]"
        #J = "[#########-]"
        #K = "[##########]"
        os.system("cls")
        load_str = "STARTING JARVIS"
        ls_len = len(load_str)
        print(version)
      
        animation = "|/-\\"
        #animation = A,B,C,D,E,F,G,H,I,J,K
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
        try:
            speak("Searching For News...")
            news_headlines = []
            res = requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=3c7091dbbd9547cca52fcd852572d7a9&category=general").json()
            articles = res["articles"]
            for article in articles:
                news_headlines.append(article["title"])
            speak(news_headlines[:5])
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def joke():
        try:
            headers = {
                'Accept': 'application/json'
            }
            res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
            jokes = res["joke"]
            speak(jokes)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")
    
    def advice():
        try:
            res = requests.get("https://api.adviceslip.com/advice").json()
            advice = res['slip']['advice']
            speak(advice)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")
    
    def unmute_mic():
        os.system("env\python.exe mic\process.py")
    
    def updates():
        try:
            link = f"https://www.github.com/Hashah2311/JARVIS/releases/tag/{nversion}"
            try:
                urllib.request.urlopen(link)
                speak("Updates Available!")
                speak("Opening update page in browser")
                webbrowser.open(link)
            except urllib.error.HTTPError:
                speak("No new update available currently")
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")
    
    def calculate(question):
        try:
            client = wolframalpha.Client("42H99P-JYULKAR7QQ")
            answer = client.query(question)
            answer = next(answer.results).text
            speak(answer)
        except:
            speak("Sorry sir, I couldn't fetch your question's answer. Please try again.")
    
    def wikipedia_search(query):
        try:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=5)
            speak("Here's what I found")
            speak("According to Wikipedia")
            speak(results)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")
    
    def google_search(query):
        try:
            speak("Searching Google...")
            query = query.replace('google', '')
            query = query.replace(' ', '+')
            google = "https://google.com/search?q=" + query
            speak("Found! Redirecting...")
            webbrowser.open(google)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def get_weather():
        try:
            speak("Detecting your city...")
            url = 'https://ipgeolocation.abstractapi.com/v1/?api_key=85ef8f826f7e42c6ad55b2f3f2d45758'
            response = urllib.request.urlopen(url)
            data = json.load(response)
            city = data['city']
            speak("Getting weather for")
            speak(city)
            google = "https://google.com/search?q=weather+in+" + city
            google2 = requests.get(google)
            soup = bs4.BeautifulSoup(google2.text, "html.parser" )
            temp = soup.find( "div" , class_='BNeawe' ).text
            weather_url = 'https://api.openweathermap.org/data/2.5/weather?' + 'q=' + city + '&appid=6df3640e0f36dfc3479361494ac0dfcd'
            request_result = requests.get(weather_url)
            data = request_result.json()
            main = data['main']
            humidity = main['humidity'], "%"
            speak("Condition in your city:")
            speak("Temperature:")
            speak(temp)
            speak("Humidity:")
            speak(humidity)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def get_ip():
        try:
            speak("Searching for your ip...")
            base = requests.get('https://api64.ipify.org?format=json').json()
            ip = base['ip']
            speak("Your ip is")
            speak(ip)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def search_youtube():
        try:
            speak("What should I search?")
            search = takeCommand()
            speak("Ok. Searching Youtube...")
            search = search.replace(' ', '+')
            youtube = "https://www.youtube.com/results?search_query=" + search
            speak("Found! Opening youtube...")
            webbrowser.open(youtube)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def search_google(query):
        try:
            speak("Searching Google for")
            speak(query)
            query = query.replace('google', '')
            query = query.replace(' ', '+')
            google = "https://google.com/search?q=" + query
            speak("Found! Opening On google.")
            webbrowser.open(google)
        except:
            speak("No Internet Connection Detected. Please connect to internet and try again")

    def subtitles():
        gui.hotkey('win', 'ctrl', 'l')

except KeyboardInterrupt:
    import os
    os.system("cls")
    print("Assistant exited manually. Exiting JARVIS.")
    exit()
except Exception as error:
    import os
    os.system("cls")
    print("An error occured while running the code. Submitting the error to Github....")
    import toke as token
    tok = token.token
    e = f"{error!r}: Error occured while a JARVIS user was using the bot"
    import requests
    import json
    headers = {"Authorization" : "token {}".format(tok)}
    data2 = {"title": "JARVIS Error Reporting System Reported An Error", "labels": ["Error"], "body": (e)}
    url = "https://api.github.com/repos/Hashah2311/JARVIS/issues"
    requests.post(url,data=json.dumps(data2),headers=headers)
    exit()