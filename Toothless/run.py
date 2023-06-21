from PyQt5 import QtWidgets, QtGui,QtCore
from PyQt5.QtGui import QMovie
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
import pyttsx3
import speech_recognition as sr
import os
import time
import webbrowser
import datetime
import operator
import requests
import wikipedia
import random
import cv2
import pywhatkit as kit
import sys
import pyautogui
from tkinter import *
import wolframalpha
from ecapture import ecapture as ec
import openai
import openai_secret_manager

flags = QtCore.Qt.WindowFlags(QtCore.Qt.FramelessWindowHint)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
   hour = int(datetime.datetime.now().hour)
   if hour>=0 and hour <12:
        speak("Good morning")

   elif hour>=12 and hour<18:
        speak("Good Afternoon")
   
   else:
        speak("Good night")


    

class mainT(QThread):
  def __init__(self):
        super(mainT,self).__init__()
    
  def run(self):
    self.JARVIS()
    
  def STT(self):
        R = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listning...........")
            audio = R.listen(source)
        try:
            print("Recog......")
            text = R.recognize_google(audio,language='en-in')
            print(">> ",text)
        except Exception:
            speak("Sorry Speak Again")
            return "None"
        text = text.lower()
        return text
  def ask_gpt(prompt):
    os.environ['org-UqzhVmcranYL4qXUUhQKxbza'] = 'org-UqzhVmcranYL4qXUUhQKxbza' 
    os.environ['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'] = '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'
    openai.organization = os.environ['org-UqzhVmcranYL4qXUUhQKxbza']
    openai.api_key = os.environ['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']
    openai.Model.list()
    response = openai.Completion.create(
        engine="davinci", # use the most powerful GPT-3 engine
        prompt=prompt,
        max_tokens=60, # set the maximum number of tokens to generate
        n=1, # set the number of responses to generate
        stop=None, # set the stopping sequence
        temperature=0.7 # set the creativity of the responses
    )
    message = response.choices[0].text.strip()
    return message
  
  def JARVIS(self):
        wish()
        while True:
            self.query = self.STT()
            if 'good bye' in self.query:
                sys.exit()
            
            elif 'open youtube' in self.query:
             speak("what you will like to watch ?")
             query = self.STT().lower()
             kit.playonyt(f"{query}")
            elif 'play music' in self.query:
                speak("playing music from pc")
                self.music_dir =(r"C:\Users\moham\Music")
                self.musics = os.listdir(self.music_dir)
                os.startfile(os.path.join(self.music_dir,self.musics[0]))
            
            elif 'open chat' in self.query:
                response = ask_gpt(prompt=self.query)
                speak(response)
            
          
            elif 'close chrome' in self.query:
             os.system("taskkill /f /im chrome.exe")
          
            elif 'close youtube' in self.query:
             os.system("taskkill /f /im msedge.exe")
          
            elif 'open google' in self.query:
             speak("what should I search ?")
             query = self.STT().lower()
             webbrowser.open(f"{query}")
             results = wikipedia.summary(query, sentences=2)
             speak(results)
          
            elif 'close google' in self.query:
             os.system("taskkill /f /im msedge.exe")
          
            elif 'play music' in self.query:
             music_dir = (r"C:\Users\moham\Music")
             songs = os.listdir(music_dir) 
             os.startfile(os.path.join(music_dir, random.choice(songs)))
          
            elif 'close movie' in self.query:
             os.system("taskkill /f /im vlc.exe")
          
            elif 'close music' in self.query:
             os.system("taskkill /f /im vlc.exe")
          
            elif 'the time' in self.query:
             strTime = datetime.datetime.now().strftime("%H:%M:%S") 
             speak(f"Sir, the time is {strTime}")
          
            elif "shut down the system" in self.query:
             os.system("shutdown /s /t 5")
          
            elif "restart the system" in self.query:
             os.system("shutdown /r /t 5")
          
            elif "Lock the system" in self.query:
             os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
             
            elif "open notepad" in self.query:
             npath = "C:\WINDOWS\system32\\notepad.exe" 
             os.startfile(npath)
             
            elif "close notepad" in self.query:
             os.system("taskkill /f /im notepad.exe")
          
            elif "open command prompt" in self.query:
             os.system("start cmd")
          
            elif "close command prompt" in self.query:
             os.system("taskkill /f /im cmd.exe")
          
            elif "open camera" in self.query:
             cap = cv2.VideoCapture(0)
             while True:
                 ret, img = cap.read()
                 cv2.imshow('webcam', img)
                 k = cv2.waitKey(50)
                 if k==27:
                     break;
             cap.release()
             cv2.destroyAllWndows()
            
            elif"take photo"in self.query or "snap" in self.query or "photo" in self.query:
              ec.capture(0,"robo camera","img.jpg")
          
            elif "go to sleep" in self.query:
             speak(' alright then, I am switching off')
             sys.exit()
          
            elif "take screenshot" in self.query or "screenshot" in self.query:
              speak('tell me a name for the file')
              name = self.STT().lower()
              time.sleep(3)
              img = pyautogui.screenshot() 
              img.save(f"{name}.png") 
              speak("screenshot saved")
              print("screenshot saved")
          
            elif "calculate" in self.query:
              r = sr.Recognizer()
              with sr.Microphone() as source:
                  speak("ready")
                  print("Listning...")
                  r.adjust_for_ambient_noise(source)
                  audio = r.listen(source)
              my_string=r.recognize_google(audio)
              print(my_string)
          
              def get_operator_fn(op):
                  return {
                  '+' : operator.add,
                  '-' : operator.sub,
                  'x' : operator.mul,
                  'divided' : operator.__truediv__,
                  }[op]
             
              def eval_bianary_expr(op1,oper, op2):
                  op1,op2 = int(op1), int(op2)
                  return get_operator_fn(oper)(op1, op2)
              speak("your result is")
              speak(eval_bianary_expr(*(my_string.split())))
          
            elif "what is my ip address" in self.query:
              speak("Checking")
              print("checking")
              try:
               ipAdd = requests.get('https://api.ipify.org').text
               print(ipAdd)
               speak("your ip adress is")
               speak(ipAdd)
              except Exception as e:
               speak("network is weak, please try again some time later")
          
            elif "volume up" in self.query:
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
              pyautogui.press("volumeup")
          
            elif "volume down" in self.query:
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
              pyautogui.press("volumedown")
          
            elif "mute" in self.query:
              pyautogui.press("volumemute")
          
            elif "refresh" in self.query:
              pyautogui.moveTo(1551,551, 2)
              pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
              pyautogui.moveTo(1620,667, 1)
              pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
          
            elif "scroll down" in self.query:
              pyautogui.scroll(1000)
          
            elif "drag visual studio to the right" in self.query:
              pyautogui.moveTo(46, 31, 2)
              pyautogui.dragRel(1857, 31, 2)
          
            elif "rectangular spiral" in self.query:
              pyautogui.hotkey('win')
              time.sleep(1)
              pyautogui.write('paint')
              time.sleep(1)
              pyautogui.press('enter')
              pyautogui.moveTo(100, 193, 1)
              pyautogui.rightClick
              pyautogui.click()
              distance = 300
          
              while distance > 0:
                  pyautogui.dragRel(distance, 0, 0.1, button="left")
                  distance = distance - 10
                  pyautogui.dragRel(0, distance, 0.1, button="left")
                  pyautogui.dragRel(-distance, 0, 0.1, button="left")
                  distance = distance - 10
                  pyautogui.dragRel(0, -distance, 0.1, button="left")
          
            elif "close paint" in self.query:
             os.system("taskkill /f /im mspaint.exe")
            
            elif "who are you" in self.query:
              print('My Name Is Toothless')
              speak('My Name Is Toothless')
              print('I can Do Everything that my creator programmed me to do')
              speak('I can Do Everything that my creator programmed me to do')
          
            elif "who created you" in self.query:
              print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
              speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
            elif "open notepad and write my name" in self.query:
              pyautogui.hotkey('win')
              time.sleep(1)
              pyautogui.write('notepad')
              time.sleep(1)
              pyautogui.press('enter')
              time.sleep(1)
              pyautogui.write("Washif", interval = 0.1)
            elif "say hello" in self.query:
              print("hello")
              speak("hello")
          
            elif 'type' in self.query: #10
              self.query = self.query.replace("type", "")
              pyautogui.write(f"{self.query}")
          
            elif 'open chrome' in self.query:
              os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe')

            elif 'maximize this window' in self.query:
             pyautogui.hotkey('alt', 'space')
             time.sleep(1)
             pyautogui.press('x')

            elif 'google search' in self.query:
             self.query = self.query.replace("google search", "")
             pyautogui.hotkey('alt', 'd')
             pyautogui.write(f"{self.query}", 0.1)
             pyautogui.press('enter')

            elif 'youtube search' in self.query:
             self.query = self.query.replace("youtube search", "")
             pyautogui.hotkey('alt', 'd')
             time.sleep(1)
             pyautogui.press('tab')
             pyautogui.press('tab')
             pyautogui.press('tab')
             pyautogui.press('tab')
             time.sleep(1)
             pyautogui.write(f"{self.query}", 0.1)
             pyautogui.press('enter')

            elif 'open new window' in self.query:
             pyautogui.hotkey('ctrl', 'n')

            elif 'open incognito window' in self.query:
             pyautogui.hotkey('ctrl', 'shift', 'n')

            elif 'minimise this window' in self.query:
             pyautogui.hotkey('alt', 'space')
             time.sleep(1)
             pyautogui.press('n')

            elif 'open history' in self.query:
             pyautogui.hotkey('ctrl', 'h')

            elif 'open downloads' in self.query:
             pyautogui.hotkey('ctrl', 'j')

            elif 'previous tab' in self.query:
             pyautogui.hotkey('ctrl', 'shift', 'tab')
            
            elif 'next tab' in self.query:
             pyautogui.hotkey('ctrl', 'tab')

            elif 'close tab' in self.query:
             pyautogui.hotkey('ctrl', 'w')

            elif 'close window' in self.query:
             pyautogui.hotkey('ctrl', 'shift', 'w')

            elif 'clear browsing history' in self.query:
             pyautogui.hotkey('ctrl', 'shift', 'delete')

            elif 'close chrome' in self.query:
             os.system("taskkill /f /im chrome.exe")

            elif 'search' in self.query:
             speak('I can answer to computational and geographical questions and what question do you want to ask now')
             question=self.STT()
             app_id="R2K75H-7ELALHR35X"
             client = wolframalpha.Client('R2K75H-7ELALHR35X')
             res = client.query(question)
             answer = next(res.results).text
             speak(answer)
             print(answer)

            elif 'wikipedia' in self.query:
             speak('Searching Wikipedia...')
             query =self.STT().replace("wikipedia", "")
             results = wikipedia.summary(query, sentences=3)
             speak("According to Wikipedia")
             print(results)
             speak(results)


            elif 'open gmail' in self.query:
                webbrowser.open_new_tab("gmail.com")
                speak("Google Mail open now")
                time.sleep(5)

            elif "weather" in self.query:
                api_key="8ef61edcf1c576d65d836254e11ea420"
                base_url="https://api.openweathermap.org/data/2.5/weather?"
                speak("whats the city name")
                print("whats the city name")
                city_name=self.STT()
                complete_url=base_url+"appid="+api_key+"&q="+city_name
                response = requests.get(complete_url)
                x=response.json()
                if x["cod"]!="404":
                    y=x["main"]
                    current_temperature = y["temp"]
                    current_humidiy = y["humidity"]
                    z = x["weather"]
                    weather_description = z[0]["description"]
                    speak(" Temperature in kelvin unit is " +
                          str(current_temperature) +
                          "\n humidity in percentage is " +
                          str(current_humidiy) +
                          "\n description  " +
                          str(weather_description))
                    print(" Temperature in kelvin unit = " +
                          str(current_temperature) +
                          "\n humidity (in percentage) = " +
                          str(current_humidiy) +
                          "\n description = " +
                          str(weather_description))
                else:
                    speak(" City Not Found ")
            
            

FROM_MAIN,_ = loadUiType(os.path.join(os.path.dirname(__file__),"./scifi.ui"))

class Main(QMainWindow,FROM_MAIN):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        self.setupUi(self)
        self.setFixedSize(1920,1080)
        self.label_7 = QLabel
        self.exitB.setStyleSheet("background-image:url(./lib/exit - Copy.png);\n""border:none;")
        self.exitB.clicked.connect(self.close)
        self.setWindowFlags(flags)
        Dspeak = mainT()
        self.label_7 = QMovie("./lib/gifloader.gif", QByteArray(), self)
        self.label_7.setCacheMode(QMovie.CacheAll)
        self.label_4.setMovie(self.label_7)
        self.label_7.start()

        self.ts = time.strftime("%A, %d %B")

        Dspeak.start()
        self.label.setPixmap(QPixmap("./lib/tuse.png"))
        self.label_5.setText("<font size=8 color='white'>"+self.ts+"</font>")
        self.label_5.setFont(QFont(QFont('Acens',8)))


app = QtWidgets.QApplication(sys.argv)
main = Main()
main.show()
exit(app.exec_())
