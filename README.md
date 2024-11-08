
---

# Real-Time Object Detection and Live Streaming with DJI Mini 3 Pro over RTMP

This project enables real-time object detection with live streaming from a DJI Mini 3 Pro drone using DJI Goggles 2, designed for applications that require immediate analysis of aerial footage. The video feed is streamed from the DJI Fly app to a Node.js RTMP server, where OpenCV processes each frame for object detection. Leveraging either pre-trained or custom-trained models, the system detects and highlights objects within the video feed in real time. This setup is ideal for applications in surveillance, environmental monitoring, and other scenarios where live aerial object detection and streaming are critical.
Forked out of -> https://github.com/zafarRehan/object_detection_COCO
## Components

- **DJI Mini 3 Pro & DJI Goggles 2**: Capture and display video feed.
- **Smartphone**: Streams video via the DJI Fly app to an RTMP server.
- **Node.js RTMP Server**: Manages the video stream.
- **OpenCV**: Processes video feed for object detection.

## Project Structure

```
dji-drone-rtmp-object-detection/
├── server.js                                     # RTMP server configuration
├── opencv_detection_rtmp.py                      # Object detection rtmp script
├── opencv_detection_image.py                     # Object detection image script
├── opencv_detection_rtmp.py                      # Object detection video script
├── ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt  # Model config
├── frozen_inference_graph.pb                     # Detection model
├── labels.txt                                    # COCO class labels
└── README.md                                     # Documentation
```

---

## Setup Instructions

### 1. Install Node.js and RTMP Server

1. **Install Node.js**: Check versions to confirm the installation.
   ```bash
   node -v
   npm -v
   ```

2. **Clone Repository and Install Dependencies**
   ```bash
   git clone https://github.com/dr-cannabotics/dji-drone-rtmp-object-detection/
   cd dji-drone-rtmp-object-detection
   npm install node-media-server
   ```

3. **Start RTMP Server**
   ```bash
   node server.js
   ```
   The server will start listening at `rtmp://127.0.0.1:1935/live`.

### 2. Stream Video to RTMP Server

1. Connect DJI Goggles 2 to the drone and smartphone.
2. In the DJI Fly app, configure the stream to `rtmp://127.0.0.1:1935/live`.

### 3. Verify RTMP Stream with VLC

1. Open VLC and go to **Media > Open Network Stream**.
2. Enter the stream URL: `rtmp://127.0.0.1:1935/live`.
3. Click **Play** to confirm the live video feed is working.

### 4. Set Up OpenCV for Object Detection

#### Using a Python Virtual Environment (recommended)

```bash
python3 -m venv ~/myenv
source ~/myenv/bin/activate
pip install opencv-python
```

In `opencv_detection.py`, update the video capture source to the RTMP stream:

```python
cap = cv2.VideoCapture('rtmp://127.0.0.1:1935/live')
```

Run the detection script:

```bash
python opencv_detection.py
```

---

## Optional: Training a Custom Object Detection Model

If you want to detect specific objects, you can train a custom model. Here’s how:

### 1. Data Collection and Annotation

1. **Collect Images**: Gather images of the objects you want to detect. Aim for a diverse set of images with various backgrounds and lighting conditions.
2. **Annotate Images**: Use tools like [LabelImg](https://github.com/tzutalin/labelImg) or [Roboflow](https://roboflow.com/) to label objects in each image. Save annotations in **Pascal VOC XML** or **COCO JSON** format, as required by your training pipeline.

### 2. Set Up the Training Environment

1. **Install TensorFlow**: For object detection, use TensorFlow 2.x.
   ```bash
   pip install tensorflow
   ```

2. **Install TensorFlow Object Detection API**:
   - Clone the TensorFlow models repository:
     ```bash
     git clone https://github.com/tensorflow/models.git
     ```
   - Install the Object Detection API and its dependencies:
     ```bash
     cd models/research
     protoc object_detection/protos/*.proto --python_out=.
     pip install .
     ```

### 3. Prepare the Dataset

Convert your dataset to TFRecord format, which is required for training in TensorFlow.

1. **Convert Annotations**:
   Use a script (like `xml_to_tfrecord.py` for VOC or `json_to_tfrecord.py` for COCO) to generate `.tfrecord` files.

2. **Update `label_map.pbtxt`**:
   Define your class labels in `label_map.pbtxt`:
   ```text
   item {
     id: 1
     name: 'object_name'
   }
   ```
   Repeat for each object you want to detect.

### 4. Configure Model for Training

1. Choose a pre-trained model from TensorFlow's [Model Zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md) (e.g., SSD MobileNet V3).
2. Download the model and configuration file, then modify the configuration to point to your dataset, `label_map.pbtxt`, and adjust other parameters (e.g., batch size, learning rate).

### 5. Train the Model

Run the training script with your configuration file:

```bash
python models/research/object_detection/model_main_tf2.py \
    --pipeline_config_path=path/to/pipeline.config \
    --model_dir=path/to/output \
    --alsologtostderr
```

Monitor the training process, and when it reaches a satisfactory accuracy, export the model:

```bash
python models/research/object_detection/exporter_main_v2.py \
    --input_type image_tensor \
    --pipeline_config_path path/to/pipeline.config \
    --trained_checkpoint_dir path/to/output/checkpoint \
    --output_directory path/to/exported_model
```

### 6. Integrate the Custom Model

1. Replace `frozen_inference_graph.pb` and `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` with the new model files.
2. Update `opencv_detection.py` to load your custom model:

   ```python
   net = cv2.dnn.readNet('path/to/exported_model/frozen_inference_graph.pb', 
                         'path/to/exported_model/label_map.pbtxt')
   ```

---

## Usage

1. **Start the RTMP Server**
   ```bash
   node server.js
   ```

2. **Stream Video from DJI Goggles 2**
   - Set up the stream in DJI Fly app.
   - Verify the RTMP stream in VLC (see instructions above).

3. **Run the OpenCV Script for Object Detection**
   ```bash
   python opencv_detection.py
   ```

You should see object detection in action on the video feed.

---

## Tips and Troubleshooting

- **Network Setup**: Ensure both your smartphone and server are connected to the same Wi-Fi network for stable streaming.
- **RTMP Configuration**: Adjust `server.js` settings (e.g., buffer size) for optimized performance if needed.
- **Confidence Thresholds**: Fine-tune detection thresholds in `opencv_detection.py` to balance detection accuracy and performance.

---


Happy flying, hacking, and object-detecting! 🛸
