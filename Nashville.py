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
def nash(img):
    original_image = skimage.img_as_float(img)
    r = original_image[:, :, 0]
    g = original_image[:, :, 1]
    b = original_image[:, :, 2]
        
    b_more = np.clip(b + 0.03, 0, 1.0)
    r_more = np.clip(r + 0.03, 0, 1.0)
    g_more = np.clip(g - 0.03, 0, 1.0)
    
    merged = np.stack([r_more, g_more, b_more], axis=2)
    blurred = filters.gaussian(merged, sigma=10, multichannel=True)
    final = np.clip(merged*1.8 - blurred*0.2, 0, 1.0)
    b = final[:, :, 2]
    b_adjusted = channel_adjust(b, [0, 0.05, 0.1, 0.2, 0.3,
        0.5, 0.7, 0.8, 0.9,
        0.95, 1.0])
    final[:, :, 2] = b_adjusted
    plt.xticks([])
    plt.yticks([])
    plt.imshow(final)
    plt.show()