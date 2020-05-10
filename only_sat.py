#Returns images the only contain the satellite.
import matplotlib.pyplot as plt
import random

def contains_sat(img_name):
    min_x = 2**20
    min_y = 2 ** 20
    max_x = -1
    max_y = -1

    found_sat = False
    img = plt.imread(img_name)
    for y in range(len(img)):
        sat_in_column = False

        for x in range(len(img[0])):
            if not img[y][x] == 0:
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
            return True

    if max_x == -1:
        return False
    else:
        return True

img_path = "/home/tsl_student/Desktop/DenseFusion-Pytorch-1.0/datasets/linemod/Linemod_preprocessed/data/01/mask/"

num_images = 1000

def name_gen():
    for i in range(1, num_images+1):
        img_name = img_path+"{0:05d}".format(i)+".png"
        if not contains_sat(img_name):
            yield "{0:05d}".format(i)

img_names = random.shuffle(list(name_gen()))

print(img_names)

