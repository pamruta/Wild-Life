
import keras

# loading weights from VGG-16 pre-trained model
from keras.applications.vgg16 import VGG16
model = VGG16()

print("VGG-16 Model is loaded..")

# load input image and preprocess it for predictions
import sys
filename = sys.argv[1]

from keras.preprocessing import image
input = image.load_img(filename, target_size=(224, 224))
input = image.img_to_array(input)

import numpy as np
input = np.expand_dims(input, axis=0)

from keras.applications.vgg16 import preprocess_input
input = preprocess_input(input)

# run model
predictions = model.predict(input)

# print objects detected and confidence scores
from keras.applications.vgg16 import decode_predictions
# top K labels
for label in decode_predictions(predictions, top=5)[0]:
	# apply some threshold on confidence score
	# or 0 to print all top 5
	if label[2] > 0:
		print(label[1] + ": " + str(label[2]))
