import time
import picamera

class cameraTester:
    def __init__(self) -> None:
        pass
    def runAWBTests(self):
        with picamera.PiCamera() as camera:
            camera.resolution = (1024, 768)
            # for mode in camera.AWB_MODES:
                
            #     camera.awb_mode = mode
            #     time.sleep(2)
            #     camera.capture('./photos/'+str(mode)+'foo.jpeg')
            #     print("snap")
            camera._set_iso(20)
            camera.awb_mode = 'sunlight'
            time.sleep(2)
            camera.capture('./photos/sunnyIdiot.jpeg')
            print("snap")
                #'sunlight is a good mode'
                