# 导包
import pandas as pd
import numpy as np

#
df = pd.DataFrame(data=np.array([['zs', 17, 173.5],
                                 ['ls', 19, 175.0],
                                 ['ww', 20, 172.5]]),
                  # 列索引名称
                  columns=['name', 'age', 'height'],
                  # 行索引名称
                  index=['stu_1', 'stu_2', 'stu_3'])

print(df)

# 直接获取元素 ----先列，再行

# # 获取单列数据 --series
# print(df['name'])
# # 获取多列数据 ---列名列表
# print(df[['name', 'age']])

# 获取单列的指定行内容 ---行下标、行下标切片
# head(n) 获取指定的前n行
# tail(n) 获取指定的后n行
# print(df['name'][:2])
# print(df['name'].head(2))

# 获取多列的指定行 ---下标切片、head tail
# print(df[['name', 'age']][:2])
# print(df[['name', 'age']].head(2))

# 使用loc iloc 方式
# 直接索引
# loc 方式只能使用名称
# print(df.loc[:,'name'])
# 名称切片 ---前后都包含
# print(df.loc[:, 'name':'age'])
# iloc 方式只能使用下标
# print(df.iloc[:, 0:1])
