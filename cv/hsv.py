# -*- coding: UTF-8 -*-
import cv2
import numpy as np

img = cv2.imread('r.jpg')
HSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #RGB 转为 HSV
H, S, V = cv2.split(HSV)    #分离 HSV 三通道
Lowerred0 = np.array([155,43,35])
Upperred0 = np.array([180,255,255])
mask1 = cv2.inRange(HSV, Lowerred0, Upperred0)
Lowerred1 = np.array([0,43,35])
Upperred1 = np.array([11,255,255])
mask2 = cv2.inRange(HSV, Lowerred1, Upperred1)    #将红色区域部分归为全白，其他区域归为全黑
Apple = mask1 +mask2
cv2.imshow("apple", Apple)
cv2.waitKey(0)