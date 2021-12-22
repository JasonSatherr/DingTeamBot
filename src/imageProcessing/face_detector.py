from io import BytesIO
import cv2
import numpy as np
from abc import abc, abstractmethod
from detector import Detector
class FaceFinder(Detector):
    def __init__(self) -> None:
        self.__featuresFound = 0  #make private!!
        self.__processedPhoto = BytesIO()
        self.__classifier = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
        print("Face construct")

    def processPhoto(self, stream):
        '''Returns image processed for faces

        This class will take a BytesIO stream, convert it to a CV mat and
        then perform analysis on the photo to detect the features that need
        to be detected
        
        Args:
            stream: a bytes IO stream that will be transformed into a
                CV mat for image processing on'''
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 9) #neighbors hyperparameter
        self.__featuresFound = (len(faces))
        #When it's higher, it reduces the chance of a false +
        image = self.drawFeatureBoxes(image,faces)
        self.__processedPhoto = self.getStreamFromCVImage(image)
        #cv2.imwrite("./photos/sather.jpeg", image)

    # def __getStreamFromCVImage(self,image):
    #     '''gets the processed image to a readable stream'''
    #     is_success, buffer = cv2.imencode(".jpg", image)
    #     io_buf = BytesIO(buffer)
    #     return io_buf

    # def __drawFaceBoxes(self, image, faces):
    #     '''draws the face boxes on the image'''
    #     for (x, y, w, h) in faces:  #draw the faces  #if we make a parent class for this and...
    #         #maskFinder, then this is certainly a parent's method...
    #         cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
    #     return image

    @property
    @abstractmethod
    def classifier(self):
        '''Gets the classifier'''
        return self.__classifier

    @classifier.setter
    @abstractmethod
    def classifier(self, value):
        '''Sets the classifier'''
        self.__classifier = value 

    @property
    @abstractmethod
    def processedPhoto(self):
        '''Gets the processed photo'''
        return self.__processedPhoto

    @processedPhoto.setter
    @abstractmethod
    def processedPhoto(self, value):
        '''Sets processedPhoto'''
        self.__processedPhoto = value

    @property
    @abstractmethod
    def featuresFound(self):
        '''Gets featuresFound'''
        return self.__featuresFound

    @featuresFound.setter
    @abstractmethod
    def featuresFound(self, value):
        '''Sets featuresFound'''
        self.__featuresFound = value
    

    

    # def getNumFacesFromImage(self, stream):
    #     self.__processPhoto(stream)
    #     return self.__getFaceCount()
        
