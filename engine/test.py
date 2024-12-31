import pvporcupine
import pyautogui as autogui
import pyaudio
import struct
import time
import numpy as np

def hotword():
    porcupine = None
    paud = None
    audio_stream = None
    try:
        # Use valid keywords
        porcupine = pvporcupine.create(keywords=["alexa", "porcupine"])
        paud = pyaudio.PyAudio()
        audio_stream = paud.open(rate=porcupine.sample_rate, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=porcupine.frame_length)
        
        # Loop for streaming
        while True:
            keyword = audio_stream.read(porcupine.frame_length)
            keyword = struct.unpack_from("h" * porcupine.frame_length, keyword)
            keyword = np.array(keyword, dtype=np.int16)

            # Processing keyword comes from mic 
            keyword_index = porcupine.process(keyword)

            # Checking if keyword is detected
            if keyword_index >= 0:
                print("Hotword detected")

                # Pressing shortcut key win+j
                autogui.keyDown("win")
                autogui.press("j")
                time.sleep(2)
                autogui.keyUp("win")
                
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()

hotword()