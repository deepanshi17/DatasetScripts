#Purpose: Processes images into the proper format, size and directory structure to be used by segnet
#Written by Sammy Ochoa
#Last updated 10-10-19

#Important Notes
#Set root as the folder with a MASK and a Normal folder
#It will produce a new folder called data that has the images combined and images from mask will be labeled as x-label.png and normal as x-color.png
#This will resize all pics to be 640x480 and will reformat the mask images to be grayscale 0 for background or 1 for the satellite. This produces an image that is not really visible to humans
#but is the format that is required by segnet. 



from os import listdir, mkdir
from shutil import copy
from PIL import Image


root = "/home/tsl_student/Desktop/S_Rotate/"


masked = root + "Mask/"
color = root + "Normal/"
data = "data/"


maskedImages = listdir(masked)

try:
    mkdir(root + data)

except Exception as e:
    print(e)


x = 0
for i in maskedImages:
    #copy(masked + i, root + data + str(x) + "-label.png")
    im = Image.open(masked+i).convert('L')
    im = im.resize((640,480), Image.ANTIALIAS)
    for r in range(640):
        for c in range(480):
                if im.getpixel((r,c)) > 8:
                        im.putpixel((r,c), 0)

                else:
                        im.putpixel((r,c),1)



    im.save(root+data+str(x) + "-label.png")


    x+=1
    print(x)


colorImages = listdir(color)
x = 0
for i in colorImages:
    #copy(color + i, root + data + str(x) + "-color.png")

    im = Image.open(color + i)
    im = im.resize((640, 480), Image.ANTIALIAS)
    im.save(root + data + str(x) + "-color.png")
    x+=1
    print(x)



print("Done")



