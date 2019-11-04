# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 20:47:18 2019

@author: Akshat.Dubey.000
"""
import numpy as np
import cv2
cap=cv2.VideoCapture(0)
while True:
    _,frame=cap.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red=np.array([150,150,50])
    upper_red=np.array([180,255,150])
    mask=cv2.inRange(hsv,lower_yellow,upper_yellow)
    res=cv2.bitwise_and(frame,frame,mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k=cv2.waitKey(5) & 0xFF
    if k==27:
        break
cv2.destroyAllWindows()
cap.release()
    