import os
os.system("env\python.exe -m pip install speechRecognition datetime wikipedia pypiwin32 requests bs4 psutil pyautogui wheel wolframalpha")
whl = "env\python.exe -m pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl"
os.system(whl)
os.system("env\python.exe -m pip install git+https://github.com/jpercent/pyttsx.git")