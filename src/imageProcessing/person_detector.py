#At this point I should have a detector super class x.x
#OH GOD I NEED A SUPER CLASS
import numpy as np
import cv2
from io import BytesIO

class PersonDetector:
    def __init__(self) -> None:
        self.peopleFound = 0  #make private!!
        self.processedPhoto = BytesIO()
        self.hog = cv2.HOGDescriptor()
        self.hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

    def processPhoto(self, stream):
        data = np.frombuffer(stream.getvalue(), dtype=np.uint8)
        image = cv2.imdecode(data, 1)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        boxes, weights = self.hog.detectMultiScale(gray, winStride=(24,24))
        self.__setPeopleCount(len(boxes))
        self.__drawBoxes(image, boxes)
        self.__setProcessedPhoto(self.__getStreamFromCVImage(image))

    
    def __getStreamFromCVImage(self,image):
        '''gets the processed image to a readable stream'''
        is_success, buffer = cv2.imencode(".jpg", image)
        io_buf = BytesIO(buffer)
        return io_buf

    def __drawBoxes(self, image, boxes):
        '''draws the face boxes on the image'''
        boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

        for (xA, yA, xB, yB) in boxes:
            # display the detected boxes in the colour picture
            cv2.rectangle(image, (xA, yA), (xB, yB),
                            (0, 255, 0), 2)
        return image

    def __setPeopleCount(self, numPeople):
        '''sets face count'''
        self.peopleFound = numPeople

    def __setProcessedPhoto(self, processedPhoto):
        self.processedPhoto = processedPhoto

    def getFaceCount(self):
        return self.peopleFound

    def getProcessedPhoto(self):
        return self.processedPhoto


    #PEOPLE DETECT HERE!!!!
    # cv2.startWindowThread()

    # # open webcam video stream
    # cap = cv2.VideoCapture(0)

    # # the output will be written to output.avi
    # out = cv2.VideoWriter(
    #     'output.avi',
    #     cv2.VideoWriter_fourcc(*'MJPG'),
    #     15.,
    #     (640,480))

    # while(True):
    #     # Capture frame-by-frame
    #     ret, frame = cap.read()

    #     # resizing for faster detection
    #     frame = cv2.resize(frame, (640, 480))
    #     # using a greyscale picture, also for faster detection
    #     gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)

    #     # detect people in the image
    #     # returns the bounding boxes for the detected objects
    #     boxes, weights = hog.detectMultiScale(frame, winStride=(8,8) )

        
        
    #     # Write the output video 
    #     out.write(frame.astype('uint8'))
    #     # Display the resulting frame
    #     cv2.imshow('frame',frame)
    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break

    # # When everything done, release the capture
    # cap.release()
    # # and release the output
    # out.release()
    # # finally, close the window
    # cv2.destroyAllWindows()
    # cv2.waitKey(1)