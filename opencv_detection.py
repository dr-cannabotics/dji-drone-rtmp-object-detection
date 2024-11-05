# opencv_detection.py
import cv2

# Load the model configuration and weights
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

# Load class labels
classLabels = []
filename = 'labels.txt'
with open(filename, 'rt') as spt:
    classLabels = spt.read().rstrip('\n').split('\n')

# Set model input parameters
model.setInputSize(320, 320)  # Adjust size for performance
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# Open RTMP stream
cap = cv2.VideoCapture('rtmp://<your-laptop-IP>:1935/live')
if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Get screen dimensions (adjusted to smaller size)
screen_width = 900  # Example: adjusted width
screen_height = 550  # Example: adjusted height

font = cv2.FONT_HERSHEY_PLAIN

try:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        classIndex, confidence, bbox = model.detect(frame, confThreshold=0.65)  # Confidence threshold
        if len(classIndex) != 0:
            for classInd, boxes in zip(classIndex.flatten(), bbox):
                cv2.rectangle(frame, boxes, (255, 0, 0), 2)
                cv2.putText(frame, classLabels[classInd - 1], (boxes[0] + 10, boxes[1] + 40), font, fontScale=1, color=(0, 255, 0), thickness=2)

        # Resize frame to fit the screen
        resized_frame = cv2.resize(frame, (screen_width, screen_height))

        # Show the resized frame in a window
        cv2.imshow('Result', resized_frame)

        # Break loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {e}")
finally:
    cap.release()
    cv2.destroyAllWindows()
