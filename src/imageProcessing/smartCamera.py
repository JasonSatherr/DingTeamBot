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
        self.basePicture = self.getPictureStream()          #Cached image ig
        self.processedPhotoBare = None
        self.processedPhotoMasked = None
        

    def purgeStream(self):
        self.basePicture.seek(0)
        self.basePicture.truncate(0)

    def getNewPicture(self):
        self.purgeStream()
        self.basePicture = self.getPictureStream()

    def analyzeForBareFaces(self, newPicture = False): 
        if newPicture:
            self.getNewPicture()
        #else use the old picture, whatever that maybe
        self.bareFaces = self.getNumFacesFromImage(self.basePicture)
        #make a way to extract the pic that open cv makes...

    def updateFaceCount(self, newPicture = False):
        self.analyzeForBareFaces(newPicture)
        #self.analyzeForMaskedFaces(newPicture)
        

    def getNumBareFaces(self):
        return self.bareFaces
    
    def getNumMaskedFaces(self):
        return self.maskedFaces

    



        