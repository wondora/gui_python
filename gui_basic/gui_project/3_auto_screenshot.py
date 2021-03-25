import time
from PIL import ImageGrab

time.sleep(5) # 5초 대기

for i in range(1, 11):
  img = ImageGrab.grab() # 현재 스크린 이미지 가져오는것 
  img.save("image{}.png".format(i))
  time.sleep(2)
