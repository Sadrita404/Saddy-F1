import pyautogui
import time
import random
import sys
from pynput import keyboard

# --- CONFIGURATION ---
STOP_KEY = keyboard.Key.esc  # Press 'Esc' to kill the script instantly
DURATION_MINUTES = 60
START_DELAY = 5
MIN_TYPE_SPEED = 0.02 
MAX_TYPE_SPEED = 0.08

SNIPPETS = [
    "def validate_connection(host, port):",
    "    if not host:\n        return False",
    "    print(f'Connecting to {host}:{port}...')",
    "    return True",
    "import time\nimport sys",
    "class WatcherTest:\n    def __init__(self):\n        self.active = True"
]

# Global flag to control the loop
running = True

def on_press(key):
    global running
    if key == STOP_KEY:
        print(f"\n[!] {STOP_KEY} pressed. Stopping script immediately...")
        running = False
        return False # Stops the listener

def simulate_typing():
    global running
    print(f"[*] Starting in {START_DELAY} seconds. Click into VS Code!")
    print(f"[*] TO STOP: Press the '{STOP_KEY}' key at any time.")
    
    # Start the keyboard listener in the background
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    
    time.sleep(START_DELAY)
    end_time = time.time() + (DURATION_MINUTES * 60)
    
    try:
        while running and time.time() < end_time:
            text_to_type = random.choice(SNIPPETS)
            
            # Typing Loop
            print(f"Typing... (Press Esc to Stop)")
            for char in text_to_type:
                if not running: break
                pyautogui.write(char, interval=random.uniform(MIN_TYPE_SPEED, MAX_TYPE_SPEED))
            
            if not running: break
            time.sleep(random.uniform(0.5, 1.5))
            
            # Deletion Loop
            delete_count = random.randint(5, len(text_to_type) + 5)
            print(f"Deleting {delete_count} chars...")
            for _ in range(delete_count):
                if not running: break
                pyautogui.press('backspace')
                time.sleep(0.01)
                
            time.sleep(0.5)
            
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("[*] Script terminated safely.")
        sys.exit()

if __name__ == "__main__":
    simulate_typing()