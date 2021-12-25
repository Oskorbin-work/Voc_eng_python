from pynput import keyboard
from clipboard import clipboard

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
        clipboard()


# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
