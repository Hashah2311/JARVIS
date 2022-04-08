import os
env = "env\python.exe"
os.system(f"{env} -m pip install bs4 datetime pipwin psutil pyautogui pyfiglet pypiwin32 requests speechRecognition wheel Wikipedia wolframalpha")
os.system(f"{env} -m pip uninstall pyttsx pyaudio")
os.system(f"{env} -m pip install git+https://github.com/jpercent/pyttsx.git")
os.system(f"{env} -m pipwin install pocketsphinx Pyaudio")