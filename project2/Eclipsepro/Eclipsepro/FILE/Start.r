Start

    # Import necessary modules
    Import os, subprocess, time, keyboard, pygame, sys

    # Print the running Python executable and environment variables
    Print("Running python exe:", sys.executable)
    Print(os.environ.copy())

    # Import keyboard module and Enum class
    Import keyboard
    From enum import Enum

    # Global variables initialization
    arabic = True
    caps_lock = False
    last_time_called = 0
    end_signal = 'continue'

    # Define Arabic to English key mapping dictionary
    arabic_key_mapping = {
        'q': 'ض', 'w': 'ص', 'e': 'ث', 'r': 'ق', 't': 'ف', 'y': 'غ', 'u': 'ع', 'i': 'ه',
        'o': 'خ', 'p': 'ح', '[': 'ج', ']': 'د',
        'a': 'ش', 's': 'س', 'd': 'ي', 'f': 'ب', 'g': 'ل', 'h': 'ا', 'j': 'ت', 'k': 'ن',
        'l': 'م', ';': 'ك', '\'': 'ط',
        'z': 'ئ', 'x': 'ء', 'c': 'ؤ', 'v': 'ر', 'b': 'لا', 'n': 'ى', 'm': 'ة', ',': 'و',
        '.': 'ز', '/': 'ظ'
    }

    # Define an Enum for configuration type
    class configType(Enum):
        HotKey = 1
        ReMap = 2

    # Define a keyboard controller class
    class keyboardController:
        shortcut = []
        hooks = []

        # Function to add shortcut action
        def add_shortcut_action(self, keys, action, type):
            self.shortcut.append((keys, action, type))

        # Function to map English to Arabic characters
        def map_english_to_arabic(self, event_name):
            return self.arabic_to_english.get(event_name)

        # Function to suppress a specific shortcut
        def suppress_shortcut(self, keys):
            self.add_shortcut_action(keys, lambda: None, configType.HotKey)

        # Function to compile shortcuts
        def compile(self):
            for keys, action, type in self.shortcut:
                if type == configType.HotKey:
                    hook = keyboard.add_hotkey(keys, action, suppress=True)
                    self.hooks.append(hook)
                elif type == configType.ReMap:
                    keyboard.remap_key(keys, action)

    # Function to toggle Caps Lock
    def toggle_caps_lock():
        global caps_lock
        caps_lock = not caps_lock
        print("Caps Lock is now", "on" if caps_lock else "off")

    # Function to handle Arabic typing
    def arabic_caps(input):
        global caps_lock
        if not caps_lock:
            keyboard.write(english_to_arabic(input))
        else:
            keyboard.press_and_release('shift+' + input)

    # Function to convert English to Arabic characters
    def english_to_arabic(english_char):
        global arabic_key_mapping
        return arabic_key_mapping.get(english_char)

    # Function to change signal
    def change_signal():
        global end_signal
        end_signal = 'end'

    # Create an instance of keyboard controller for Arabic configuration
    arabic_config = keyboardController()

    # Define Arabic shortcuts
    arabic_config.add_shortcut_action('b', lambda: keyboard.write('ال'), configType.HotKey)
    arabic_config.add_shortcut_action('shift+g', lambda: keyboard.write('أل'), configType.HotKey)
    arabic_config.add_shortcut_action('shift+b', lambda: keyboard.write('آل'), configType.HotKey)
    arabic_config.add_shortcut_action('shift+t', lambda: keyboard.write('إل'), configType.HotKey)
    arabic_config.add_shortcut_action('caps lock', toggle_caps_lock, configType.HotKey)
    arabic_config.suppress_shortcut('shift+backslash')
    arabic_config.suppress_shortcut('backslash')
    arabic_config.add_shortcut_action('f8', lambda: print('end'), configType.HotKey)

    # Define Arabic keys
    arabic_keys = [
        'a', 's', 'd', 'f', 'g', 'h',
        'j', 'k', 'l', 'm', 'n', 'q',
        'r', 't', 'w', 'x', 'c', 'v',
        'y', 'u', 'i', 'o', 'p', 'z'
    ]
    for key in arabic_keys:
        arabic_config.add_shortcut_action(key, lambda key=key: arabic_caps(key), configType.HotKey)

    # Compile Arabic configuration
    arabic_config.compile()

    # Wait for F1 key press to start
    keyboard.wait('f1', suppress=True)

End
