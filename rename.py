#Renames images from category_xxxx.png to xxx.png
from os import listdir, rename


depthList = listdir("depth/")
maskList = listdir("mask/")
rgbList = listdir("rgb/")


for f in depthList:
    print(f)
    newName = f.split("_")[1]
    rename("depth/" + f, "depth/" + f + "_label.png)

for f in rgbList:
    print(f)
    newName = f.split("_")[1]
    rename("rgb/" + f, "rgb/" + newName)

for f in maskList:
    print(f)
    newName = f.split("_")[1]
    rename("mask/" + f, "mask/" + newName)


