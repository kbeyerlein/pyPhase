'''
Created on Sep 5, 2013

Python Module which contains algorithms for iterative phase retrieval 

@author: kbeyerle
'''
import sys

# Need to change this for each computer
#sys.path.append('/home/kbeyerle/git/myPyFun/MyFuncts/src/')
sys.path.append('/home/ken/git/myPyFun/MyFuncts/src/')
import myMath

import numpy as np
import matplotlib.pyplot as plt
import detector as det

def zeroPhase(rho):
    return np.absolute(rho)

def makePositive(rho):
    posRho=np.array([[j if j>0 else 0 for j in i] for i in rho])
    return posRho

def makeReal(arr):
    return np.array([[np.absolute(i) if i.real >=-0.000001 else -np.absolute(i) for i in row] for row in arr])

def makeThresholdMask(arr, val):
    return np.array([[1 if i.real > val else 0 for i in row] for row in arr])

def makePositiveMask(arr):
    return makeThresholdMask(arr, 0.0000001)

def invertMask(mask):
    return np.ones(np.shape(mask))-np.array(mask)

def modulusProjection(rho, mod, mask):
    f= np.fft.fft2(np.array(rho))
    invmask=invertMask(mask)
    f=(mod.real*np.exp(1j*np.angle(f)))*mask+f*invmask
    """print "f"
    plt.imshow(det.centerFFTImage(np.absolute(f)), interpolation='nearest')
    plt.colorbar()
    plt.show()
    """
    rho= np.fft.ifft2(f)
    return rho

def supportProjection(rho, support):
    return np.array(rho)*np.array(support)

def autoCorrelation(arr):
    return np.absolute(np.fft.ifft2(np.array(arr)))

def HIO(rho, mod, support, mask, b=0.9, positive=False, debug=False):
    if (debug):
        print "support"
        plt.imshow(det.centerFFTImage(support), interpolation='nearest')
        plt.colorbar()
        plt.show()
    modRho=modulusProjection(rho, mod, mask)
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

def ErrReduct(rho, modulus, support, mask, positive=False):
    myRho=modulusProjection(rho,modulus, mask)
    if (positive):
        support=makePositiveMask(myRho*np.array(support))
    return supportProjection(myRho, support)

def ShrinkWrap(rho, support, sigma, threshold=0.2, sigmaMin=0):
    gaussian=myMath.TwoDNormalArray(rho.shape, [int(rho.shape[0]/2),int(rho.shape[1]/2)], [sigma,sigma])
    blurred=np.fft.ifft2(np.fft.fft2(rho)*np.absolute(np.fft.fft2(gaussian)))
    blurred=np.absolute(blurred)
    newSupport=makeThresholdMask(blurred, threshold*np.amax(blurred))
    sigma*=0.99
    if (sigma< sigmaMin): sigma=sigmaMin
    return newSupport, sigma