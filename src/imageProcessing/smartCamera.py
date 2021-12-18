from io import BytesIO
from camera import Camera
from face_detector import FaceFinder



class smartCamera(Camera, FaceFinder):
    def __init__(self) -> None:
        '''Constructor for smart Camera

        
        '''
        super().__init__()
        # self.camera = Camera()
        # self.faceDetector = FaceFinder()
        self.bareFaces = 0          #number of non-masked faces the camera detects
        self.maskedFaces = 0        #number of masked faces that the camera detects
        self.basePicture = BytesIO()          #Cached image ig
        self.processedPhotoBare = BytesIO()
        self.processedPhotoMasked = BytesIO() 
        

    def purgeStream(self):
        self.basePicture.seek(0)
        self.basePicture.truncate(0)

    def getNewPicture(self):  #gets a new pic and then performs analysis on them...
        self.purgeStream()
        self.basePicture = self.getPictureStream()
        self.updateFaceCount()

    def analyzeForBareFaces(self): 
        #else use the old picture, whatever that maybe
        self.bareFaces = self.getNumFacesFromImage(self.basePicture)
        #make a way to extract the pic that open cv makes...

    def updateFaceCount(self):
        self.analyzeForBareFaces()
        #self.analyzeForMaskedFaces()
    
    def getBasePicture(self):
        self.basePicture.seek(0)
        return self.basePicture

    def getNumBareFaces(self):
        return self.bareFaces
    
    def getNumMaskedFaces(self):
        return self.maskedFaces

    



        