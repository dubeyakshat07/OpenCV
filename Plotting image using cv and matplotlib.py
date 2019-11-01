# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
print(cv2.__version__)
img=cv2.imread('F:\ROY_0058.JPG',1)
print(img)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('Akshat.jpg',img)
from matplotlib import pyplot as plt
img=cv2.imread('F:\ROY_0058.JPG',0)
plt.imshow(img,cmap='gray',interpolation='bicubic')
