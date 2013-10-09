'''
Created on Sep 5, 2013
Python Module which contains functions for image manipulation file conversion.
@author: kbeyerle
'''

import numpy as np

def centerFFTImage(arr):
    temp=np.roll(arr, int(np.array(arr).shape[0]/2), axis=0)
    temp=np.roll(temp, int(np.array(arr).shape[1]/2), axis=1)
    return temp