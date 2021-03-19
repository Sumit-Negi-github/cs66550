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

import setup ,loader,time_series_analysis,fft_analysis




# Configuration settings 
config={
    # You can modify these
    "video_name" : "crunches_dark.mp4",      # name of the video
    "ws_bpm" : 7,                      # This is the window size of the bpm
    "frame_rate":30,                      # downsample rate . please enter less than std_fps
    "x_px_rate":1,                        # x axis pixel rate
    "y_px_rate":1,                       # y axis pixel rate


    # Dont change these
   "video_path":"dataset/",
    "frames_folder" : "frames",     # folder to store the frames
    "std_fps" : 30 ,                    # standard frame rate of mobile camera
    "resized_frames_folder" : "r_frames",    # resized image are saved in this folder
    "ws_rm" : 2 ,                     # This is running mean window size. Actually the window size is 2 times , ahead and behind
    "crop_px": 20                      # This is to remove the boundary pixels to increase the snr . Put 0 by default
}





# It will perform setup for the program
setup.setup(config)

# Converting into matrix of pixels
R,G,B = loader.load(config)

# Time series Analysis
bpm =  time_series_analysis.func(config,R,G,B)
print("The average pulse rate (in BPM) by time series analysis ", bpm)


# Frequency and Bpm by FFT
freq, bpm  = fft_analysis.func(config,R)
print("The frequency calculated by using DFT is :",freq ," hz")
print("The pulse rate  in BPM (by DFT) is: ",bpm)

