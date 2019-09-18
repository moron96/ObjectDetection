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
while True:
    return_value, image = camera.read()
    cv2.imwrite(input_path, image)
    detection = detector.detectObjectsFromImage(input_image=input_path,
                                                output_image_path=output_path)
    for eachItem in detection:
        if eachItem["percentage_probability"] < 60:
            color = (92, 92, 247)
        elif eachItem["percentage_probability"] < 85:
            color = (92, 247, 240)
        else:
            color = (129, 207, 104)
        cv2.rectangle(image,
                      (eachItem["box_points"][0], eachItem["box_points"][1]),
                      (eachItem["box_points"][2], eachItem["box_points"][3]),
                      color,
                      2)
        cv2.putText(image,
                    eachItem["name"] + " : " + str(eachItem["percentage_probability"]),
                    (eachItem["box_points"][0], eachItem["box_points"][1]-5),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    color,
                    1,
                    cv2.LINE_AA)
        print(eachItem["name"], " : ", eachItem["percentage_probability"])
    print("\n\n")

    cv2.imshow("detected", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
# camera.release()
# cv2.destroyAllWindows()
