import os,subprocess,time,keyboard,pygame,sys
from enum import Enum

def play_audio():
    audio_folder = "C:\\Users\\Dell\\Desktop\\english.wav"
    pygame.mixer.init()
    sound = pygame.mixer.Sound(audio_folder)
    sound.play()
    pygame.time.delay(int(sound.get_length() * 800))

play_audio()



arabic = True
caps_lock = False
last_time_called = 0
end_signal = 'continue'



class configType(Enum):
    HotKey = 1
    ReMap = 2


class keyboardController:
    shortcut = []
    hooks = []
    # اضافة اختصار
    def add_shortcut_action(self, keys, action, type):
        self.shortcut.append((keys, action, type))

    def map_english_to_arabic(self, event_name):
        return self.arabic_to_english.get(event_name)

    # الغاء تفعيل اختصار معين
    def suppress_shortcut(self, keys):
        self.add_shortcut_action(keys, lambda: None, configType.HotKey)

    def compile(self):
        for keys, action, type in self.shortcut:
            if type == configType.HotKey:

                hook = keyboard.add_hotkey(keys, action, suppress=True)
                self.hooks.append(hook)
            elif type == configType.ReMap:
                keyboard.remap_key(keys, action)

    def unhook_shortcuts(self):
        for hook in self.hooks:
            try:
                keyboard.remove_hotkey(hook)
                self.hooks.remove(hook)
            except KeyError:
                print('hook error:', hook)

#VfFvVf
#VVfFvVfVfFvFvFvFv
sSSSSSSSWWW


def switch_lang(arabic_config, english_config):
    global arabic, last_time_called
    current_time = time.time()
    if(current_time - last_time_called < 0.3):
        return
    last_time_called = current_time
    if arabic:
        arabic = False
        keyboard.unhook_all_hotkeys()
        # play_sound('english')
        print(f"{arabic} english lang")
        english_config.compile()
    else:
        arabic = True
        keyboard.unhook_all_hotkeys()
        # play_sound('arabic')
        print(f"{arabic} arabic lang")
        arabic_config.compile()

def change_signal():
    global end_signal
    end_signal = 'end'

english_config = keyboardController()

# english shortcuts
# english_config.add_shortcut_action('f1', lambda: switch_lang(arabic_config, english_config), configType.HotKey)
english_config.suppress_shortcut('caps lock')
english_config.suppress_shortcut('shift + backslash')
english_config.suppress_shortcut('backslash')
english_config.add_shortcut_action('f8', lambda: print('end'), configType.HotKey)

english_config.compile()

keyboard.wait('f1', suppress=True)