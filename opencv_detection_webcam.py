import cv2

# Load the model configuration and weights
config_file = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
frozen_model = 'frozen_inference_graph.pb'

model = cv2.dnn_DetectionModel(frozen_model, config_file)

# Load the class labels
classLabels = []
filename = 'labels.txt'
with open(filename, 'rt') as spt:
    classLabels = spt.read().rstrip('\n').split('\n')

# Set model input parameters
model.setInputSize(320, 320)  # Adjust for better results
model.setInputScale(1.0 / 127.5)
model.setInputMean((127.5, 127.5, 127.5))
model.setInputSwapRB(True)

# Initialize the webcam
cap = cv2.VideoCapture(0)  # '0' is usually the default webcam. Change if using a different camera.

# Define the font
font = cv2.FONT_HERSHEY_PLAIN

while True:
    # Capture each frame
    ret, frame = cap.read()
    if not ret:
        break  # Exit if the frame is not captured

    # Perform object detection
    classIndex, confidence, bbox = model.detect(frame, confThreshold=0.5)  # Tune confThreshold as needed

    # Draw bounding boxes and labels on detected objects
    for classInd, conf, boxes in zip(classIndex.flatten(), confidence.flatten(), bbox):
        cv2.rectangle(frame, boxes, (255, 0, 0), 2)
        cv2.putText(frame, classLabels[classInd - 1], (boxes[0] + 10, boxes[1] + 40), font,
                    fontScale=3, color=(0, 255, 0), thickness=3)

    # Display the resulting frame
    cv2.imshow('Webcam Object Detection', frame)

    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
