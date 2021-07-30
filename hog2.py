import cv2
import imutils
from people import App
import _thread
import people2

# Initializing the HOG person
# detector

	#pedestrian_detection_image(path)

class start():

    def __init__(self, path):
        self.pedestrian_detection_video(path)
        
    def pedestrian_detection_image(self, image):
        regions = 0
        hog = cv2.HOGDescriptor()
        cv2.namedWindow('Image')
        hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

        # # Reading the Image
        # image = cv2.imread(img)


        # Resizing the Image
        image = imutils.resize(image,
                            width=min(400, image.shape[1]))

        # Detecting all the regions in the
        # Image that has a pedestrians inside it
        (regions, _) = hog.detectMultiScale(image,
                                            winStride=(6, 8),
                                            padding=(1, 1),
                                            scale=1.018)

        # Drawing the regions in the Image
        for (x, y, w, h) in regions:
            cv2.rectangle(image, (x, y),
                        (x + w, y + h),
                        (0, 0, 255), 2)

        # Showing the output Image
        cv2.imshow('Image', image)
        cv2.waitKey(1)
        # cv2.destroyAllWindows()

    def pedestrian_detection_video(self, path):

        cap = cv2.VideoCapture(path)
        # people.app.lbl_Counter
        # people2.counter()
        while cap.isOpened():
            r,frame = cap.read()
            self.pedestrian_detection_image(frame)
		

