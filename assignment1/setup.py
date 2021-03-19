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

import size_reducer, video_to_frames


def setup(config) :
    
    # Create folder if not exists
    if (os.path.exists(config["frames_folder"])):
        directory = 1
    else:
        os.makedirs(config['frames_folder'])


    if (os.path.exists(config['resized_frames_folder'])):
        directory = 1
    else:
        os.makedirs(config['resized_frames_folder'])
        
        
        
        
    # To clean the folder for storing the frames 
    dir = config['frames_folder']
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    dir = config['resized_frames_folder']
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
            
            
            
    # Call to video to frames converter
    video_to_frames.converter (config["video_path"]+config["video_name"], config["frames_folder"])
    
    
    
    
    # Reducing the size of the frames.
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

    size_reducer.resizer(config["frames_folder"] ,  config["resized_frames_folder"] , dim_y,dim_x)
    
    
    
            
            
            

            
            
