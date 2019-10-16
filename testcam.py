import cv2

camera = cv2.VideoCapture(1)

while True:
    return_value, image = camera.read()
    cv2.imwrite("./test.jpg", image)
    cv2.imshow("detected", image)
