import pandas as pd

# 加载数据
users = pd.read_excel('./users.xlsx')
print(users)
print(users.columns)

# 增加---给users 添加新的一列
# users['next_age'] = users['age'] + 1
# print(users)

# 删除---drop方法
# labels 指定删除的行、列名称
# axis --轴，
# 如果 labels指定的行名称，此时axis = 0,
# 如果labels 指定的是列名称，此时axis = 1
# inplace  True直接原来的 users产生修改
# 如果是False，不会对users产生修改，会返回一个新的修改之后的结果
# users.drop(labels=['next_age', 'age', 'poo', 'sex'], axis=1, inplace=True)
# print(users)

# 修改 --直接获取到存在的列，然后重新赋值
# users['age'] = 18
# print(users)
# 在满足某些情况的条件下，才进行修改
# 如果 age 偶数，就将偶数年龄 修改为99
# bool 数组索引 --True ,干掉False
# 构建bool数组  ----让 满足偶数的为True,不满足的为False
# 比较运算---返回bool数组
bool_index = users.loc[:, 'age'] % 2 == 0
# print(bool_index)

# 根据bool数组索引，筛选出 为偶数的 样本   再对这些满足条件的样本的age 进行重新赋值
users.loc[bool_index, 'age'] = 99

print(users)
