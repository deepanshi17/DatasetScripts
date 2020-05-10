#Renames the blender generated masks to xxxx_label.png to work with semantic segmentation results
from os import listdir, rename


root = "/home/tsl_student/Desktop/Fresh-Fusion/DenseFusion-Pytorch-1.0/datasets/serpent/serpentProcessed/segnet_results/01_label/"

files = listdir(root)



for f in files:
    print(f)
    name = f.split(".")[0]
    newNmame = name + "_label.png"
    rename(root + f, root+ newNmame)




