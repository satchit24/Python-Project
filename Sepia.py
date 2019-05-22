# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 23:58:55 2019

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
def sepia(img):
    original_image = skimage.img_as_float(img)
    r = original_image[:, :, 0]
    g = original_image[:, :, 1]
    b = original_image[:, :, 2]
    
    tr=0.393*r+0.769*g+0.189*b
    tg=0.349*r+0.686*g+0.168*b
    tb=0.272*r+0.534*g+0.131*b
    
    merged = np.stack([tr, tg, tb], axis=2)
    blurred = filters.gaussian(merged, sigma=10, multichannel=True)
    final = np.clip(merged*1.2-blurred*0.2, 0, 1.0)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(final)
    plt.show()