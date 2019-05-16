

Process video frame by frame by detecting objects using Keras..
For illustration, the scripts are used to identify animal species in wild-life videos..

[1] 	To process a single image input,

		Usage: python3 keras-vgg16.py IMAGE

	Sample images are provided in 'sample-images' folder

	Top 5 most relevant tags are printed directly on stdout..

[2]	To process video,

	[A] If you prefer to run python script via command-line:

		Usage: python3 process-video.py VIDEO

		Sample video is provided for testing in 'sample-videos' folder

		Output of process-video.py script is stored in 'result/output.mp4' and shows
		the most relevant tags for each frame

	[B] Jupyter Notebook: video-tagger.ipynb

		Follow the step-by-step instructions for processing videos using object detection..

		Provides the option to either download an online video using youtube-dl library, or
		run video-tagger on local video file
