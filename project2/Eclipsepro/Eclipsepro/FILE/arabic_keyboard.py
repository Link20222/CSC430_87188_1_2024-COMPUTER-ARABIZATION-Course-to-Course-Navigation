import os,subprocess,time,keyboard,pygame,sys

print("Running python exe:", sys.executable)
print(os.environ.copy())
import keyboard
from enum import Enum

arabic = True
caps_lock = False
last_time_called = 0
end_signal = 'continue'

arabic_key_mapping = {
    'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه',
    'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د',
    'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن',
    'l': 'م', ';': 'ك', '\'': 'ط',
    'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ',': 'و',
    '.': 'ز', '/': 'ظ'
}

class configType(Enum):
    HotKey = 1
    ReMap = 2


class keyboardController:
    shortcut = []
    hooks = []

    def add_shortcut_action(self, keys, action, type):
        self.shortcut.append((keys, action, type))

    def map_english_to_arabic(self, event_name):
        return self.arabic_to_english.get(event_name)


    def suppress_shortcut(self, keys):
        self.add_shortcut_action(keys, lambda: None, configType.HotKey)

    def compile(self):
        for keys, action, type in self.shortcut:
            if type == configType.HotKey:

                hook = keyboard.add_hotkey(keys, action, suppress=True)
                self.hooks.append(hook)
            elif type == configType.ReMap:
                keyboard.remap_key(keys, action)


def toggle_caps_lock():
    global caps_lock
    caps_lock = not caps_lock
    print("Caps Lock is now", "on" if caps_lock else "off")


def arabic_caps(input):
    global caps_lock
    if not caps_lock:
        keyboard.write(english_to_arabic(input))
    else:
        keyboard.press_and_release('shift+' + input)


def english_to_arabic(english_char):
    global arabic_key_mapping
    return arabic_key_mapping.get(english_char)


def change_signal():
    global end_signal
    end_signal = 'end'

arabic_config = keyboardController()


# اختصارات عربية
arabic_config.add_shortcut_action('b', lambda: keyboard.write('ال'), configType.HotKey)
arabic_config.add_shortcut_action('shift+g', lambda: keyboard.write('أل'), configType.HotKey)
arabic_config.add_shortcut_action('shift+b', lambda: keyboard.write('آل'), configType.HotKey)
arabic_config.add_shortcut_action('shift+t', lambda: keyboard.write('إل'), configType.HotKey)
arabic_config.add_shortcut_action('caps lock', toggle_caps_lock, configType.HotKey)
arabic_config.suppress_shortcut('shift+backslash')
arabic_config.suppress_shortcut('backslash')
arabic_config.add_shortcut_action('f8', lambda: print('end'), configType.HotKey)


arabic_keys = [
    'a', 's', 'd', 'f', 'g', 'h',
    'j', 'k', 'l', 'm', 'n', 'q',
    'r', 't', 'w', 'x', 'c', 'v',
    'y', 'u', 'i', 'o', 'p', 'z'
]
for key in arabic_keys:
    arabic_config.add_shortcut_action(key, lambda key=key: arabic_caps(key), configType.HotKey)


arabic_config.compile()
keyboard.wait('f1', suppress=True)