from skimage import io
from PIL import Image
import os, shutil
import matplotlib.pyplot as plt
import math
import cmath
import random
import numpy as np
import os
import cv2
from scipy.misc import electrocardiogram
from scipy.signal import find_peaks

from scipy.fft import fft, fftfreq
import numpy as np






def func(config,R_mean):
    time = float(len(R_mean))/config["frame_rate"]
    y = fft(R_mean)
    R_fft = fftfreq(len(R_mean))
    y_dash = []
    R_fft_dash = []
    for i in range(len(y)):
        if R_fft[i]*config["frame_rate"]>=1:
            R_fft_dash.append(R_fft[i]*config["frame_rate"])
            y_dash.append(y[i])
    ind =  y_dash.index(max(y_dash))
    bpm = float(R_fft_dash[ind]*60)
    freq = float(R_fft_dash[ind])
    
#     print("The index where amplitude is maximum is :",ind)
#     print("The frequncy corresponding to the maximum amplitude (by DFT) is :",R_fft_dash[ind])
#     print("The maximum amplitude is :",y[ind])
    
    plt.plot(R_fft_dash,y_dash,color = "red")
    plt.title("Frequency vs Amplitude Plot")
    plt.xlabel("Frequency")
    plt.ylabel("Amplitude")
    plt.show()
    return freq,bpm
