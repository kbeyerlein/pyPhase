'''
Created on Sep 5, 2013

Python Module which contains algorithms for iterative phase retrieval 

@author: kbeyerle
'''

import numpy as np
import matplotlib.pyplot as plt
import detector as det

def zeroPhase(rho):
    return np.absolute(rho)

def makePositive(rho):
    posRho=np.array([[j if j>0 else 0 for j in i] for i in rho])
    return posRho

def modulusProjection(rho, mod):
    f= np.fft.fft2(np.array(rho))
    f=mod.real*np.exp(1j*np.angle(f))
    rho= np.fft.ifft2(f)
    return rho

def supportProjection(rho, support):
    return np.array(rho)*np.array(support)

def makeReal(arr):
    return np.array([[np.absolute(i) if i.real >=-0.000001 else -np.absolute(i) for i in row] for row in arr])

def makePositiveMask(arr):
    return np.array([[1 if i.real > 0.0000000001 else 0 for i in row] for row in arr])

def invertMask(mask):
    return np.ones(np.shape(mask))-np.array(mask)

def autoCorrelation(arr):
    return np.absolute(np.fft.ifft2(np.array(arr)))

def HIO(rho, mod, support, b=0.9, positive=False, debug=False):
    if (debug):
        print "support"
        plt.imshow(det.centerFFTImage(support), interpolation='nearest')
        plt.colorbar()
        plt.show()
    modRho=modulusProjection(rho, mod)
    if (positive):
        support = makePositiveMask(modRho*np.array(support))
    suppModRho=modRho*np.array(support)
    hiodiff=(rho-b*modRho)*invertMask(support)
    if (debug):
        print "suppModRho"
        plt.imshow(det.centerFFTImage(suppModRho.real), interpolation='nearest')
        plt.colorbar()
        plt.show()
        print "hiodiff"
        plt.imshow(det.centerFFTImage(hiodiff.real), interpolation='nearest')
        plt.colorbar()
        plt.show()
        print "modRho"
        plt.imshow(det.centerFFTImage(modRho.real), interpolation='nearest')
        plt.colorbar()
        plt.show()
        print "rho"
        plt.imshow(det.centerFFTImage(rho.real), interpolation='nearest')
        plt.colorbar()
        plt.show()
        print "invsupport"
        plt.imshow(det.centerFFTImage(invertMask(support)), interpolation='nearest')
        plt.colorbar()
        plt.show()
        
    return  suppModRho+hiodiff

def ErrReduct(rho, modulus, support, positive=False):
    myRho=modulusProjection(rho,modulus)
    if (positive):
        support=makePositiveMask(myRho*np.array(support))
    return supportProjection(myRho, support)