import cv2
from PIL import Image
import numpy as np
import imgC
import matchImg
import threading

cam = cv2.VideoCapture(0)

while True:
    success, frame = cam.read()

    if not success:
        break

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    elif cv2.waitKey(1) & 0xFF == ord('c'):
        req = threading.Thread(target=imgC.capture, args=(frame,)).start()
        if req == 0:
            print("Done")

    elif cv2.waitKey(1) & 0xFF == ord('d'):
        print("Starting")
        threading.Thread(target=matchImg.matching, args=(frame,)).start()

cam.release()
cv2.destroyAllWindows()