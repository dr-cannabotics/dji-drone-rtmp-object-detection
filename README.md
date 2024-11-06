Sure! Here's the updated project description with the final line added:

---

# Real-Time Object Detection with DJI Mini 3 Pro

This project enables real-time object detection using the video feed from the DJI Mini 3 Pro drone and DJI Goggles 2. The setup streams the video to a Node.js RTMP server, where the feed is processed with OpenCV for object detection.

## Components

- **DJI Mini 3 Pro & DJI Goggles 2**: Capture and display video feed.
- **Smartphone**: Streams video from DJI Fly app to RTMP server.
- **Node.js RTMP Server**: Receives and relays video feed.
- **OpenCV**: Analyzes the feed for object detection.

## Project Structure

```
dji-drone-rtmp-object-detection/
├── server.js                     # RTMP server configuration
├── opencv_detection.py           # Object detection script
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config
├── frozen_inference_graph.pb     # Detection model
├── labels.txt                    # COCO class labels
└── README.md                     # Documentation
```

## Setup Instructions

### 1. Install Node.js and RTMP Server

- Install Node.js: `node -v`, `npm -v`.
- Clone the repo and install dependencies: 
  ```bash
  git clone https://github.com/dr-cannabotics/dji-drone-rtmp-object-detection/
  cd dji-drone-rtmp-object-detection
  npm install node-media-server
  ```
- Start the server: 
  ```bash
  node server.js
  ```
  The server will listen at `rtmp://127.0.0.1:1935/live`.

### 2. Stream Video

- Connect DJI Goggles 2 to your drone and smartphone.
- Use the DJI Fly app to stream the feed to `rtmp://127.0.0.1:1935/live`.

### 3. Verify the RTMP Stream with VLC

- Open VLC and go to **Media > Open Network Stream...**.
- Enter the stream URL: `rtmp://127.0.0.1:1935/live`.
- Click **Play** to view the live stream and ensure the video feed is working.

### 4. Set Up OpenCV for Object Detection

- **Using Virtual Environment** (recommended):
  ```bash
  python3 -m venv ~/myenv
  source ~/myenv/bin/activate
  pip install opencv-python
  ```
- Update `opencv_detection.py` with:
  ```python
  cap = cv2.VideoCapture('rtmp://127.0.0.1:1935/live')
  ```
- Run the object detection script:
  ```bash
  python opencv_detection.py
  ```

### Optional: Custom Object Detection Model

- To train a custom model, fine-tune a pre-trained SSD MobileNet V3 model with TensorFlow on a labeled dataset.
- After training, update `opencv_detection.py` to use your new model for real-time detection.

## Usage

1. Start the RTMP server:
   ```bash
   node server.js
   ```
2. Stream from DJI Goggles 2 via the DJI Fly app.
3. Verify the RTMP stream with VLC as described above.
4. Run the OpenCV script to see object detection in action.

## Notes

- Ensure both devices are on the same Wi-Fi network.
- Adjust RTMP settings for better performance.
- Fine-tune confidence thresholds in `opencv_detection.py` for better accuracy.

---

**Happy hacking, flying, and forking!**

--- 

This includes your request at the end of the document, adding a fun note to the users!
