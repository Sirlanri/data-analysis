import os
import numpy as np

#构建数据
def build_data():
    dirname="five/trainingDigits/"
    trains = os.listdir(dirname)
    for train in trains:
        index = 0
        with open(file=dirname+train,mode='r') as f:
            realnum = int(train[0:1])
            lines = f.readlines()
            newline = ''
            for line in lines:
                newline = ''.join([newline,line])
            print(newline)


build_data()