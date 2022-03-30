import os
os.system("env\python.exe -m pip install bs4 datetime psutil pyautogui pyfiglet pypiwin32 requests speechRecognition wheel Wikipedia wolframalpha")
whl = "env\python.exe -m pip install PyAudio-0.2.11-cp310-cp310-win_amd64.whl"
os.system(whl)
os.system("env\python.exe -m pip uninstall pyttsx")
os.system("env\python.exe -m pip install git+https://github.com/jpercent/pyttsx.git")
