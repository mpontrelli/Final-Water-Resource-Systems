# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 12:58:20 2018

@author: mpontr01
"""

import scipy.signal as sig
import matplotlib.pyplot as plt

#def Butterworth(waveform):
b, a = sig.butter(4, .5)

y = sig.filtfilt(b, a, waveE)
plt.plot(y)
    