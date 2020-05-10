#Prints the dictionary from two yml files for comparison
import yaml

testGT = open("/home/tsl_student/Desktop/DenseFusion-Pytorch-1.0/datasets/linemod/Linemod_preprocessed/data/01Original/gt.yml")

ourGT = open("/home/tsl_student/Desktop/1/gt.yml")


goodData = yaml.load_all(testGT, yaml.FullLoader)
badData = yaml.load_all(ourGT, yaml.FullLoader)


print("GOOD DATA")
for x in goodData:
    print(x)


print("BAD DATA")

for x in badData:
    print(x)
