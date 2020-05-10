#Converts masks that are in 0 and 1 format to 0 and 255 format

from os import listdir, mkdir
from shutil import copy
from PIL import Image


root = "/home/tsl_student/Desktop/DenseFusion-Pytorch-1.0/datasets/linemod/Linemod_preprocessed/data/01/"
data = "newMasks/"

masked = root + "mask/"


maskedImages = listdir(masked)
for img in maskedImages:
    print(img)



try:
    mkdir(root + data)

except Exception as e:
    print(e)


x = 1
for i in maskedImages:
    #copy(masked + i, root + data + str(x) + "-label.png")
    im = Image.open(masked+i).convert('L')
    for r in range(640):
        for c in range(480):
                if im.getpixel((r,c)) == 1:
                        im.putpixel((r,c), 255)

                else:
                        im.putpixel((r,c),0)


    im.convert("RGB")
    im.save(root+data+i)


    x+=1
    print(x)

