# Code to convert video to frames and stored frames in frames folder


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




def converter ( video_name , frames_folder ) :
         cap = cv2.VideoCapture(video_name)

         image_num = 0
         while (cap.isOpened()):
                  ret,frame=cap.read()
                  if ret == False:
                           break
                  cv2.imwrite(frames_folder+"/frame%d.jpg"%image_num,frame)
                  image_num += 1
         print("video is  successfully converted into frames")
