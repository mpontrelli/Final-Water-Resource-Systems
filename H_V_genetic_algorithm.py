# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 07:02:14 2018

@author: Marshall
"""
#Imports

import matplotlib.pyplot as plt
import numpy as np

###############################################################################
#GOAL: input required inputs
fs = 100 #sampling frequency
Filename = "C:\\Users\\Marshall\\Box Sync\\Spring_2018\\Research\\Mexico City\\19sep17\\AE0220170919181440.txt"
HV1 = np.array([])
HV2 = np.array([])
############################################################################### 
#GOAL: prepare waveforms in the time domain
#Import Waveform from txt file
waveform = np.genfromtxt(Filename, skip_header = 109)
NS = waveform[:, 0] #north south
V = waveform[:, 1] #vertical
EW = waveform[:, 2] #east west

#Subtract the mean from each waveform
xNS = NS - np.mean(NS)
xV = V - np.mean(V)
xEW = EW - np.mean(EW)

del NS
del V
del EW
del waveform
del Filename

###############################################################################
#GOAL: Prepare waveform in the frequency domain
#compute ffts
xNS = np.fft.fft(xNS)
xV = np.fft.fft(xV)
xEW = np.fft.fft(xEW)


#compute amplitude spectra
xNS = np.abs(xNS)
xV = np.abs(xV)
xEW = np.abs(xEW)
plt.plot(xNS)


###############################################################################
#GOAL: smooth the amplitude spectra
#apply 20 point moving average filter
k = [.05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05, .05,]
xNS = np.convolve(k, xNS)
xV = np.convolve(k, xV)
XEW = np.convolve(k, xEW)
plt.plot(xNS)fdgsgsdgd
###############################################################################
#GOAL: Perform the H/V

for i in range(len(xNS)):
    hv1 = xNS[i] / xV[i]
    HV1 = np.append(HV1, hv1)
#plt.plot(HV1)
    









