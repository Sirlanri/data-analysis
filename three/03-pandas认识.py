# pandas库----进行数据处理
# 里面封装了numpy 、 matplotlib 部分功能 ----> 运算、可视化、统计分析
# pandas结构：
# series   ---存储一维数据，只有行索引、没有列索引
# dataframe ---存储二维数据，具有行索引、列索引

# 导包
import pandas as pd
import numpy as np

#
# df = pd.DataFrame(data=np.array([['zs', 17, 173.5],
#                                  ['ls', 19, 175.0],
#                                  ['ww', 20, 172.5]]),
#                   # 列索引名称
#                   columns=['name', 'age', 'height'],
#                   # 行索引名称
#                   index=['stu_1', 'stu_2', 'stu_3'])
#
# print(df)
# print(df.ndim)
# print(df.shape)
# print(df.size)
# df 还有一些属性
# print(df.index)  # 行索引名称
# print(df.columns)  # 列索引名称
# print(df.values)  # value
# print(type(df.values))  # <class 'numpy.ndarray'>
# 没有itemsize ---因为dataframe中不同的列可以是不同的类型
# 没有 dtype ---因为dataframe中不同的列可以是不同的类型
# print(df.dtypes)  # 每一列的对应的数据类型
# print(type(df))  # <class 'pandas.core.frame.DataFrame'>

# 获取 df 中的 name
# print(df['name'])
# print(df['name'].ndim)
# print(type(df['name']))  # <class 'pandas.core.series.Series'>

#
# se = pd.Series(data=np.array(['zs', 'ls', 'ww']),
#                index=['stu_1', 'stu_2', 'stu_3'])
#
# print(se)
