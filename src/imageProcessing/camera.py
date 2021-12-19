import io
import time
import picamera

import numpy as np

# Create the in-memory stream
class Camera:
    def __init__(self) -> None:
        print("hello")
        pass

    def getPictureStream(self,mode):
        stream = io.BytesIO()
        with picamera.PiCamera(resolution =(1920,1080)) as camera:
            if isinstance(mode, str):
                if mode.lower() == 'sun' or mode.lower() == 'sunlight':
                    camera.awb_mode = 'sunlight'
                    print("SUN MODE")
            time.sleep(2)
            camera.capture(stream, format='jpeg')
        return stream
