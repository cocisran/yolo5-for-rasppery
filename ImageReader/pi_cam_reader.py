from picamera2 import Picamera2
import time
import numpy

class PiCamera():
    '''Clase para leer el stream de la camara de la rasppery'''

    def __init__(self) -> None:
        self.picam = Picamera2()
        self.picam.start()
        print("Starting Camera")
        time.sleep(1)

    def take_picture(self):
        '''Toma una foto de la camara'''
        image = self.picam.capture_image("main")
        return numpy.array(image)
