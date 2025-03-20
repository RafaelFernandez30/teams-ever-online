import pyautogui # type: ignore
import time
from datetime import datetime

def move_mouse():
    while True:
   
        x, y = pyautogui.position()
        #Tudo posso!
        pyautogui.moveTo(x + 330, y, duration=0.5)
        
        pyautogui.moveTo(x, y, duration=0.5)

        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Mouse movido! ({current_time})")
        
        time.sleep(300)

if __name__ == "__main__":
    move_mouse()
