import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.cluster import KMeans
import pymysql


def build_data():
    ''' 加载数据 '''
    air_data = pd.read_csv('six/air_data.csv')
    # 使用mysql提供数据
    con = pymysql.connect(host="127.0.0.1", user="root",
                          password="123456", db="pydata")
    #air_data_sql = pd.read_sql('select * from airdata',con)
    return air_data


def deal_data(air_data):
    ''' 处理数据 '''
    bool_index1 = air_data['SUM_YR_1'].notnull()
    bool_index2 = air_data['SUM_YR_2'].notnull()
    # bool数组筛选
    bool_index = bool_index1 & bool_index2
    air_data = air_data.loc[bool_index, :]

    # 飞行次数
    bool_id1 = air_data['SUM_YR_1'] > 0
    bool_id2 = air_data['SUM_YR_2'] > 0
    bool_id3 = air_data['avg_discount'] > 0

    bool_id = (bool_id1 | bool_id2) & bool_id3
    air_data = air_data.loc[bool_id, :]

    # LRMFC构建
    air_data = air_data.loc[:, ['FFP_DATE', 'LOAD_TIME',
                                'LAST_TO_END', 'avg_discount', 'FLIGHT_COUNT', 'SEG_KM_SUM']]
    air_data['L_days'] = pd.to_datetime(
        air_data['LOAD_TIME'])-pd.to_datetime(air_data['FFP_DATE'])
    air_data['L'] = [tmp.days / 30 for tmp in air_data['L_days']]
    air_data['R'] = air_data['LAST_TO_END']
    air_data['F'] = air_data['FLIGHT_COUNT']
    air_data['M'] = air_data['SEG_KM_SUM']
    air_data['C'] = air_data['avg_discount']

    air_data = air_data.loc[:, ['L', 'R', 'F', 'M', 'C']]
    # 标准化数据
    stand = preprocessing.minmax_scale(air_data)
    return stand


def k_means(air_data, k):
    km = KMeans(n_clusters=k)
    # 训练数据
    km.fit(air_data)
    y_predict = km.predict(air_data)
    center = km.cluster_centers_
    return y_predict, center


def show_res(center):
    '''可视化雷达图'''
    plt.figure()
    # 支持中文
    plt.rcParams['font.sans-serif'] = 'SimHei'
    plt.rcParams['axes.unicode_minus'] = False
    data_length = center.shape[1]
    angle = np.linspace(0, 2*np.pi, data_length, endpoint=False)
    angle = np.concatenate((angle, [angle[0]]), axis=0)
    for i in range(center.shape[0]):
        data = np.concatenate((center[i, :], [center[i, 0]]), axis=0)
        plt.polar(angle, data)
    plt.title('航空的聚类')
    plt.legend(['第1类', '第2类', '第3类', '第4类', '第5类', ])
    plt.xticks(angle[:-1], ['L', 'R', 'F', 'M', 'C'])
    plt.show()


def main():
    data = build_data()
    after_deal = deal_data(data)
    y_predict, center = k_means(after_deal, 5)
    show_res(center)


main()
