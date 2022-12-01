import speech_recognition
import os
from gtts import gTTS


mytext = "Hello! How can i help you?"
audio = gTTS(text=mytext, lang="en", slow=False)

audio.save("hello.mp3")
