## Quick Start

1. Download YOLOv3 weights and config from [YOLO website](http://pjreddie.com/darknet/yolo/). Or extract the zip in the models folder
2. Convert the Darknet YOLO model to a Keras model with convert.py
```
python convert.py yolov3.cfg ./models/yolov3.weights ./models/yolov3.h5
```
3. Change the configuration based on models downloaded
```
model_path = "./models/yolov3.h5" 
# path to models that you download, must be in form of .h5

detector.setModelTypeAsYOLOv3()
detector.setModelTypeAsRetinaNet()
detector.setModelTypeAsTinyYOLOv3()
# pick one based on the modes you downloaded
```

4. Change the camera input depends on your primary or secondary camera (if you only got 1 camera input, set to 0)
```
camera = cv2.VideoCapture(1) #for secondary camera
camera = cv2.VideoCapture(0) #for primary camera
```

5. Run
```
python realtime.py
```

6. Enjoy



# Environment using:
Pipenv
