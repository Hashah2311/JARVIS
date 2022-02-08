import pyautogui
from speak_f import *
zoom = 'Zoom_mic.png'
try:
    buttonx, buttony = pyautogui.locateCenterOnScreen(zoom)
    pyautogui.click(buttonx, buttony)
    speak("Mic Unmuted")
except TypeError:
    speak("Cant find the button. You need to be in zoom meeting window in full screen mode.")