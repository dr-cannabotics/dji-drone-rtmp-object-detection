
---

# Real-Time Object Detection and Live Streaming with DJI Mini 3 Pro over RTMP

This project enables real-time object detection on live video streams from a DJI Mini 3 Pro drone, utilizing DJI Goggles 2, an RTMP server, and OpenCV. Designed for applications requiring immediate analysis of aerial footage—such as surveillance and environmental monitoring—the system streams from the DJI Fly app to a Node.js RTMP server, where OpenCV processes each frame for object detection. The setup supports pre-trained models to detect and highlight objects within the video feed in real time.

> **Forked from:** [zafarRehan/object_detection_COCO](https://github.com/zafarRehan/object_detection_COCO)

---

## Project Structure

```
dji-drone-rtmp-object-detection/
├── server.js                                      # RTMP server configuration
├── opencv_detection_image.py                      # Object detection script for images (independent)
├── opencv_detection_rtmp.py                       # Object detection script for RTMP stream
├── opencv_detection_video.py                      # Object detection script for video files (independent)
├── opencv_detection_webcam.py                     # Object detection script for webcam input (independent)
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt   # Model configuration for SSD MobileNet
├── frozen_inference_graph.pb                      # Pre-trained object detection model
├── labels.txt                                     # COCO class labels
└── README.md                                      # Documentation
```

---

## Components

- **DJI Mini 3 Pro & DJI Goggles 2**: Capture and display the video feed.
- **Smartphone**: Streams video via the DJI Fly app to an RTMP server.
- **Node.js RTMP Server**: Manages the video stream.
- **OpenCV**: Processes video frames for object detection.

## Features

- **Real-Time Detection**: Processes video frames with OpenCV in real time, detecting objects based on COCO classes.
- **Low-Latency Streaming**: Streams live video from the DJI Fly app to a local RTMP server, viewable on VLC or similar clients.
- **Independent Detection Scripts**: `opencv_detection_image.py`, `opencv_detection_video.py`, and `opencv_detection_webcam.py` can run independently for detecting objects in images, video files, or webcam feeds, without requiring the RTMP server.

---

## Getting Started

### Prerequisites

1. **Node.js**: Ensure Node.js is installed.
2. **Python 3.x**: Set up Python and install OpenCV for object detection.
3. **DJI Fly App**: Use the DJI Fly app on a smartphone to configure video streaming.

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/dr-cannabotics/dji-drone-rtmp-object-detection/
   cd dji-drone-rtmp-object-detection
   ```

2. **Set Up RTMP Server**:
   - Install dependencies:
     ```bash
     npm install node-media-server
     ```
   - Start the RTMP server:
     ```bash
     node server.js
     ```
     The server listens on `rtmp://127.0.0.1:1935/live`.

3. **Configure DJI Fly App for RTMP Streaming**:
   - Connect DJI Goggles 2 to the drone and smartphone.
   - Configure the stream in DJI Fly app to `rtmp://127.0.0.1:1935/live`.

4. **Verify RTMP Stream (Optional)**:
   - Open VLC, navigate to **Media > Open Network Stream**.
   - Enter the RTMP URL: `rtmp://127.0.0.1:1935/live`.
   - Click **Play** to confirm the live video feed is working.

5. **Install OpenCV in Python**:
   - Set up a virtual environment (optional):
     ```bash
     python3 -m venv ~/myenv
     source ~/myenv/bin/activate
     ```
   - Install OpenCV:
     ```bash
     pip install opencv-python
     ```

---

## Running the Python Detection Scripts

The following scripts are included in the project and can be run independently for different video sources. Only `opencv_detection_rtmp.py` requires the RTMP server; the others do not.

### 1. **Detect Objects in RTMP Stream**

   For detecting objects on a live RTMP stream from the DJI drone:
   ```bash
   python opencv_detection_rtmp.py
   ```
   *Note*: Ensure the DJI Fly app is streaming to `rtmp://127.0.0.1:1935/live`, as configured above.

### 2. **Detect Objects in an Image**

   For detecting objects in a single image file:
   - Place your target image in the project folder or specify its path in the script.
   - Open `opencv_detection_image.py` and update the image path:
     ```python
     img = cv2.imread('test_image.png')  # Specify the path to your image file
     ```
   - Run the script:
     ```bash
     python opencv_detection_image.py
     ```
   *Note*: This script runs independently and does not require the RTMP server.

### 3. **Detect Objects in a Video File**

   For detecting objects in a video file:
   - Place your target video file in the project folder or specify its path in the script.
   - Open `opencv_detection_video.py` and update the video file path:
     ```python
     cap = cv2.VideoCapture('test_video.mp4')  # Specify the path to your video file
     ```
   - Run the script:
     ```bash
     python opencv_detection_video.py
     ```
   *Note*: This script runs independently and does not require the RTMP server.

### 4. **Detect Objects via Webcam**

   For real-time object detection using your computer’s webcam:
   ```bash
   python opencv_detection_webcam.py
   ```
   *Note*: This script runs independently and does not require the RTMP server.

---

Happy flying, hacking, and object-detecting! 🛸

---
