import cv2
from SolarSpotter.Model import  Yolo5
from ImageReader import LiveCamReader, current_frame, frame_rate
from Util.Cv2Drawer import box_drawer
model_path = "models/bestV3.pt"

yolo = Yolo5(model_path)

cv2.namedWindow("test")

for i in range(64):
    ruta_imagen = f'data/test{i+1}.jpg'
    image = cv2.imread(ruta_imagen)
    results = yolo.get_image_markers_over_confidence(image, 0.6)
    for box in results:
        box_drawer(image,**box)
    if results:
        cv2.imshow("test", image)
        cv2.waitKey(0)
    print(results)



cv2.destroyAllWindows()
