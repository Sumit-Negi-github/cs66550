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


def normalized_pixels(R_dash , G_dash , B_dash) :
#     R = np.array(  [   float(R_dash[i] )  /   ( R_dash[i] + G_dash[i] + B_dash[i]  )     for i in range(len(R_dash))      ] )
#     G = np.array(  [   float(G_dash[i] )  /   ( R_dash[i] + G_dash[i] + B_dash[i]  )     for i in range(len(G_dash))      ] )
#     B = np.array(  [   float(B_dash[i] )  /    ( R_dash[i] + G_dash[i] + B_dash[i]  )      for i in range(len(B_dash))    ] )

    R = np.array(  [   float(R_dash[i] )  /   255     for i in range(len(R_dash))      ] )
    G = np.array(  [   float(G_dash[i] )  /   255     for i in range(len(G_dash))      ] )
    B = np.array(  [   float(B_dash[i] )  /    255      for i in range(len(B_dash))     ] )

    return R , G , B



def running_mean(matrix,ws):
        mean_run=np.array([np.mean(matrix[max(i-ws,0):min(len(matrix)-1,i+ws)]) for i in range(len(matrix))])
        return mean_run





def plot_with_peak(R):
        peaks,peak_heights = find_peaks(R,height= 0)
        peak_heights = peak_heights['peak_heights']
        R_neg = -1*R
        valleys,valleys_heights = find_peaks(R_neg,height= -1000)
        valleys_heights = valleys_heights['peak_heights']
        valleys_heights = valleys_heights*-1
        
        return peaks,peak_heights,valleys,valleys_heights


def combiner(v,vh,p,ph):
    d = []
    for i in range(len(v)):
        d.append((v[i],vh[i],'v'))
    for i in range(len(p)):
        d.append((p[i],ph[i],'p'))
    d.sort()
    return d



def bpm_counter(d,win_time):
    count = 0
    for i in range(len(d)):
        if i==0 and d[i][2]=='p':
            count += 1
        elif i == len(d)-1 and d[i][2]=='p':
            count += 1
        elif  d[i][2]=='p':
            if d[i-1][2] == 'v' and abs(d[i-1][1]-d[i][1]) < abs(d[i][1]-d[i+1][1]) :
                count += 1
    bpm = (float(count)/win_time)*60
    return bpm




def func(config,R_mean,G_mean,B_mean) :
    R_norm,G_norm,B_norm = normalized_pixels(R_mean,G_mean,B_mean)
    
    R_running_mean = running_mean(R_norm, config["ws_rm"])
    G_running_mean = running_mean(G_norm, config["ws_rm"])
    B_running_mean = running_mean(B_norm, config["ws_rm"])
    
    beat_array =[]
    win_frames = config["ws_bpm"]*config["frame_rate"]
    start = config["frame_rate"]*config["ws_bpm"]
    for i in range(start,len(R_running_mean)):
        arr = R_running_mean[ i-win_frames : i ]
        p,ph,v,vh=plot_with_peak(arr)
        d=combiner(v,vh,p,ph)
        n_beats = bpm_counter(d ,config["ws_bpm"])
        beat_array.append(n_beats)

    x = [i/config["frame_rate"] for i in range(win_frames, len(beat_array)+win_frames)]
    plt.figure(figsize=(13, 7))
    plt.plot(x,beat_array,color='red')
    plt.xlabel("seconds")
    plt.xlim(0,)
    plt.ylabel("beats per minute (bpm)")
    plt.title("Pulse Rate with sliding window of "+str(config["ws_bpm"])+" seconds"+
              "  ( frame sampling rate="+str(config["frame_rate"])+" fps )")
    plt.show() 
    
    bpm = sum(beat_array)/len(beat_array)
    return bpm
