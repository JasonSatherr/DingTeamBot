from camera import Camera
from face_detector import FaceFinder



class smartCamera():
    def __init__(self) -> None:
        '''Constructor for smart Camera

        
        '''
        self.camera = Camera()
        self.faceDetector = FaceFinder()
        self.bareFaces = 0          #number of non-masked faces the camera detects
        self.maskedFaces = 0        #number of masked faces that the camera detects

    def analyzeForFaces(self):
        stream = self.camera.getPictureStream()