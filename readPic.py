#Opens an image and prints all the pixel values
from PIL import Image
from os import listdir
import numpy as np

dir = "/home/tsl_student/Desktop/DenseFusion-Pytorch-1.0/datasets/linemod/Linemod_preprocessed/segnet_results/01_label/"

files = listdir(dir)

pic = np.array(Image.open(dir + files[0]))
for r in pic:
	for c in r:
		if(pic[r][c].any != 0):

			print(pic[r][c])

