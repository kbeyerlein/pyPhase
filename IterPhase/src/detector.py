'''
Created on Sep 5, 2013
Python Module which contains functions for image manipulation file conversion.
@author: kbeyerle
'''

import numpy as np

def centerFFTImage(arr):
    n=np.array(arr).size
    temp=np.roll(arr, int((n**0.5)/2), axis=0)
    temp=np.roll(temp, int((n**0.5)/2), axis=1)
    return temp