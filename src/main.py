from camera import Camera
from face_detector import FaceFinder

def main():
    """The main file will run everything
    """
    cam = Camera()
    stream = cam.getPictureStream()
    faceFinder = FaceFinder()
    numFaces = faceFinder.getNumFacesFromImage(stream)
    print('we found '+ str(numFaces)+ ' faces')



if __name__ == "__main__":
    main()