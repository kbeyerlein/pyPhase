#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 15:13:36 2017

@author: beyerlein
"""

import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import detector as det

def makeThresholdMask(arr, val):
    return np.array([1 if (np.abs(a) > val) else 0 for a in arr])

    