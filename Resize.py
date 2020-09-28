import os
import cv2

for file_name in os.listdir(r"C:\Users\DELL\Desktop\TestPictures11"):
    if file_name.split(".")[-1].lower() in {"jpg", "png"}:
        img = cv2.imread("C:/Users/DELL/Desktop/TestPictures11/" + file_name)
        img = cv2.resize(img, (156, 156))
        path = r"C:\Users\DELL\Desktop\TestPictures12\ " + file_name
        print(path)
        cv2.imwrite(path, img)

    cv2.waitKey(0)
