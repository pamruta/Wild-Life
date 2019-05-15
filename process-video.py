
# loading VGG16 pre-trained model in keras
import keras
from keras.applications.vgg16 import VGG16
model = VGG16()

print("VGG-16 Model is Loaded...")

# return label containing the animal species detected in a given image
def get_label(input_image):

	# pre-process input image

	from keras.preprocessing import image
	input_image = image.img_to_array(input_image)

	import numpy as np
	input_image = np.expand_dims(input_image, axis=0)

	from keras.applications.vgg16 import preprocess_input
	input_image = preprocess_input(input_image)

	# run model to get objects detected 
	predictions = model.predict(input_image)

	# return the first label with confidence above certain threshold
	from keras.applications.vgg16 import decode_predictions
	for label in decode_predictions(predictions, top=5)[0]:
		if label[2] > 0.6:
			return label[1]

	return ""

# process video frame by frame 
def process_video(stream):

	# create output video in mp4 format
	codec = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')

	# note: size of the output video must match with the input
	output = cv2.VideoWriter('result/output.mp4', codec, 10, (1280, 720), True)

	label = ""

	while 1:

		flag, frame = stream.read()

		if flag:

			# resizing frame size for keras vgg-16 model
			bgr_frame = cv2.resize(frame, (224, 224))

			# converting opencv BGR format to RGB for keras
			rgb_frame = cv2.cvtColor(bgr_frame, cv2.COLOR_BGR2RGB)

			# calling keras vgg-16 model for image recognition
			label = get_label(rgb_frame)

			cv2.putText(frame, label, (100,100), cv2.FONT_HERSHEY_DUPLEX, 2.0, (0,255,255))
			output.write(frame)
			cv2.imshow('Wild Life', frame)

			if cv2.waitKey(10) & 0xFF == ord('q'):
        	                break
		else:
			break

	output.release()
	stream.release()
	cv2.destroyAllWindows()

	return 1


# get video filename from command line
import sys
video = sys.argv[1]

# create video stream in opencv
import cv2
stream = cv2.VideoCapture(video)

# process video stream and print labels
print("Video Processing Started..")
process_video(stream)

print("Video Processing Completed..")

