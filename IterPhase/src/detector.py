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

#This does not do a good job of cutting off the outside intensity, 
# Consider some suggestions in: http://stackoverflow.com/questions/2777907/python-numpy-roll-with-padding
def recenterImage(arr, currCenter):
    newCenter=np.array([np.array(arr).shape[0]/2, np.array(arr).shape[1]/2])
    delta=newCenter-np.array(currCenter)
    arr2=np.roll(np.roll(arr, delta[0], axis=0), delta[1], axis=1)
    return arr2