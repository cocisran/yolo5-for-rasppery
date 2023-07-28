import cv2
import ctypes
import math
from SolarSpotter.Model import  Yolo5
from Util.Cv2Drawer import box_drawer

width = 1080
height = 720
model_path = "models/bestV4.pt"
yolo = Yolo5(model_path)
cv2.namedWindow("video test")

for i in range(1,8):
    videoFile = f"videos/video{i}.mp4"
    cap = cv2.VideoCapture(videoFile)
    frameRate = cap.get(5) #frame rate
    
    while(cap.isOpened()):
        frameId = cap.get(1) #current frame number
        ret, frame = cap.read() 

        if (ret != True):
            break

        if (frameId % (math.floor(frameRate) / 15) == 0):
            frame = cv2.resize(frame, (width, height))
            results = yolo.get_image_markers_over_confidence(frame, 0.7)
            for box in results:
                box_drawer(frame,**box)

            cv2.imshow("video test", frame)
            cv2.waitKey(0) 

    cap.release()

cv2.destroyAllWindows()
print ("Done!")
