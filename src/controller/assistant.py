import speech_recognition as sr

class Assistant:
    
    def __init__(self, lang="en"):
        self.lang = lang
        
    def listen(self, r, source):
        
        heard = "" 
        try:
            audio = r.listen(source)
            heard = r.recognize_google(audio)
        except sr.UnknownValueError:
            # print("Could not understand audio")
            pass
        except sr.RequestError as e:
            # print("Could not request results; {0}".format(e))
            pass

        return heard.lower()
    
    def speak(self,text):
        """
        Plays the message
         
        @param text (String): message to play as sound
        
        """
        pass