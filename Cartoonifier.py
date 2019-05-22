# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 22:01:01 2019

@author: Satchit
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

def getSobelEdge(img , size=3):
    sx = cv2.Sobel(img, cv2.CV_64F,1,0,ksize=size)
    sy = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=size)
    edges = np.sqrt(np.square(sx) + np.square(sy))
    edges = np.floor((edges / (np.max(edges)+0.001)) * 100 ).astype(np.uint8)
    return edges

def cartoon(img):
    MEDIAN_BLUR_FILTER_SIZE = 5
    LAPLACIAN_FILTER_SIZE = 5
    EDGES_THRESHOLD = 10
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    imgray = cv2.medianBlur(imgray , MEDIAN_BLUR_FILTER_SIZE)
    edges = getSobelEdge(imgray , -1)
    
    _ , mask = cv2.threshold(edges , EDGES_THRESHOLD , 255 , cv2.THRESH_BINARY_INV )
    height , width, _ = img.shape
    img = cv2.resize(img,(width//2, height//2), interpolation = cv2.INTER_LINEAR)
    tmp = img
    REPETITIONS = 17
    ksize = 9
    sigmaColor = 9
    sigmaSpace = 7
    
    for i in range(REPETITIONS):
        tmp = cv2.bilateralFilter(img, ksize, sigmaColor , sigmaSpace)
        img = cv2.bilateralFilter(tmp , ksize, sigmaColor , sigmaSpace)
    
    img = cv2.resize(img, (width, height))
    newimg = np.zeros(img.shape).astype(np.uint8)
    print(newimg.shape)
    for i in range(3):
        newimg[:,:,i] = cv2.bitwise_and(img[:,:,i],mask)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(newimg)
    plt.show()