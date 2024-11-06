
---

# Real-Time Object Detection with DJI Mini 3 Pro

This project enables real-time object detection using a video feed from the DJI Mini 3 Pro drone and DJI Goggles 2. The setup streams the video from the DJI Goggles 2 to a Node.js RTMP server, where the feed is processed with OpenCV for object detection.

## Project Overview

### Key Components

- **DJI Mini 3 Pro & DJI Goggles 2**: Capture and display the video feed.
- **Smartphone**: Connects to DJI Goggles 2 and uses the DJI Fly app to stream video to an RTMP server.
- **Node.js RTMP Server**: Hosted on a laptop to receive and relay the video stream.
- **OpenCV Script**: Analyzes the video feed in real-time for object detection.

### Prerequisites

- **Hardware**: DJI Mini 3 Pro, DJI Goggles 2, and a compatible smartphone.
- **Software**: Laptop with Node.js, Python, and OpenCV installed.
- **Network**: Ensure both the smartphone and laptop are on the same Wi-Fi network.

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

Install Node.js by following the platform-specific instructions on the Node.js official site.

Verify installation with:

```bash
node -v
npm -v
```

Clone the repository and install dependencies:

```bash
git clone https://github.com/dr-cannabotics/dji-drone-rtmp-object-detection/
cd dji-drone-rtmp-object-detection
npm install node-media-server
```

Configure and run the RTMP server by editing `server.js` and then starting the server with:

```bash
node server.js
```

The server will listen on `rtmp://127.0.0.1:1935/live`.

### Step 2: Stream Video Feed

1. Connect DJI Goggles 2 to the drone and smartphone.
2. Install the DJI Fly app on the smartphone to display the video feed.
3. Use the DJI Fly app to stream the feed to the RTMP server:
   - **URL**: `rtmp://127.0.0.1:1935/live`
   - **Stream Key**: Leave empty or use a custom key.
4. Start streaming from the DJI Fly app.

### Step 3: Set Up OpenCV for Object Detection

#### 1. Using a Virtual Environment (Recommended)

This method keeps installations isolated and avoids conflicts with system packages. Run the following commands:

```bash
python3 -m venv ~/myenv  # Creates a virtual environment in your home directory
source ~/myenv/bin/activate  # Activates the virtual environment
pip install opencv-python  # Installs opencv-python within the virtual environment
```

Once you activate the virtual environment with `source ~/myenv/bin/activate`, you can run your Python scripts with `cv2` without issues. Use `deactivate` to exit the virtual environment when done.

#### 2. Install Python Dependencies

Install OpenCV:

```bash
pip install opencv-python
```

Update the RTMP stream URL in `opencv_detection.py`:

```python
cap = cv2.VideoCapture('rtmp://127.0.0.1:1935/live')
```

Run the Python script:

```bash
python opencv_detection.py
```

## (Optional) Training the Object Detection Model

For those who want to fine-tune the object detection model for custom objects, training is optional. This setup uses a pre-trained model (SSD MobileNet V3) for object detection out of the box, but you can train a custom model if needed.

To train or fine-tune for custom objects:

- **Prepare the Dataset**: Label images with tools like LabelImg and convert annotations into TFRecord format.
- **Fine-tune a Pre-trained Model**: Use a pre-trained model like SSD MobileNet V3 and fine-tune it with TensorFlow on your custom dataset.

### Training Steps

1. Download and set up the TensorFlow Object Detection API.
2. Convert the dataset into TFRecord format.
3. Fine-tune the model using a pre-trained checkpoint and configure it with your dataset.
4. Export the trained model once training is complete.

### Inference with OpenCV

After training, use the new model in `opencv_detection.py` for real-time object detection.

## Usage

1. Start the RTMP server:

   ```bash
   node server.js
   ```

2. Stream from DJI Goggles 2 using the DJI Fly app to the RTMP server.
3. Run the OpenCV script to view real-time object detection results from the RTMP live stream server.

### Example Output

Real-time detection of objects (e.g., people, cars) with bounding boxes and labels using the SSD MobileNet V3 model.

## Notes

- Ensure both devices are on the same local network.
- Adjust RTMP settings for latency and performance.
- Modify detection confidence thresholds in `opencv_detection.py` if necessary.

### Troubleshooting

- **Video Stream Issues**: Verify the RTMP server is running and the URL is correct.
- **Latency**: Optimize RTMP settings or network conditions.
- **Detection Accuracy**: Fine-tune confidence thresholds in the detection script.

### Contributing

Contributions are welcome! Fork the repository and submit pull requests.

--- 
