import os
import numpy as np
import matplotlib as plt
from sklearn.neighbors import KNeighborsClassifier
#构建数据
def build_data():
    dirname="five/trainingDigits/"
    trains = os.listdir(dirname)
    newlines=np.zeros(32,32)
    for train in trains:
        index = 0
        with open(file=dirname+train,mode='r') as f:
            realnum = int(train[0:1])
            lines = f.readlines()
            newline = ''
            for line in lines:
                newline = ''.join([newline,line])
            newlines[index] = newline
            index+=1
    nparray = np.array(newlines)

def save_data(datalist):
    pass

def knndo():
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit()

#可视化数据
def view():
    #创建画布
    plt.figure()
    #绘图
    

build_data()