try:
    from functions import *
    music_dir = 'PATH TO ANY SONG FILE'
    if __name__ == "__main__":
        animation()
        wishMe()
        while True:
            query = takeCommand().lower()
            if 'wikipedia' in query:
                wikipedia_search(query)
            elif '.com' in query:
                if 'open' in query:
                    query =  query.replace('open', '')
                    webbrowser.open(query)
                else:
                    webbrowser.open(query)
    #        elif 'play music' in query:
    #            songs = os.listdir(music_dir)
    #            print(songs)    
    #            os.startfile(os.path.join(music_dir, songs[0]))
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
            elif 'google' in query:
                google_search(query)
            elif 'weather' in query:
                get_weather()
            elif 'what is my ip' in query:
                get_ip()
            elif 'youtube' in query:
                search_youtube()
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
            elif 'subtitles' in query:
                speak("starting subtitles...")
                subtitles()
            else:
                search_google(query)

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