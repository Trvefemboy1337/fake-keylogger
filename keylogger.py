from pynput import keyboard
from colorama import init, Fore, Style

init(autoreset=True)

def press_on_key(key):
    try:
        print(Fore.GREEN + Style.BRIGHT + f"Key: {key.char}")
    except AttributeError:
        print(Fore.YELLOW + Style.BRIGHT + f"Bold key {key}")

def release(key):
    print(Fore.RED + Style.BRIGHT + f"{key} released")

    if key == keyboard.Key.esc:
        return False

with keyboard.Listener(on_press=press_on_key, on_release=release) as listener:
    listener.join()


