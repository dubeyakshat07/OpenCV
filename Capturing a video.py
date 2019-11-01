# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 21:05:47 2019

@author: Akshat.Dubey.000
"""

import numpy as np
import cv2
cap=cv2.VideoCapture(0)
fourcc=cv2.VideoWriter_fourcc(*'XVID')
out=cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))
while(cap.isOpened()):
    ret, frame=cap.read()
    if ret==True:
        
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
            break
    else:
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()
            
            

    