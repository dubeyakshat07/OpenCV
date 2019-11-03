# -*- coding: utf-8 -*-

"""
Created on Sun Nov  3 20:30:04 2019

@author: Akshat.Dubey.000
"""
import numpy as np
import cv2
img1=cv2.imread('F:/OpenCV/ROY_0058.JPG',cv2.IMREAD_COLOR)
img=cv2.resize(img1,(821,785))
img2=cv2.imread('F:/OpenCV/Capture.JPG',1)
add=cv2.add(img,img2)#This version of add will add all the pixel values
weighted=cv2.addWeighted(img,0.25,img2,0.75,0)
img3=img+img2
cv2.imshow("Image1",img3)
cv2.imshow("Image2",add)
cv2.imshow("Image3",weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
