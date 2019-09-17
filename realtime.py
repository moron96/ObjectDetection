import cv2
import time
from imageai.Detection import ObjectDetection
from imageai.Detection import VideoObjectDetection

detector = ObjectDetection()
# videodetector = VideoObjectDetection()

model_path = "./models/yolov3.h5"
input_path = "./input/opencv.jpg"
output_path = "./output/processed.jpg"

detector.setModelTypeAsYOLOv3()
detector.setModelPath(model_path)
detector.loadModel()

# videodetector.setModelTypeAsYOLOv3()
# videodetector.setModelPath(model_path)
# videodetector.loadModel()


# def perframe(counting, output_objects_array, output_objects_count, detected_copy):
#     cv2.imshow('frame', detected_copy)
#     print(counting)
#     print(output_objects_array)
#     print(output_objects_count)


camera = cv2.VideoCapture(1)
i = 0;
start = time.time()
while True:
    return_value, image = camera.read()
    if image is not None:
        cv2.imwrite(input_path, image)
        detection = detector.detectObjectsFromImage(input_image=input_path,
                                                    output_image_path="./output/processed"+str(i)+".jpg")
        # videodetection = videodetector.detectObjectsFromVideo(camera_input=camera,
        #                                                       save_detected_video=False,
        #                                                       frames_per_second=60,
        #                                                       frame_detection_interval=1,
        #                                                       return_detected_frame=True,
        #                                                       per_frame_function=perframe)
        if i-2 > 0:
            img_file = r"./output/processed"+str(i-2)+".jpg"
            img = cv2.imread(img_file)
            cv2.imshow('frame', image)
        i += 1

        for eachItem in detection:
            print(eachItem["name"], " : ", eachItem["percentage_probability"])
            print("\n\n")
