from cgitb import text
from email.mime import audio
import pyttsx3
import speech_recognition as sr
import re
from speak_and_listen import hear_me, speak
def recognize_voice(r):
   with sr.Microphone() as source:
      print("Puedes hablar")
      audio = r.listen(source)
      text  = r.recognize_google(audio, language="es-ES")
   return


def iniciar_engine():
   engine = pyttsx3.init()
   engine.setProperty("voice", "spanish")



def indentify_name(text):
   name =None 
   patterns = ["me llamo ([A-Za-z]+)", "mi nombre es ([A-Za-z]+)"]
   for pattern in patterns:
      try:
         name = re.findall(patterns, text)
      except IndexError:
         print("Este tio no tiene nombre")
      return name
   
def main():
   speak("Hola, como te llamas")
   text = hear_me()
   name = indentify_name(text)
   if name:
        speak("Encantado de conocerte, {}".format(name[0]))
   else:
        speak("La verdad que no te entiendo deja ya de comer pollas")
      
if __name__ == "__main__":
   main()