import keyboard
from PIL import ImageGrab
import time

def screeshot():
  curr_time = time.strftime("_%Y%m%D_%H:%M:%S")
  img = ImageGrab.grab()
  img.save("image{}.png".format(curr_time))

keyboard.add_hotkey("F9", screeshot)
# keyboard.add_hotkey("a", screeshot)
# keyboard.add_hotkey("ctrl+shift+a", screeshot)

keyboard.wait("esc") # 사용자가 esc를 누를 때까지 프로그램 수행