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
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
#       elif 'play music' in query:
#           songs = os.listdir(music_dir)
#           print(songs)    
#           os.startfile(os.path.join(music_dir, songs[0]))
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
                speak(e)
        elif 'email to person2' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "emailid of person2"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak(e)
        elif 'email to person3' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "emailid of person3"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak(e)
        elif 'jarvis' in query:
            intro()
        elif 'google' in query:
            query = query.replace('google', '')
            for results in search(query, tld="co.in", num=1, stop=1, pause=2):
                speak("Found! Redirecting")
                print(results)
                webbrowser.open(results)
        elif 'weather' in query:
            url = 'http://ipinfo.io/json'
            response = urlopen(url)
            data = json.load(response)
            city = data['city']
            google = "https://google.com/search?q=weather+in+" + city
            request_result = requests.get(google)
            soup = bs4.BeautifulSoup( request_result.text, "html.parser" )
            temp = soup.find( "div" , class_='BNeawe' ).text 
            speak("The temperature in")
            speak(city)
            speak("is")
            speak(temp)