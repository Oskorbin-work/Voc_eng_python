from pynput import keyboard

from pandas.io.clipboard import clipboard_get

def on_press(key):
    try:
        pass
    except AttributeError:
        pass

def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False
    if key == keyboard.Key.cmd:
        text = clipboard_get()
        if text != '':
            print(text)

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()