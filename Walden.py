# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 03:17:58 2019

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
def wald(img):
    original_image = skimage.img_as_float(img)
    r = original_image[:, :, 0]
    g = original_image[:, :, 1]
    b = original_image[:, :, 2]
    
    r_boost = channel_adjust(r, [0, 0.6,0.8, 1])
    
    g_boost = channel_adjust(g, [0,0.6,0.8,1])
    
    b_boost = channel_adjust(b, [0, 0.6,0.8, 1])    
    b_more = np.clip(b + 0.2, 0, 1.0)
    r_more = np.clip(r + 0.1, 0, 1.0)
    g_more = np.clip(g + 0.07, 0, 1.0)
    
    merged = np.stack([r,g_more,b_boost], axis=2)
    blurred = filters.gaussian(merged, sigma=10, multichannel=True)
    final = np.clip(merged*1.1 - blurred*0.2, 0, 1.0)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(final)
    plt.show()