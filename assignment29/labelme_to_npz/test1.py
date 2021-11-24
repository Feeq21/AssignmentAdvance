import os 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from dataset_core1 import create_dataset



srcPaths = ['D:/KOTOCLASS/secondmonth/cv-master/advanceworkbook/assignment28/classdata/dataset/pic1','D:/KOTOCLASS/secondmonth/cv-master/advanceworkbook/assignment28/classdata/dataset/pic2']
datasetfilename = 'cvdataset.npz'

if create_dataset(datasetfilename,srcPaths):

    data = np.load(datasetfilename, allow_pickle=True)

    imgList = data['images']
    labelList = data['labels']
    print(imgList.shape)
    print(labelList.shape)

    img = imgList[2]
    label = labelList[2]

    imgRGB  =img[:,:,::-1]
    plt.imshow(imgRGB)
    plt.title(label)
    plt.show()