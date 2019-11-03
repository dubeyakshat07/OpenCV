# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:30:04 2019

@author: Akshat.Dubey.000
"""
import numpy as np
import cv2
img=cv2.imread('F:/OpenCV/ROY_0058.JPG',cv2.IMREAD_COLOR)
img=cv2.resize(img,(1440,720))
#Here we are accessing a particular pixel of the image
px=img[100,150]
print(px)
#Now, we will change the color of the pixel
px=[255,255,255]
print(px)
#roi stands for region of image. roi is actually a sub-image of an image
roi=img[100:150,100:150]
print(roi)
roi=[0,0,255]
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()