from gtts import gTTS
from io import BytesIO
import pygame
import time

def speak(text):
      mp3_fp=BytesIO()
      tts=gTTS(text,lang='en')
      tts.write_to_fp(mp3_fp)
      return mp3_fp

pygame.init()
pygame.mixer.init()
sound=speak("Hi I am the assistant made by Laghuvi")
sound.seek(0)
pygame.mixer.music.load(sound,"mp3")
pygame.mixer.music.play()
time.sleep(5)