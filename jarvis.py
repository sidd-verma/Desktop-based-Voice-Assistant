import pyttsx3
import speech_recognition as sr
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
from tkinter.filedialog import *
from PyDictionary import PyDictionary as dict
import datetime
from playsound import playsound
import requests
from bs4 import BeautifulSoup
from GoogleNews import GoogleNews
import subprocess as sub_p
from time import sleep
from google_trans_new import google_translator


googlenews = GoogleNews()

Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
print(voices)
Assistant.setProperty('voices', voices[0].id)
Assistant.setProperty('rate', 170)


def speak(audio):
    print("  ")
    Assistant.say(audio)
    print(f"Audio: {audio}")
    print(" ")
    Assistant.runAndWait()
    print(audio)


def takeCommand():

    command = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening...")
        command.pause_threshold = 1
        audio = command.listen(source, timeout=4, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = command.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query.lower()


def twit():
    speak("OK Sir.")
    webbrowser.open('https://twitter.com/home')
    speak('Done Sir.')


def whatsapp():
    speak("tell me the name of the person")
    name = takeCommand()

    if 'priyanka' in name:
        speak('tell me the message')
        msg = takeCommand()
        speak('Tell me the time sir')
        speak('Time in hour')
        hour = int(takeCommand())
        speak('Time in minutes')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+9454213881", msg, hour, min, 20)
        speak('Ok sir.Sending whatsapp message')

    elif 'subham' in name:
        speak('tell me the message')
        msg = takeCommand()
        speak('Tell me the time sir')
        speak('Time in hour')
        hour = int(takeCommand())
        speak('Time in minutes')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg("+9036637227", msg, hour, min, 20)
        speak('Ok sir.Sending whatsapp message')

    else:
        speak('tell me the phone number')
        phone = int(takeCommand())
        ph = "91" + phone
        speak('tell me the message')
        msg = takeCommand()
        speak('Tell me the time sir')
        speak('Time in hour')
        hour = int(takeCommand())
        speak('Time in minutes')
        min = int(takeCommand())
        pywhatkit.sendwhatmsg(ph, msg, hour, min, 20)
        speak('Ok sir.Sending whatsapp message')


def music():
    speak('Tell me the name  of the song')
    musicname = takeCommand()

    if 'Chalo Shiv Shankar Ke Mandir Mein' in musicname:
        os.startfile("D:\\music\\Chalo Shiv Shankar Ke Mandir Mein - Shiv Aaradhna 128 Kbps.mp3")
    else:
        pywhatkit.playonyt(musicname)

    speak('Your song has been started')


def youtube_automation():
    speak('whats your command')
    comm = takeCommand()

    if 'pause' in comm:
        keyboard.press('space bar')

    elif 'restart' in comm:
        keyboard.press('0')

    elif 'mute' in comm:
        keyboard.press('m')

    elif 'skip' in comm:
        keyboard.press('l')

    elif 'back' in comm:
        keyboard.press('j')

    elif 'full screen' in comm:
        keyboard.press('f')

    speak('done sir.')

def chrome_automation():
    speak('Chrome Automation started')
    comma = takeCommand()

    if 'close this tab' in comma:
        keyboard.press_and_release('ctrl+w')

    elif 'open new tab' in comma:
        keyboard.press_and_release('ctrl+t')
    
    elif 'open new window' in comma:
        keyboard.press_and_release('ctrl+n')

    elif 'history' in comma:
        keyboard.press_and_release('ctrl+h')

    speak("Done Sir.")

def Dict():
    speak('Activated Dictionary')
    speak('Tell me the problem')
    probl = takeCommand()

    if 'meaning' in probl:
        probl = probl.replace('what is the', "")
        probl = probl.replace('jarvis', "")
        probl = probl.replace('meaning of', "")
        result = dict.meaning(probl)
        speak(f'The Meaning for {probl} is {result}')

    elif 'synonym' in probl:
        probl = probl.replace('what is the', "")
        probl = probl.replace('jarvis', "")
        probl = probl.replace('synonym of', "")
        result = dict.synonym(probl)
        speak(f'The Synonym for {probl} is {result}')

    elif 'antonym' in probl:
        probl = probl.replace('what is the', "")
        probl = probl.replace('jarvis', "")
        probl = probl.replace('synonym of', "")
        result = dict.antonym(probl)
        speak(f'The antonym for {probl} is {result}')

    speak('Exited Dictionary.')


def temp():
    search = 'Temperature in Lucknow'
    url = f'https://www.google.com/search?q={search}'
    r = requests.get(url)
    data = BeautifulSoup(r.text, 'html.parser')
    temperature = data.find('div', class_='BNeawe').text
    speak(f'The Temperature is {temperature}')


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour == 12:
        speak("Good Noon!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak('Hello Sir.')
    speak('I Am Your Personal AI Assistant')
    speak('How may I help you?')


def news():
    Assistant.say('Getting news for you')
    Assistant.runAndWait()
    googlenews.get_news('Today news')
    googlenews.result()
    a = googlenews.get_texts()
    print(*a, sep='\n')


def alarm():
    speak('Enter the time:')
    time = input(': Enter the time :')

    while True:
        tc = datetime.datetime.now()
        now = tc.strftime('%H:%M:%S')

        if now == time:
            speak('Time to wake up sir.')
            playsound('Alarm-Windows-10.mp3', block=True)
            speak('Alarm Closed!')

        elif now > time:
            break


def yts(query):
    speak("OK Sir. This is what I found for your search")
    query = query.replace("jarvis", "")
    query = query.replace("youtube search", "")
    web = 'https://www.youtube.com/results?search_query=' + query
    webbrowser.open(web)
    speak('Done Sir.')


def gs(query):
    speak("OK Sir. This is what I found for your search")
    query = query.replace("jarvis", "")
    query = query.replace("google search", "")
    pywhatkit.search(query)
    speak('Done Sir.')


def wikip(query):
    speak("Searching Wikipedia.......")
    query = query.replace("jarvis", "")
    query = query.replace("wikipedia", "")
    wiki = wikipedia.summary(query, 2)
    speak(f'According to wikipedia : {wiki}')


def webs(query):
    speak("OK Sir. Launching")
    query = query.replace("jarvis", "")
    query = query.replace("website", "")
    query = query.replace(" ", "")
    web1 = query.replace('open', '')
    web2 = 'https://www.' + web1 + '.com'
    webbrowser.open(web2)
    speak('Launched Sir.')


def ipa():
    speak('OK Sir.')
    ip = requests.get('https://api.ipify.org').text
    speak(f"Your IP Address is {ip}")
    speak('Done Sir.')


def tm():
    speak('OK Sir.')
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"Sir, the time is {strTime}")
    speak('Done Sir.')


def ss():
    kk = pyautogui.screenshot()
    sp = asksaveasfilename()
    kk.save(sp+'_screenshot.png')


def mic_ed():
    speak('OK Sir.')
    webbrowser.open("microsoftedge.com")
    speak('Done Sir.')


def so():
    speak('OK Sir.')
    webbrowser.open("https://stackoverflow.com")
    speak('Done Sir.')


def cp():
    speak('OK Sir.')
    os.system('start cmd')
    speak('Done Sir.')


def cm():
    speak('OK Sir.')
    sub_p.run("start microsoft.windows.camera:", shell=True)
    speak('Done Sir.')


def cal():
    speak('OK Sir.')
    sub_p.Popen("C:\\Windows\\System32\\calc.exe")
    speak('Done Sir.')


def img():
    speak('OK Sir.')
    os.startfile("C:\\Users\\siddharth verma\\Pictures\\Screenshots")
    speak('Done Sir.')


def np():
    speak('OK Sir.')
    os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
    speak('Done Sir.')


def msw():
    speak('OK Sir.')
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE")
    speak('Done Sir.')


def mse():
    speak('OK Sir.')
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE")
    speak('Done Sir.')


def msp():
    speak('OK Sir.')
    os.startfile("C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE")
    speak('Done Sir.')


def tc():
    speak('OK Sir.')
    os.startfile("C:\\TurboC++\\TC_DOS.exe")
    speak('Done Sir.')


def fb():
    speak("OK Sir.")
    webbrowser.open('https://www.facebook.com')
    speak('Done Sir.')


def ama():
    speak("OK Sir.")
    webbrowser.open('https://www.amazon.in')
    speak('Done Sir.')


def myn():
    speak("OK Sir.")
    webbrowser.open('https://www.myntra.com')
    speak('Done Sir.')


def ft():
    speak("OK Sir.")
    webbrowser.open('https://www.flipkart.com')
    speak('Done Sir.')

def openapps(query):
    speak('Ok sir. Wait a second.')

    if 'code' in query:
        os.startfile('C:\\Users\\siddharth verma\\AppData\\Local\\Programs\\Microsoft VS Code')

    elif 'chrome' in query:
        os.startfile('"C:\\Program Files\\Google\Chrome\\Application\\chrome.exe"')

    elif 'instagram' in query:
        webbrowser.open('https://www.instagram.com/')

    elif 'facebook' in query:
        webbrowser.open('https://www.facebook.com/')

    elif 'maps' in query:
        webbrowser.open('https://www.google.co.in/maps/place/BANSAL+INSTITUTE+OF+ENGINEERING+AND+TECHNOLOGY/@26.9423459,80.9245913,17z/data=!4m12!1m6!3m5!1s0x399957e00ca6992d:0x3e09558f651ae573!2sBANSAL+INSTITUTE+OF+ENGINEERING+AND+TECHNOLOGY!8m2!3d26.9423459!4d80.92678!3m4!1s0x399957e00ca6992d:0x3e09558f651ae573!8m2!3d26.9423459!4d80.92678?hl=en')

    speak('Your command has been successfully completed.')

def closeapps(query):
    speak('Ok sir. Wait a second.')

    if 'code' in query:
        os.system("taskkill /IM code.exe")

    elif 'chrome' in query:
        os.system("taskkill /IM chrome.exe")

    elif 'instagram' in query:
        os.system("taskkill /IM msedge.exe")

    elif 'facebook' in query:
        os.system("taskkill /IM msedge.exe")

    elif 'maps' in query:
        os.system("taskkill /IM msedge.exe")

    speak('Your command has been successfully completed.')


def taskexe():
    while True:
        query = takeCommand()

        if 'hello' in query:
            wishme()

        elif 'how are you' in query:
            speak('I am fine sir!')
            speak('Whats about you')

        elif 'you need a break' in query:
            speak('Ok sir. you can call me anytime.')
            break

        elif 'bye' in query:
            speak('Ok Sir. Bye.')
            break

        elif 'youtube search' in query:
            yts(query)

        elif 'google search' in query:
            gs(query)

        elif 'website' in query:
            webs(query)

        elif 'facebook' in query:
            fb()

        elif 'amazon' in query:
            ama()

        elif 'myntra' in query:
            myn()

        elif 'flipkart' in query:
            ft()

        elif 'twitter' in query:
            twit()

        elif 'music' in query:
            music()

        elif 'wikipedia' in query:
            wikip(query)

        elif 'whatsapp message' in query:
            whatsapp()

        elif 'screenshot' in query:
            ss()

        elif 'open facebook' in query:
            openapps(query)

        elif 'open instagram' in query:
            openapps(query)

        elif 'open code' in query:
            openapps(query)

        elif 'open maps' in query:
            openapps(query)

        elif 'open chrome' in query:
            openapps(query)
        
        elif 'close chrome' in query:
            closeapps(query)

        elif 'close code' in query:
            closeapps(query)

        elif 'close instagram' in query:
            closeapps(query)

        elif 'close facebook' in query:
            closeapps(query)

        elif 'close maps' in query:
            closeapps(query)
        
        elif 'pause' in query:
            keyboard.press('space bar')

        elif 'restart' in query:
            keyboard.press('0')

        elif 'mute' in query:
            keyboard.press('m')

        elif 'skip' in query:
            keyboard.press('l')

        elif 'back' in query:
            keyboard.press('j')

        elif 'full screen' in query:
            keyboard.press('f')

        elif 'youtube tools' in query:
            youtube_automation()

        elif 'joke' in query:
            get = pyjokes.get_joke()
            speak(get)

        elif 'dictionary' in query:
            Dict()

        elif 'alarm' in query:
            alarm()

        elif 'temperature' in query:
            temp()

        elif 'headlines' in query:
            news()

        elif 'microsoft edge' in query:
            mic_ed()

        elif 'notepad' in query:
            np()

        elif 'microsoft word' in query:
            msw()

        elif 'microsoft excel' in query:
            mse()

        elif 'microsoft powerpoint' in query:
            msp()

        elif 'turbo c' in query:
            tc()

        elif 'images' in query:
            img()

        elif 'calculator' in query:
            cal()

        elif 'camera' in query:
            cm()

        elif 'command prompt' in query:
            cp()

        elif 'stack overflow' in query:
            so()

        elif 'ip address' in query:
            ipa()

        elif 'the time' in query:
            tm()
        
        elif 'close this tab' in query:
            keyboard.press_and_release('ctrl+w')

        elif 'open new tab' in query:
            keyboard.press_and_release('ctrl+t')
    
        elif 'open new window' in query:
            keyboard.press_and_release('ctrl+n')

        elif 'history' in query:
            keyboard.press_and_release('ctrl+h')

        elif 'chrome automation' in query:
            chrome_automation()

        elif 'repeat my words' in query:
            speak('Speak sir!')
            jj=takeCommand()
            speak(f"You Said : {jj}")


        elif 'my location' in query:
            speak("Ok sir. Wait a second")
            webbrowser.open('https://www.google.co.in/maps/place/The+Residency,+Lucknow/@26.8611692,80.9293587,16.65z/data=!4m13!1m7!3m6!1s0x399bfd991f32b16b:0x93ccba8909978be7!2sLucknow,+Uttar+Pradesh!3b1!8m2!3d26.8467406!4d80.9458923!3m4!1s0x399bfd95d4ec4999:0x58b425c3fb30dcca!8m2!3d26.8606372!4d80.9267863')

        

taskexe()