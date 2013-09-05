#!/usr/bin/env python

# test program to phase an object with Error Reduction

import numpy as np
import sys
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import Image

sys.path.append('../src/')
import iterPhase as ip
import detector as det


realrho=[[0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0.5,0,0,0,0,0,0,0,0],
         [0,0.5,1,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,0],
         [0,0,0,0,0,0,0,0,0,0,0,0]]

support=[[1.,1.,1.,0.,0.,1.,1.,1.],
         [1.,1.,0.,0.,0.,0.,1.,1.],
         [1.,0.,0.,0.,0.,0.,0.,1.],
         [0.,0.,0.,0.,0.,0.,0.,0.],
         [0.,0.,0.,0.,0.,0.,0.,0.],
         [1.,0.,0.,0.,0.,0.,0.,1.],
         [1.,1.,0.,0.,0.,0.,1.,1.],
         [1.,1.,1.,0.,0.,1.,1.,1.]]

print "Real Rho"
plt.imshow(realrho, interpolation='nearest')
plt.show()

f=np.fft.fft2(realrho)

Iobs= np.ndarray.conjugate(f)*f

print "Observed Intensity"
plt.imshow(det.centerFFTImage(Iobs.real), interpolation='nearest')
plt.show()

mod = np.sqrt(Iobs)
mod = mod.real

print "Autocorrelation"
# plt.imshow(centerImage(np.absolute(np.fft.ifft2(Iobs))), interpolation = "nearest")
# plt.show()
autocorr=ip.autoCorrelation(Iobs)
support= ip.makePositiveMask(autocorr)
plt.imshow(det.centerFFTImage(support), interpolation = "nearest")
plt.show()

f0=np.vectorize(complex)(np.sqrt(Iobs),[[np.random.random()*2*np.pi for i in range(len(j))] for j in Iobs] )

# print f0

myRho = np.fft.ifft2(f0)
print "Initial Rho"
plt.imshow(det.centerFFTImage(np.absolute(myRho)),interpolation = "nearest")
plt.show()

for i in range(10000):
    myRho = ip.ErrReduct(myRho, mod, support)
    # myRho = ip.HIO(myRho, mod, support)
    if (i%1000 == 0):
        plt.imshow(det.centerFFTImage(np.absolute(myRho)),interpolation = "nearest")
        plt.show()