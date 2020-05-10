#Generates the gt.yml from the truth data and masks generated in blender.

import yaml
import matplotlib.pyplot as plt
from os import listdir




def get_bound_box(img_name):
    min_x = 2**20
    min_y = 2 ** 20
    max_x = -1
    max_y = -1

    found_sat = False
    img = plt.imread(img_name)
    for y in range(len(img)):
        sat_in_column = False

        for x in range(len(img[0])):
            if not img[y][x][0] == 0:
                found_sat = True
                sat_in_column = True
                if x < min_x:
                    min_x = x
                if y <min_y:
                    min_y = y
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y

        if found_sat and not sat_in_column:
            return[min_x, min_y, max_x - min_x, max_y - min_y]

    return [min_x, min_y, max_x - min_x, max_y - min_y]










dataFile = "/home/tsl_student/Desktop/10000img/1/all.txt"   #Path to truth data
maskDirectory = "/home/tsl_student/Desktop/10000img/1/maskDense"  #Path to the mask directory in black and white format
outputFile = "/home/tsl_student/Desktop/gt.yml"


data = open(dataFile, 'r')
masks = sorted(listdir(maskDirectory))
print(masks)
line = True
counter = 1
maskCounter = 0

dataset = []
gtDict = {}
while(line):
    frameData = ""

    for x in range(3):

        line = data.readline()
        frameData += line

    frameData = frameData.replace("Matrix", "")
    frameData = frameData.replace("Vector","")
    frameData = frameData.replace("((", "[")
    frameData = frameData.replace("))", "]")
    frameData = frameData.replace("(", "[")
    frameData = frameData.replace(")", "]")
    frameData = frameData.replace("\n", " ")

    print(frameData)

    frameData = eval(frameData)


    pos = data.tell()
    line = data.readline()
    data.seek(pos)






    currentMask = maskDirectory + masks[maskCounter]
    maskCounter+=1

    for x in range(len(frameData['Location'])):
        frameData['Location'][x] = frameData['Location'][x] * 1000


    gtDict.update({counter: [{"cam_R_m2c":sum(frameData["Rotation"], []), "cam_t_m2c":frameData["Location"], "obj_bb": get_bound_box(currentMask), "obj_id":1}]})
    #print(gtDict)
    counter+=1
data.close()


newGT = open(outputFile, 'w+')
print(yaml.dump(gtDict))
newGT.write(yaml.dump(gtDict))
newGT.close()
