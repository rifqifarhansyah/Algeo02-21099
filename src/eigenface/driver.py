import os
import cv2
import numpy as np
from eigenfaces import *
from PIL import Image

def computeFaceRecognition (self) :

    self.dirDataSet = "D:/ITB 21/KULYAHHH/SEMESTER 3/AlGeo/TUBES 2 ALGEO/Algeo02-21099/test/data_100"

    # *** find the normalized of Data Set ***
    self.trainingFaces = getTrainingFaces(self.dirDataSet)

    # *** convert test image to vector ***
    self.matrixImage = np.asarray(self.image_input) # NOT FIX
    self.vectorImage = getVectorImage(self.matrixImage)
    # print("processing.. 5%")

    # *** find best Eigen Vector of DataSet ***
    self.bestEigenVector = getBestEigenFaces(self.trainingFaces)
    # print("processing.. 35%")

    # *** find the linear combination of bestEigenVector from test image ***
    self.linerCombination = getLinComOfEigVector(self.bestEigenVector, self.vectorImage)

    # *** find matrix of coeff LinearCombination ***
    self.matrixLinCom = getLinComMatrix(self.bestEigenVector, self.trainingFaces)
    self.minimumDistance = getMinimumDistance(self.linerCombination, self.matrixLinCom)
    # print("processing.. 70%")

    # *** tolerance value ***
    self.toleranceValue = 1
    # print(self.minimumDistance)
    if (self.minimumDistance < self.toleranceValue) :
        self.imagefile = getClosestImage(self.dirDataSet, self.matrixLinCom, self.linerCombination)
        return(self.imagefile)

