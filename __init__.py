try:
    import os
    os.system("cls")
    print("checking if dependencies are installed")
    env = "env\python.exe"
    os.system(f"{env} -m pip install bs4 datetime pipwin psutil pyautogui pyfiglet pypiwin32 requests speechRecognition wheel Wikipedia wolframalpha")
    os.system(f"{env} -m pip uninstall pyttsx")
    os.system(f"{env} -m pip install git+https://github.com/jpercent/pyttsx.git")
    os.system(f"{env} -m pipwin install pocketsphinx")
    os.system(f"{env} -m pipwin install Pyaudio")
    #Starting the app
    os.system(f"{env} Main.py")
except KeyboardInterrupt:
    import os
    os.system("cls")
    print("Assistant exited manually. Exiting JARVIS.")
    exit()
except Exception as error:
    import os
    os.system("cls")
    print("An error occured while running the code. Submitting the error to Github....")
    import token
    tok = token.token
    e = str(error)
    import requests
    import json
    headers = {"Authorization" : "token {}".format(tok)}
    data2 = {"title": "JARVIS Error Reporting System Reported An Error", "labels": ["Error"], "body": (e)}
    url = "https://api.github.com/repos/Hashah2311/JARVIS/issues"
    requests.post(url,data=json.dumps(data2),headers=headers)
    exit()