from io import BytesIO
from camera import Camera
from face_detector import FaceFinder



class smartCamera(Camera, FaceFinder):
    def __init__(self) -> None:
        '''Constructor for smart Camera

        
        '''
        # self.camera = Camera()
        # self.faceDetector = FaceFinder()
        self.bareFaces = 0          #number of non-masked faces the camera detects
        self.maskedFaces = 0        #number of masked faces that the camera detects
        self.stream = self.getPictureStream()          #Cached image ig
        

    def purgeStream(self):
        self.stream.seek(0)
        self.stream.truncate(0)

    def getNewPicture(self):
        self.purgeStream()
        self.stream = self.getPictureStream()

    def analyzeForBareFaces(self, newPicture = False): 
        if newPicture:
            self.getNewPicture()
        #else use the old picture, whatever that maybe
        self.bareFaces = self.getNumFacesFromImage(self.stream)
        #make a way to extract the pic that open cv makes...



        