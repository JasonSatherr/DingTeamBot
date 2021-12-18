from io import BytesIO
from camera import Camera
from face_detector import FaceFinder



class smartCamera(FaceFinder, Camera):
    def __init__(self) -> None:
        '''Constructor for smart Camera

        
        '''
        self.faceFinder = FaceFinder()
        self.bareFaces = 0          #number of non-masked faces the camera detects
        self.maskedFaces = 0        #number of masked faces that the camera detects
        self.basePicture = BytesIO()          #Cached image ig
        self.processedPhotoBare = BytesIO()
        self.processedPhotoMasked = BytesIO() 
        

    def purgeStream(self):
        self.basePicture.seek(0)
        self.basePicture.truncate(0)

    def takeNewPicture(self,mode):  #gets a new pic and then performs analysis on them...
        self.purgeStream()
        self.basePicture = self.getPictureStream(mode)
        self.__processPhoto()


    def __processPhoto(self):
        self.__analyzeForBareFaces()
        self.__setProcessedPhotoBare()
        # self.analyzeForMaskedFaces()

    def __analyzeForBareFaces(self): 
        self.faceFinder.processPhoto(self.basePicture)
        self.bareFaces = self.faceFinder.getFaceCount()

    def __setProcessedPhotoBare(self):
        self.processedPhotoBare = self.faceFinder.getProcessedPhoto()
        self.processedPhotoBare.seek(0)
    
    def getBasePicture(self):
        self.basePicture.seek(0)
        return self.basePicture

    def getProcessedPhotoBare(self):
        return self.processedPhotoBare

    def getNumBareFaces(self):
        return self.bareFaces
    
    def getNumMaskedFaces(self):
        return self.maskedFaces

    



        