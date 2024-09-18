from pynput import keyboard

def on_press(key):
    try:
        print(key.char.upper(), end=' ', flush=True)
    except AttributeError:
        print(f'{key} pressed', end=' ', flush=True)

def on_release(key):
    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
