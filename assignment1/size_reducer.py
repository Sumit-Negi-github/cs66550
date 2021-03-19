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



# Code to Resize the original image 
def resizer (frames_folder , resized_folder, dim_y, dim_x ):
         for frame_num in os.listdir(frames_folder ):
                  im = Image.open(frames_folder  + "/" + frame_num)
                  im1=im.resize( (dim_y,dim_x) )
                  im1.save(resized_folder  + "/" + frame_num)
         print("size reduced successfully done.")

