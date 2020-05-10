import random

# puts all non-train images in test file

# file with all the images containing the satellite 
f_all = open("/home/tsl_student/Desktop/10000img/1/all.txt", "r")
f_train = open("/home/tsl_student/Desktop/Fresh-Fusion/DenseFusion-Pytorch-1.0/datasets/serpent/serpentProcessed/data/01/train.txt", "w")
f_test = open("/home/tsl_student/Desktop/Fresh-Fusion/DenseFusion-Pytorch-1.0/datasets/serpent/serpentProcessed/data/01/test.txt", "w")

num_train = 3000

images = list(line for line in f_all) 
random.shuffle(images)
train_images = [images[i] for i in range(num_train)]
test_images = [images[i] for i in range(num_train, len(images))]

for img in train_images:
	f_train.write(img)
for img in test_images:
	f_test.write(img)

f_all.close()
f_train.close()
f_test.close()

