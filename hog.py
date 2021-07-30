import cv2
import imutils
import time
import sendEmail
# Initializing the HOG person
# detector
	#pedestrian_detection_image(path)
def pedestrian_detection_image(image, counter):
	hog = cv2.HOGDescriptor()
	cv2.namedWindow('Image')
	hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

	# # Reading the Image
	# image = cv2.imread(img)


	# Resizing the Image
	image = imutils.resize(image, width=min(400, image.shape[1]))

	# Detecting all the regions in the
	# Image that has a pedestrians inside it
	(regions, _) = hog.detectMultiScale(image, winStride=(6, 8), padding=(1, 1), scale=1.018)

	# Drawing the regions in the Image
	for (x, y, w, h) in regions:
		cv2.rectangle(image, (x, y), (x + w, y + h), (0, 0, 255), 2)

	# Showing the output Image
	# print('Number of People: ', len(regions))
	cv2.putText(image, str(len(regions)), (5,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
	cv2.imshow('Image', image)
	if(len(regions) > 2 and counter < 1):
		print('Alert Sent')
		sendEmail.send("aditya.shresth17@gmail.com", 'Crowd Detected!', 'It is to be informed that crowd is detected at area 51.')
		counter += 1
	cv2.waitKey(1)
	return counter
	# cv2.destroyAllWindows()

def pedestrian_detection_video(path):

	cap = cv2.VideoCapture(path)
	# people.app.lbl_Counter
	# people2.counter()
	counter = 0
	while cap.isOpened():
		r,frame = cap.read()
		counter += pedestrian_detection_image(frame, counter)

		

