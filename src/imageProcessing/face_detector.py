from io import BytesIO
import cv2
import numpy as np

# Create the in-memory stream

class FaceFinder:
    def __init__(self) -> None:  #we need to handle the cold start ig
        self.facesFound = 0  #make private!!
        self.processedPhoto = BytesIO()
        self.face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml')
        print("Face construct")

    def processPhoto(self, stream):
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, 1.1, 9) #neighbors hyperparameter
        self.__setFaceCount(len(faces))
        #When it's higher, it reduces the chance of a false +
        image = self.__drawFaceBoxes(image,faces)
        self.__setProcessedPhoto(self.__getStreamFromCVImage(image))
        #cv2.imwrite("./photos/sather.jpeg", image)

    def __getStreamFromCVImage(self,image):
        is_success, buffer = cv2.imencode(".jpg", image)
        io_buf = BytesIO(buffer)
        return io_buf

    def __drawFaceBoxes(self, image, faces):
        for (x, y, w, h) in faces:  #draw the faces  #if we make a parent class for this and...
            #maskFinder, then this is certainly a parent's method...
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
        return image

    def __setFaceCount(self, numFaces):
        self.facesFound = numFaces

    def __setProcessedPhoto(self, processedPhoto):
        self.processedPhoto = processedPhoto

    def getFaceCount(self):
        return self.facesFound

    def getProcessedPhoto(self):
        return self.processedPhoto

    

    

    # def getNumFacesFromImage(self, stream):
    #     self.__processPhoto(stream)
    #     return self.__getFaceCount()
        
