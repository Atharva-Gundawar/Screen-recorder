
import pyautogui
import cv2
import numpy as np
import time

resolution = (1920, 1080)
codec = cv2.VideoWriter_fourcc(*"XVID")
filename = "name.avi"
fps = 15.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
# cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
# cv2.resizeWindow("Live", 480, 270)

start_time = time.time()
x = 1
counter = 0
while True:
    img = pyautogui.screenshot()
    # frame = np.array(img)
    # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # out.write(frame)
    out.write(cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
    # cv2.imshow('Live', frame)
    counter += 1
    if (time.time() - start_time) > x:
        # print("FPS: ", counter / (time.time() - start_time))
        fps = counter / (time.time() - start_time)
        counter = 0
        start_time = time.time()
    # if cv2.waitKey(1) == ord('q'):
    # 	break

out.release()
cv2.destroyAllWindows()
