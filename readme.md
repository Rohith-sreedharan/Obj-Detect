# Object Detection using pre-trained YOLO model

This Python script uses the YOLO object detection model to detect green balls in a video. It will log the detections in a text file and display the video with bounding boxes around the detected balls. 

# Algorthim

The script performs the following steps:
1. Imports the necessary libraries: cv2 for video processing and ultralytics.YOLO for object detection.
2. Initialize the YOLO model with the "yolov8n.pt" weights file.
3. Open the video file "sam.mp4" using cv2.VideoCapture.
4. Initializes variables for counting the number of balls and calculating the total confidence.
5. Open a log file "ball_detections.txt" to write the detection details.
6. Enters a loop to read frames from the video.
7. Passes each frame to the YOLO model for object detection.
8. Iterates over the detected objects and checks if they are green balls with a confidence threshold of 0.25.
9. Draws bounding boxes around the detected balls on the frame.
10. Updates the ball count and total confidence.
11. Write the detection details in the log file.
12. Displays the frame with the bounding boxes.
13. To exit the loop, Check for the 'q' key press.
14. Release the video capture and close all windows.
15. Print the total ball count and average confidence.

# Description
The detect_balls function uses the YOLO object detection model to detect green balls in a video. It returns the total count of green balls detected and the average confidence score of the detected green balls.

# Inputs
None

# Installation

`pip3 install -r requirements.txt`

# Usage
`python3 main.py`

# Constraints
The script is designed to detect green balls in a video using the YOLO object detection model. It may not work well for other objects or scenarios.

# Note
- Please update your video file path in the script. at Line 6 in main.py

# Disclaimer
> The YOLO object detection model is a pre-trained model that may not work perfectly in all scenarios. The script is designed for educational purposes and may require modifications for specific use cases. This code is provided as an example and it is not guaranteed to work in all scenarios. Please use it at your own risk. 

# Author
- [RohithAditya](https://github.com/Rohith-Sreedharan)

# References
- [YOLOv5](https://github.com/ultralytics/yolov5)
- [OpenCV](https://opencv.org/)
- [YOLO Object Detection](https://pjreddie.com/darknet/yolo/)
- [Ultralytics YOLO](https://github.com/ultralytics)

# License
This project is licensed under the MIT License - see the LICENSE file for details.