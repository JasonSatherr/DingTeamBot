import io
import time
import picamera

import numpy as np

# Create the in-memory stream
class Camera:
    def __init__(self) -> None:
        print("hello")
        pass

    def getPictureStream(self):
        stream = io.BytesIO()
        with picamera.PiCamera() as camera:
            camera.start_preview()
            time.sleep(2)
            camera.capture(stream, format='jpeg')
        return stream
