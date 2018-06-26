# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 12:14:52 2018

@author: sruthi
"""

import numpy as np
import cv2
import os

img= cv2.imread(r'C:\Users\sruth\OneDrive\Desktop\simplilearn\Opencv\waterbottle.jpg',cv2.IMREAD_COLOR)
px=img[77,5]
print(px)
img[77,5]=[255,0,0]
print(px)

bottle_cap=img[60:180,10:180]
img[0:120,0:170]=bottle_cap

#Region of an image
img[100:150,100:150]=[0,255,0]
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()