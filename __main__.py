try:
    from __init__ import *
    music_dir = 'PATH TO ANY SONG FILE'
    if __name__ == "__main__":
        dependencies()
        animation()
        wishMe()
        t = 0
        while True:
            if t <=10:
                query = takeCommand().lower()
                if 'wikipedia' in query:
                    wikipedia_search(query)
                    t = t * 0
                elif '.com' in query:
                    if 'open' in query:
                        query =  query.replace('open', '')
                        webbrowser.open(query)
                    else:
                        webbrowser.open(query)
                    t = t * 0
                elif 'play music' in query:
                    songs = os.listdir(music_dir)
                    print(songs)    
                    os.startfile(os.path.join(music_dir, songs[0]))
                    t = t * 0
                elif 'time' in query:
                    time = "Sir, the time is", datetime.datetime.now().strftime("%H:%M:%S")    
                    speak(time)
                    t = t * 0
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
                    t = t * 0
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
                    t = t * 0
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
                    t = t * 0
                elif 'google' in query:
                    google_search(query)
                    t = t * 0
                elif 'weather' in query:
                    get_weather()
                    t = t * 0
                elif 'what is my ip' in query:
                    get_ip()
                    t = t * 0
                elif 'youtube' in query:
                    search_youtube()
                    t = t * 0
                elif 'news' in query:
                    news()
                    t = t * 0
                elif 'joke' in query:
                    joke()
                    t = t * 0
                elif 'advice' in query:
                    advice()
                    t = t * 0
                elif 'exit' in query:
                    speak("Good bye! have a nice day!")
                    exit()
                    t = t * 0
                elif 'mic' in query:
                    speak("Ok sir!")
                    unmute_mic()
                    t = t * 0
                elif "check for updates" in query:
                    updates()
                    t = t * 0
                elif "calculate" in query:
                    query = query.replace('calculate ', '')
                    calculate(query)
                    t = t * 0
                elif 'subtitles' in query:
                    speak("starting subtitles...")
                    subtitles()
                    t = t * 0
                else:
                    if query == 'none':
                        t = t + 1
                    else:
                        search_google(query)
            else:
                os.system('cls')
                print("Going to sleep...")
                print("To wake me up just say \"Wake up JARVIS\"")
                hot_word = "wake"
                with sr.Microphone() as source:
                    r = sr.Recognizer()
                    r.pause_threshold = 2
                    audio = r.listen(source)
                    try:
                        query = r.recognize_google(audio, language='en-IN')
                    except sr.RequestError:
                        query = r.recognize_sphinx(audio, language='en-US')
                    query = query.lower()
                if hot_word in query:
                    t = t * 0
                    speak("Waking Up...")
                    os.system('cls')
                else:
                    t = t + 0

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