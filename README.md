

Note: Eventually the files in this directory will be replaced with a single Jupyter Notebook
to demonstrate object detection with Keras, to identify animal species in wild life vidoes..

Till then, try:

[1] 	To process a single image input,
		Usage: python3 keras-vgg16.py IMAGE
	Sample images are provided in 'sample-images' folder

[2]	To process video,
		Usage: python3 process-video.py VIDEO
	Few sample videos are provided in 'sample-videos' folder
	In future, the script will allow user to automatically download a video from a given public url

	Output of process-video.py script is stored in 'result' directory as 'output.mp4', and shows
	the most probable tag for each frame
