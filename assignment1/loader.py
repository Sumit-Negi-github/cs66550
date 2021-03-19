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

 # I will trim 5 second video from starting and end as it may contain more noise
 


def count_frames(config):
         count = 0
         for  frame_name in os.listdir( config["frames_folder"] ) : count+=1
         return count

def jpg_to_matrix(config,no_frames , factor, xpr, ypr,offset):
         

    dimension = io.imread(config["frames_folder"]+"/frame0.jpg")
    n_cols = dimension.shape[1]
    n_rows = dimension.shape[0]

    dim_x,dim_y =0,0
    if n_rows > n_cols:
        factor = float(n_rows)/n_cols
        dim_x = int(factor*100)
        dim_y = 100
    else:
        factor = float(n_cols)/n_rows
        dim_y = int(factor*100)
        dim_x = 100


         
    intensity_matrix_R,intensity_matrix_G,intensity_matrix_B =[],[],[]
    frame_cut = int(config["std_fps"] * 5)
    factor = int(factor)
    a = frame_cut 
    b = int(no_frames-frame_cut)
    c= int(factor)
    
    
    for frame_num in range(frame_cut,no_frames-frame_cut,factor):
        name = io.imread(config["resized_frames_folder"]+"/frame"+str(frame_num)+".jpg")
        R = np.array([   name[x][y][0]    for x in range(0+offset,dim_x-offset,xpr)   for y in range(0+offset,dim_y-offset,ypr)      ])
        G = np.array([   name[x][y][1]    for x in range(0+offset,dim_x-offset,xpr)   for y in range(0+offset,dim_y-offset,ypr)      ])
        B = np.array([   name[x][y][2]    for x in range(0+offset,dim_x-offset,xpr)   for y in range(0+offset,dim_y-offset,ypr)      ])
   
        intensity_matrix_R.append(R) 
        intensity_matrix_G.append(G)
        intensity_matrix_B.append(B)
    return intensity_matrix_R,intensity_matrix_G,intensity_matrix_B


def mean_component_value(matrix):
         mean_array = [ np.mean(matrix[i]) for i in range(len(matrix)) ] 
         return mean_array


def load(config):
         no_frames = count_frames(config)
         print("Number of frames are  :",no_frames)



         R,G,B = jpg_to_matrix(config,no_frames, int(config["std_fps"]//config["frame_rate"]),config["x_px_rate"],config["y_px_rate"],config["crop_px"])


         R_mean = mean_component_value(R)
         G_mean = mean_component_value(G)
         B_mean = mean_component_value(B)



         return R_mean,G_mean,B_mean
         
         
         
