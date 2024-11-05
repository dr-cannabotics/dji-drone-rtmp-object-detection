Here’s a complete GitHub project description that includes all the components you mentioned, with additional clarity and structure for easier understanding:

---

# Real-Time Object Detection from DJI Mini 3 Pro with DJI Goggles 2, RTMP Streaming, and OpenCV

This project enables real-time object detection on a DJI Mini 3 Pro drone video feed, using **DJI Goggles 2**, **DJI Fly App**, **RTMP streaming**, and **OpenCV**. The setup involves streaming the video feed from **DJI Goggles 2** (connected to the drone) via a smartphone using the DJI Fly app, sending it to an **RTMP server**, and processing the stream with OpenCV for object detection.

---

## Project Overview

### Key Components:
1. **DJI Mini 3 Pro & DJI Goggles 2**: The drone captures and displays the video feed through the **DJI Goggles 2** connected to it.
2. **Smartphone**: The smartphone is connected to the **DJI Goggles 2** via USB-C and uses the **DJI Fly App** to stream the video feed to an **RTMP server**.
3. **Node.js RTMP Server**: The RTMP server hosted on the laptop receives the live video stream from the smartphone and relays it for processing.
4. **Python OpenCV Script**: The Python script on the laptop connects to the RTMP server to analyze the video feed in real time using object detection models.

This system can be used for various applications like monitoring, analysis, and tracking through a drone's real-time video feed.

---

## Prerequisites

Before setting up the project, ensure you have the following:

- **DJI Mini 3 Pro** and **DJI Goggles 2**
- **Smartphone** (for connecting to DJI Goggles 2 and running the DJI Fly app)
- **Laptop** with:
  - **Node.js** installed (for running the RTMP server)
  - **Python** and **OpenCV** installed (for object detection)
- **Network Connection**: Ensure that both the smartphone and laptop are connected to the same Wi-Fi network for RTMP streaming.

---

## Project Structure

```
dji-drone-rtmp-object-detection/
├── server.js               # RTMP server configuration (Node.js)
├── opencv_detection.py     # Python script for real-time object detection
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config file
├── frozen_inference_graph.pb                    # Object detection model
├── labels.txt             # COCO class labels
└── README.md              # Project documentation
```

---

## Setup Instructions

### Step 1: Set Up Node.js RTMP Server on the Laptop

1. **Clone the repository and install dependencies**:

   ```bash
   git clone <repository-url>
   cd dji-drone-rtmp-object-detection
   npm install
   ```

2. **Configure the RTMP server**:

   The `server.js` file configures an RTMP server using `node-media-server` to receive the video stream. The server will listen for incoming streams on port `1935`.

3. **Run the RTMP server**:

   In the project directory, start the RTMP server by running the following command:

   ```bash
   node server.js
   ```

   The server will now be listening for RTMP streams on `rtmp://<your-laptop-IP>:1935/live`.

### Step 2: Stream Video Feed from DJI Goggles 2 to RTMP Server

1. **Connect DJI Goggles 2 to the DJI Mini 3 Pro**.

2. **Connect the DJI Goggles 2 to your smartphone** using a USB-C cable.

3. **Install the DJI Fly app** on your smartphone, and configure it to display the video feed from the drone on the DJI Goggles 2.

4. **Install Larix Broadcaster (or another RTMP broadcasting app)** on your smartphone, and use it to stream the video feed from DJI Fly app to the RTMP server.

5. **Configure Larix Broadcaster**:
   - **URL**: `rtmp://<your-laptop-IP>:1935/live`
   - **Stream Key**: Leave empty or use a custom key.
   
6. **Start streaming** the video feed from the DJI Fly app to the RTMP server on your laptop.

### Step 3: Set Up OpenCV for Object Detection

1. **Install Python dependencies**:

   If not already installed, set up a Python environment and install the required libraries:

   ```bash
   pip install opencv-python
   ```

2. **Download Model Files**:

   Download the following files and place them in the project directory:
   - `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` (model configuration)
   - `frozen_inference_graph.pb` (pre-trained object detection model)
   - `labels.txt` (COCO class labels)

3. **Configure the Python script**:

   In `opencv_detection.py`, update the RTMP stream URL to reflect the IP address of your laptop:

   ```python
   cap = cv2.VideoCapture('rtmp://<your-laptop-IP>:1935/live')
   ```

4. **Run the Python script** to start the object detection:

   ```bash
   python opencv_detection.py
   ```

   The script will connect to the RTMP stream, perform real-time object detection on each frame, and display the results with bounding boxes and labels for detected objects.

---

## Usage

1. **Start the RTMP server**: Run `node server.js` on your laptop to start the RTMP server.
2. **Stream from DJI Goggles 2**: Use the DJI Fly app on the smartphone to display the drone’s feed and stream it via Larix Broadcaster to the RTMP server on your laptop.
3. **Run the OpenCV script**: Execute the Python script `opencv_detection.py` to view real-time object detection on the live video stream.

The detection results will be displayed with bounding boxes and labels for each detected object. Press `q` to stop the OpenCV window.

---

## Example Output

After setting up the system, you will see real-time detection of objects like people, cars, and animals from the video feed. The Python script uses the **SSD MobileNet V3 model** pre-trained on the **COCO dataset**. Detected objects are highlighted with bounding boxes, and the object class labels are shown on the video stream.

---

## Notes

- **Network Connection**: Make sure that the **smartphone and laptop** are on the same local network for seamless RTMP streaming.
- **Latency**: The video feed may have some latency depending on the network speed, and you can optimize the RTMP settings (e.g., buffer size) to reduce lag.
- **Model Accuracy**: You can fine-tune the object detection model or use other models for specific use cases.

---

## Troubleshooting

- **Error: Could not open video stream**: Ensure the RTMP server is running, and the correct RTMP URL is configured in Larix Broadcaster on the smartphone.
- **High latency**: Consider lowering the RTMP server's chunk size or increasing Wi-Fi bandwidth.
- **Low detection accuracy**: You can adjust the confidence threshold for object detection in `opencv_detection.py` by modifying:

   ```python
   classIndex, confidence, bbox = model.detect(frame, confThreshold=0.65)
   ```

---

## Contributing

Feel free to fork this repository and submit pull requests with improvements or enhancements. Contributions are welcome!

## License

This project is licensed under the MIT License.

---

### Acknowledgments

- **OpenCV** for computer vision and image processing.
- **Node-Media-Server** for RTMP stream handling.
- **Larix Broadcaster** for RTMP streaming from mobile devices.
- **DJI** for providing powerful drone and goggle technologies.

---

Happy coding and drone flying! 🎉

---

This GitHub project setup provides a clear and concise explanation of how to use DJI hardware, RTMP streaming, and OpenCV to perform real-time object detection on a live drone video feed.
