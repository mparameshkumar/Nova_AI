import os
from playsound import playsound
import eel
from engine.command import speak
from engine.config import Assistant_Name
@eel.expose
def playAssistantSound():
    music_dir = "C:\\Nova\\www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

def openCommand(query):
    query = query.replace(Assistant_Name,"")
    query = query.replace("open","")
    query.lower()

    if query != "":
        speak("opening"+query)
        os.system('start'+query)
    else:
        speak("Not Found")