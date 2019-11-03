# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 20:02:49 2019

@author: Akshat.Dubey.000
"""

import numpy as np
import cv2
img=cv2.imread('F:\OpenCV\ROY_0058.JPG',1)
img = cv2.resize(img, (1440,720))
print(img)
cv2.line(img,(0,0),(150,150),(255,0,0))
cv2.rectangle(img,(15,25),(200,150),5)
cv2.circle(img,(100,63),55,(0,0,255),-1)
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'OpenCV is awesome',(0,130),font,5,(255,0,255),5)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()