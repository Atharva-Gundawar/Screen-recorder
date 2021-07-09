import numpy as np
import cv2
from mss import mss
from PIL import Image
import time


def record(name):
    with mss() as sct:
        mon = {'top': 0, 'left': 0, 'width': 1900, 'height': 880}

        name = name + '.mp4'
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        desired_fps = 30.0
        out = cv2.VideoWriter(name, fourcc, desired_fps,
                              (mon['width'], mon['height']))
        # last_time = 0
        start_time = time.time()
        x = 1
        counter = 0
        print("Recording ...")
        try:
            while True:
                img = sct.grab(mon)
                out.write(cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB))
                counter += 1
        except KeyboardInterrupt:
            print(counter/(time.time() - start_time))
            cv2.destroyAllWindows()


record("Video")
