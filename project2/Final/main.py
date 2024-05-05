import os,subprocess,time,keyboard,pygame,sys
import pdb
#from moviepy.editor import *


def play_audio(file_name):
    audio_folder = "C:\\Users\\Dell\\Desktop\\Eclipsepro\\"
    file_path = audio_folder+"\\"+file_name+".wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(file_path)
    sound.play()
    pygame.time.delay(int(sound.get_length() * 800))

arabic = True
py_exe = r'C:\Users\Dell\Desktop\python.exe'
arabic_script = [py_exe, 'arabic_keyboard.py']
english_script = [py_exe, 'english_keyboard.py']

env = os.environ.copy()

running = True
while running:
    if arabic:
        play_audio("arabic")
        proc = subprocess.run(arabic_script, env=env)
        print(proc.stdout)
        arabic = not arabic
    else:
        pygame.mixer.init()
        play_audio("english")
        keyboard.press_and_release('alt+shift')
        proc = subprocess.run(english_script, env=env)
        print(proc.stdout)
        arabic = not arabic
# نص الخطا


