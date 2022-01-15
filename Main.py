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