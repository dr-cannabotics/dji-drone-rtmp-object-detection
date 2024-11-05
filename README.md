---

# Real-Time Object Detection with DJI Mini 3 Pro

This project enables real-time object detection using a video feed from the DJI Mini 3 Pro drone and DJI Goggles 2. The setup streams the video from the DJI Goggles 2 to a Node.js RTMP server, where the feed is processed with OpenCV for object detection.

## Project Overview

### Key Components

- **DJI Mini 3 Pro & DJI Goggles 2:** Capture and display the video feed.
- **Smartphone:** Connects to DJI Goggles 2 and uses the DJI Fly app to stream video to an RTMP server.
- **Node.js RTMP Server:** Hosted on a laptop to receive and relay the video stream.
- **OpenCV Script:** Analyzes the video feed in real-time for object detection.

### Prerequisites

- **Hardware:** DJI Mini 3 Pro, DJI Goggles 2, and a compatible smartphone.
- **Software:** Laptop with Node.js, Python, and OpenCV installed.
- **Network:** Ensure both the smartphone and laptop are on the same Wi-Fi network.

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

### Step 1: Install Node.js and Set Up RTMP Server

1. **Install Node.js:** Follow platform-specific instructions from [Node.js official site](https://nodejs.org/).
2. **Verify Installation:**

    ```bash
    node -v
    npm -v
    ```

3. **Clone Repository and Install Dependencies:**

    ```bash
    git clone https://github.com/dr-cannabotics/dji-drone-rtmp-object-detection/
    cd dji-drone-rtmp-object-detection
    npm install node-media-server
    ```

4. **Configure and Run RTMP Server:** Edit `server.js` to set the server settings, then run:

    ```bash
    node server.js
    ```

    The server will listen on `rtmp://127.0.0.1:1935/live`.

### Step 2: Stream Video Feed

1. **Connect DJI Goggles 2 to the drone and smartphone.**
2. **Install DJI Fly app** on the smartphone to display the video feed.
3. **Use the DJI Fly app to stream the feed to the RTMP server:**
   - **URL:** `rtmp://127.0.0.1:1935/live`
   - **Stream Key:** Leave empty or use a custom key.
4. **Start Streaming** from the DJI Fly app.

### Step 3: Set Up OpenCV for Object Detection

1. **Install Python Dependencies:**

    ```bash
    pip install opencv-python
    ```

2. **Download Model Files** and place them in the project directory.
3. **Update RTMP Stream URL** in `opencv_detection.py`:

    ```python
    cap = cv2.VideoCapture('rtmp://127.0.0.1:1935/live')
    ```

4. **Run the Python Script:**

    ```bash
    python opencv_detection.py
    ```

## Training the Object Detection Model

To train or fine-tune the object detection model for custom objects:

1. **Prepare the Dataset:** Label images with tools like LabelImg and convert annotations into TFRecord format.
2. **Fine-tune a Pre-trained Model:** Use a pre-trained model like SSD MobileNet V3 and fine-tune it with TensorFlow on your custom dataset.

### Training Steps:

- Download and set up the TensorFlow Object Detection API.
- Convert the dataset into TFRecord format.
- Fine-tune the model using a pre-trained checkpoint and configure it with your dataset.
- Export the trained model once training is complete.

### Inference with OpenCV:

After training, use the new model in `opencv_detection.py` for real-time object detection.

## Usage

1. **Start the RTMP server:**

    ```bash
    node server.js
    ```

2. **Stream from DJI Goggles 2** using the DJI Fly app to the RTMP server.
3. **Run the OpenCV script** to view real-time object detection results from the RTMP live stream server.

### Example Output

Real-time detection of objects (e.g., people, cars) with bounding boxes and labels using the SSD MobileNet V3 model.

## Notes

- Ensure both devices are on the same local network.
- Adjust RTMP settings for latency and performance.
- Modify detection confidence thresholds in `opencv_detection.py` if necessary.

## Troubleshooting

- **Video Stream Issues:** Verify the RTMP server is running and the URL is correct.
- **Latency:** Optimize RTMP settings or network conditions.
- **Detection Accuracy:** Fine-tune confidence thresholds in the detection script.

## Contributing

Contributions are welcome! Fork the repository and submit pull requests.

---

Happy coding and flying! 🎉

--- 

