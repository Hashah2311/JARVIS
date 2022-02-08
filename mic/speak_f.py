import pyttsx
engine = pyttsx.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
def speak(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()