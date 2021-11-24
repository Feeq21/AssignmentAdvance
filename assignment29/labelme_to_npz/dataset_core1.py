import os 
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def create_dataset(datasetfilename,srcPaths):

    imgList = []
    labelList = []

    #srcPath = "rawdata"
    for srcPath in srcPaths :
        for fname in os.listdir(srcPath):
            filePath = os.path.join(srcPath,fname)
            
            img = cv.imread(filePath)

            fname_no_ext = os.path.splitext(fname)[0]
            label = fname_no_ext[-1]

            imgList.append(img)
            labelList.append(label)

    images =np.array(imgList,dtype='object')
    labels = np.array(labelList,dtype='object')
    np.savez_compressed(datasetfilename,images=images,labels=labels)
    
    #print(type(imgList))
    #print(type(imgList))

    return True

# if __name__ =='__main__':

#     datasetfilename = 'afiqdataset.npz'

#     if create_dataset(datasetfilename):

#         data = np.load(datasetfilename, allow_pickle=True)

#         imgList = data['images']
#         labelList = data['labels']

#         img = imgList[0]
#         label = labelList[0]

#         imgRGB  =img[:,:,::-1]
#         plt.imshow(imgRGB)
#         plt.title(label)
#         plt.show()

    #imgList,labelList = create_dataset()
    #for i in range (5):
        #img = imgList[i]
        #label = labelList[i]
        #imgRGB  =img[:,:,::-1]
        #plt.imshow(imgRGB)
        #plt.title(label)
        #plt.show()

        #img = imgList[1]
        #imgRGB  =img[:,:,::-1]
        #plt.imshow(imgRGB)
        #plt.show()
