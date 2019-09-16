## Quick Start

1. Download YOLOv3 weights from [YOLO website](http://pjreddie.com/darknet/yolo/). Or extract the zip in the models folder
2. Convert the Darknet YOLO model to a Keras model with convert.py
```
python convert.py yolov3.cfg ./models/yolov3.weights ./models/yolov3.h5
```
3. Run YOLO detector.py
