import psutil
import os
from speak_f import *
check = "Teams.exe" in (i.name() for i in psutil.process_iter())
if check == "True":
    os.system("cd..")
    os.system("JARVIS_lib\python.exe mic\msTeams.py")
    speak("Unmuted your mic!")
else:
    cq = "CptHost.exe" in (i.name() for i in psutil.process_iter())
    if cq == "True":
        os.system("cd..")
        os.system("JARVIS_lib\python.exe mic\Zoom.py")
        speak("Unmuted your mic!")
    else:
        speak("Neither Teams nor zoom are running.Perhaps you have not joined the meeting?")