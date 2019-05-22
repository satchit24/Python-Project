# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 02:20:14 2019

@author: Satchit
"""


import numpy as np
import skimage
from skimage import io, filters
from skimage.color import rgb2hsv
import matplotlib.pyplot as plt
def channel_adjust(channel, values):
    orig_size = channel.shape
    flat_channel = channel.flatten()
    adjusted = np.interp(flat_channel, np.linspace(0, 1, len(values)), values)
    return adjusted.reshape(orig_size)
def neg(img):
    original_image = skimage.img_as_float(img)
    r = original_image[:, :, 0]
    g = original_image[:, :, 1]
    b = original_image[:, :, 2]
    
    y = 0.2125*r + 0.7154*g + 0.0721*b
    
    merged = np.stack([1-r,1-g,1-b], axis=2)
    blurred = filters.gaussian(merged, sigma=10, multichannel=True)
    final = np.clip(merged*1.2-blurred*0.2, 0, 1.0)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(final)
    plt.show()