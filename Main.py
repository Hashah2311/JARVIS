try:
    from functions import *
    music_dir = 'PATH TO ANY SONG FILE'
    if __name__ == "__main__":
        animation()
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                speak('Searching Wikipedia...')
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=5)
                speak("Here's what I found")
                speak("According to Wikipedia")
                speak(results)
            elif 'open google' in query:
                webbrowser.open("google.com")
#            elif 'play music' in query:
#                songs = os.listdir(music_dir)
#                print(songs)    
#                os.startfile(os.path.join(music_dir, songs[0]))
            elif 'time' in query:
                time = "Sir, the time is", datetime.datetime.now().strftime("%H:%M:%S")    
                speak(time)
            elif 'email to person1' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "emailid of person1"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email. Perhaps check your internet connection and Editions.txt file.")
            elif 'email to person2' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "emailid of person2"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email. Perhaps check your internet connection and Editions.txt file.")
            elif 'email to person3' in query:
                try:
                    speak("What should I say?")
                    content = takeCommand()
                    to = "emailid of person3"    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                except Exception as e:
                    print(e)
                    speak("Unable to send the email. Perhaps check your internet connection and Editions.txt file.")
            elif 'jarvis' in query:
                intro()
            elif 'google' in query:
                speak("Searching Google...")
                query = query.replace('google', '')
                query = query.replace(' ', '+')
                google = "https://google.com/search?q=" + query
                speak("Found! Redirecting...")
                webbrowser.open(google)
            elif 'weather' in query:
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
            elif 'what is my ip' in query:
                speak("Searching for your ip...")
                base = requests.get('https://api64.ipify.org?format=json').json()
                ip = base['ip']
                speak("Your ip is")
                speak(ip)
            elif 'youtube' in query:
                speak("What should I search?")
                search = takeCommand()
                speak("Ok. Searching Youtube...")
                search = search.replace(' ', '+')
                youtube = "https://www.youtube.com/results?search_query=" + search
                speak("Found! Opening youtube...")
                webbrowser.open(youtube)
            elif 'news' in query:
                news()
            elif 'joke' in query:
                joke()
            elif 'advice' in query:
                advice()
            elif 'exit' in query:
                speak("Good bye! have a nice day!")
                exit()
            elif 'mic' in query:
                speak("Ok sir!")
                unmute_mic()
            elif "check for updates" in query:
                updates()
            elif "calculate" in query:
                query = query.replace('calculate ', '')
                calculate(query)
            else:
                if 'none' in query:
                    e = "error"
                else:
                    speak("Searching Google for")
                    speak(query)
                    query = query.replace('google', '')
                    query = query.replace(' ', '+')
                    google = "https://google.com/search?q=" + query
                    speak("Found! Opening On google.")
                    webbrowser.open(google)

except Exception as error:
    if 'Keyboard Interrupt' in error:
        print("Assistant exited manually. Exiting JARVIS.")
        exit()
    else:
        print("An error occured while running the code. Submitting the error to Github and restarting....")
        file = open("Error.main.py.log", "a")
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