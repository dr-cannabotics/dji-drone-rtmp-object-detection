import cv2
import yt_dlp
import numpy as np

# Define fixed paths for the model and labels
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'
label_file_path = 'labels.txt'

# Load the model
model = cv2.dnn_DetectionModel(frozen_model, config_file)

# Load class labels
with open(label_file_path, 'rt') as f:
    classLabels = f.read().strip().splitlines()

# Set model input configurations
model.setInputSize(320, 320)
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# Ask the user if they want to provide a YouTube URL or use a sample video
user_input = input("Enter a YouTube link or type 'sample' to use a default video: ").strip()

# Set the default YouTube URL if user chooses 'sample'
if user_input.lower() == 'sample':
    yt_url = 'https://www.youtube.com/watch?v=Uw746Bv3t_E'  # Example sample video
else:
    yt_url = user_input  # Use user-provided URL

# Use yt-dlp to fetch the direct stream URL
ydl_opts = {'format': 'best[ext=mp4]'}
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    try:
        info_dict = ydl.extract_info(yt_url, download=False)
        video_stream_url = info_dict['url']
    except Exception as e:
        print(f"Error extracting video: {e}")
        exit()

# Open the video capture from the stream URL
cap = cv2.VideoCapture(video_stream_url)

if not cap.isOpened():
    print("Error opening video stream or file")
    exit()

# Set the starting position of the video to 1 minute (60 seconds)
cap.set(cv2.CAP_PROP_POS_MSEC, 60000)  # 60,000 milliseconds = 1 minute

# Create a named window to control the size of the output window (resizable)
cv2.namedWindow('YouTube Stream Object Detection', cv2.WINDOW_NORMAL)

# Optionally, set the default size for the window (before resizing)
cv2.resizeWindow('YouTube Stream Object Detection', 1280, 720)  # Default HD size (optional)

# Process each frame from the video stream
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Resize the frame to make it larger (optional: scale factor)
    frame_resized = cv2.resize(frame, (1280, 720))  # Resize to 1280x720 for larger display

    # Detect objects in the current frame
    results = model.detect(frame_resized, confThreshold=0.5)  # Adjust the confidence threshold here if needed
    
    # Validate the output structure and proceed if valid
    if isinstance(results, tuple) and len(results) == 3:
        classIndex, confidence, bbox = results

        # Ensure each part is a non-empty list or array
        if classIndex is not None and len(classIndex) > 0:
            for classInd, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
                # Get the class label and confidence score for each detected object
                label = classLabels[classInd - 1]  # COCO labels are 1-indexed, so subtract 1
                label_text = f"{label}: {conf:.2f}"

                # Draw the bounding box for the detected object
                cv2.rectangle(frame_resized, boxes, (255, 0, 0), 2)
                cv2.putText(frame_resized, label_text, (boxes[0] + 10, boxes[1] + 40), 
                            cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 2)

    # Show the result in a resizable window
    cv2.imshow('YouTube Stream Object Detection', frame_resized)

    # Break on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()
