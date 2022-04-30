import speech_recognition as sr
import settings as s
from helper.actions import process,load_data
from controller.assistant import Assistant

class Main:
    
    def start(self):
        load_data(s.commands)
        r = sr.Recognizer()
        assistant = Assistant()
        
        with sr.Microphone() as source:
            
            print(f"Hi. Call me '{s.greeting}', if you need help.")
            print("Calibrating Noise Level...")
            r.adjust_for_ambient_noise(source,duration=1)

            while True:
                
                heard = assistant.listen(r,source)
                
                if heard and heard.count(s.greeting)>0:
                    print("Listening...")
                    assistant.speak("Listening")
                    heard = assistant.listen(r,source)
                    print('Heard:',heard)
                    if heard:
                        process(heard)
                    