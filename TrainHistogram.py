import os
import cv2

for file_name in os.listdir(r"C:\Users\DELL\Desktop\TestPictures"):
    if file_name.split(".")[-1].lower() in {"jpg", "png"}:
        img = cv2.imread("C:/Users/DELL/Desktop/TestPictures/" + file_name)
        print(img)
        #cv2.imshow('Color input image', img)
        img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        # equalize the histogram of the Y channel
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])

        # convert the YUV image back to RGB format
        img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

        #cv2.imshow('Color input image', img)
        #cv2.imshow('Histogram equalized', img_output)
        path = r"C:\Users\DELL\Desktop\TestPictures11\ " + file_name
        print(path)
        cv2.imwrite(path, img_output)

    cv2.waitKey(0)
