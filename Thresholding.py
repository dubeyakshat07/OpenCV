# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 19:51:08 2019

@author: Akshat.Dubey.000
"""
import numpy as np
import cv2
img=cv2.imread("F:/OpenCV/Capture.JPG",1)
retval, threshold=cv2.threshold(img,15,150,cv2.THRESH_BINARY)
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
gauss=cv2.adaptiveThreshold(grayscaled, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
retval2,otsu=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("original image",img)
cv2.imshow("threshold",threshold)
cv2.imshow("Grayscaled",grayscaled)
cv2.imshow("Grayscaled threshold",threshold2)
cv2.imshow("Adaptive threshold",gauss)
cv2.imshow("Otsu",otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
