import pandas as pd
import numpy as np

def chuangjian():
    data1 = np.array([
        ['深蓝',20,18],
        ['深蓝2',17,8],
        ['深蓝3',30,9],
    ])
    df1=pd.DataFrame(data=data1,
        columns=['name','age','length'],
        index=['first','second','third'])

    print()

def datacaluate():
    #时间的计算
    res = pd.to_datetime('2020-5-21')-pd.to_datetime('2000-1-25')
    print(res)

datacaluate()