import os
import eel
from engine.features import *
from engine.command import *
#Playing Assistance Sound Function
def start():
    eel.init("www")
    playAssistantSound()
    eel.start('index.html')