
import math
import cv2
import pickle
import numpy as np

espacio = []
with open('espacios.pkl', 'rb') as file:
    espacio = pickle.load(file)

video = cv2.VideoCapture('v1.mp4')

while True:
    check, img = video.read()
    imgBN = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    imgTH = cv2.adaptiveThreshold(imgBN, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 16)
    imgMedian = cv2.medianBlur(imgTH, 5)
    kernel = np.ones((5,5), np.int8)
    imgDil = cv2.dilate(imgMedian, kernel)
    cuadros_azules = 0
    for x, y, w, h in espacio:
        espacio = imgDil[y:h, x:w]
        count = cv2.countNonZero(espacio)
        if count > 5:
            cuadros_azules = cuadros_azules + 1

    cv2.putText(img, "personas: " + str(math.floor(cuadros_azules/15 - 8)), (50,50), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,0), 2)
    cv2.imshow('video', img)
    cv2.waitKey(10)