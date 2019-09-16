from imageai.Detection import ObjectDetection
from imageai.Detection import VideoObjectDetection

detector = ObjectDetection()

model_path = "./models/yolov3.h5"
input_path = "./input/test2.jpg"
output_path = "./output/newimage.jpg"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()
detection = detector.detectObjectsFromImage(input_image=input_path, output_image_path=output_path)

for eachItem in detection:
    print(eachItem["name"], " : ", eachItem["percentage_probability"])
