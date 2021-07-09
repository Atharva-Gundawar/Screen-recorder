import time
import cv2
import mss
import numpy
import pyautogui 
import numpy as np

# resolution = (1920, 1080) 
# codec = cv2.VideoWriter_fourcc(*"XVID") 
# filename = "name.avi"
# fps = 10.0
# out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480*2, 540*2)

with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {'top': 0, 'left': 0, 'width': 960 , 'height': 1080}

    while 'Screen capturing':
        last_time = time.time()
        img = numpy.array(sct.grab(monitor))
        # img = cv2.GaussianBlur(img,(5,5),cv2.BORDER_DEFAULT)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)
        # out.write(img)
        img_hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        # lower_red = np.array([138,93,18]) #example value
        # upper_red = np.array([145,97,23]) #example value
        # lower_blue = np.array([110,50,50])
        # upper_blue = np.array([130,255,255])
        # mask = cv2.inRange(img_hsv, upper_blue,lower_blue)
        lower_red = np.array([100,0,0]) 
        upper_red = np.array([200,255,100]) 
        mask = cv2.inRange(img_hsv, lower_red, upper_red)
        res = cv2.bitwise_and(img,img, mask= mask) 
        dest_not1 = cv2.bitwise_not(res, mask = mask) 
        # cv2.imshow('frame',res) 
        cv2.imshow('mask',mask) 
        # cv2.imshow('dest_not1',dest_not1)
        # cv2.imshow('res',res) 
        # cv2.imshow("Live", img)
        # img_result = cv2.bitwise_not(img, img, mask=mask)
        # cv2.imshow("mask",img_result)
        print('fps: {0}'.format(1 / (time.time()-last_time)))

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break
# out.release()