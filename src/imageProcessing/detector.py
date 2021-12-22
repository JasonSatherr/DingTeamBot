from abc import ABC, abstractmethod
from io import BytesIO
from cv2 import cv2
class Detector(ABC):
    '''Abstract Parent Class for our image processing classes
    
    We want to be open to many ways of detecting people. Thus this 
    class is necessary to provide an equal interface throughout the detectors
    
    Attributes:
        classifier: A cv2 classifier that will find features
        processedPhoto: A bytes IO object that contains bounding boxes for
            features detected
        featuresFound: An integer representing how many features were found
    '''
    @abstractmethod
    def __init__(self, classifier, processedPhoto, featuresFound = 0) -> None:
        super().__init__()
        self.__classifier = classifier
        self.__processedPhoto = BytesIO()
        self.__featuresFound = featuresFound

    @property
    @abstractmethod
    def classifier(self):
        '''Gets the classifier'''
        pass

    @classifier.setter
    @abstractmethod
    def classifier(self, value):
        '''Sets the classifier'''
        pass

    @property
    @abstractmethod
    def processedPhoto(self):
        '''Gets the processed photo'''
        pass

    @processedPhoto.setter
    @abstractmethod
    def processedPhoto(self, value):
        '''Sets processedPhoto'''
        pass

    @property
    @abstractmethod
    def featuresFound(self):
        '''Gets featuresFound'''
        pass

    @featuresFound.setter
    @abstractmethod
    def featuresFound(self, value):
        '''Sets featuresFound'''
        pass

    def getStreamFromCVImage(self, image):
        '''Returns a bytesIO object given a CV image in .jpg format
        
        Args:
            image: A cv2 Mat image'''
        is_success, buffer = cv2.imencode(".jpg", image)
        io_buf = BytesIO(buffer)
        return io_buf
    
    def drawFeatureBoxes(self, image, featureLocations):
        '''Returns cv2 mat with boxes drawn around features
        
        Args:
            image: A cv2 Mat image to draw on
            featureLocations: A list of 4 dimension tuples (x, y, w, h)
                that represent the upper left corner of the feature with x and y
                and the width and height with w and h respectively'''
        for (x, y, w, h) in featureLocations:  #draw the faces  #if we make a parent class for this and...
            #maskFinder, then this is certainly a parent's method...
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return image
    
    @abstractmethod
    def processPhoto(self, stream):
        '''Returns processed image

        This class will take a BytesIO stream, convert it to a CV mat and
        then perform analysis on the photo to detect the features that need
        to be detected
        
        Args:
            stream: a bytes IO stream that will be transformed into a
                CV mat for image processing on'''
        pass
        