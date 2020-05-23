import os
import numpy as np
import matplotlib as plt
import sklearn

#构建数据
def build_data():
    dirname="five/trainingDigits/"
    trains = os.listdir(dirname)
    #放所有数据的大列表
    datalist = np.zeros((len(trains),1025))
    newlines=np.zeros((32,32))
    for train in trains:
        fileindex = 0
        with open(file=dirname+train,mode='r') as f:
            lineindex=0
            realnum = int(train[0:1])
            lines = f.readlines()
            for line in lines:
                intline = np.array([int(i) for i in line[0:32]])
                newlines[lineindex] = intline
                lineindex+=1
            datalist[fileindex,0:1] = realnum
        datalist[fileindex,1:] = newlines.ravel()
        fileindex+=1
    save_data(datalist)
    print()
        

def save_data(datalist):
    np.save('five/data/',datalist)

def load_data():
    train_data = np.load('five/data/train.npy')
    print(train_data)
def knndo():
    knn = KNeighborsClassifier(n_neighbors=5)
    knn.fit()

#可视化数据
def view():
    #创建画布
    plt.figure()
    #绘图
    

load_data()