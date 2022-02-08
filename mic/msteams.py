import pyautogui
from speak_func import *
msteams = 'msTeams_mic.png'
try:
    buttonx, buttony = pyautogui.locateCenterOnScreen(msteams)
    pyautogui.click(buttonx, buttony)
    speak("Mic Unmuted")
except TypeError:
    speak("Cant find the button. You need to be in msTeams meeting window in full screen mode.")