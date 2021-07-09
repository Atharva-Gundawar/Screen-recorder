import numpy as np
from PIL import ImageGrab
import cv2
import time

start_time = time.time()
x = 1 
counter = 0

while(True):
    printscreen_pil =  ImageGrab.grab()
    printscreen_numpy =   np.array(printscreen_pil,dtype='uint8')\
    .reshape((printscreen_pil.size[1],printscreen_pil.size[0],3)) 
    # cv2.imshow('window',printscreen_numpy)
    counter+=1
    if (time.time() - start_time) > x :
        print("FPS: ", counter / (time.time() - start_time))
        counter = 0
        start_time = time.time()
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break