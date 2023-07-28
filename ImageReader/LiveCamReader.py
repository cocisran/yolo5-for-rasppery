import cv2
from ImageReader import cam

def take_pick():
    '''Si le es posible intenta leer una imagen tomada desde el stream de origen'''
    ret, frame = cam().read()
    if not ret:
        return None
    return frame