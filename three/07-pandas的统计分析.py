import pandas as pd

# max min std var median(中位数) quantile(四分位数) mode(众数)
# count(非空数据的数目)

# 加载数据
detail = pd.read_excel('./meal_order_detail.xlsx')
print(detail)
print(detail.columns)

# 可以针对 amounts 单价进行统计指标演示
# print(detail.loc[:,'amounts'].max())
# print(detail.loc[:,'amounts'].min())
# 中位数
# print(detail.loc[:,'amounts'].median())
# 非空数据的数量
# print(detail.loc[:,'amounts'].count())
# 四分位数
# print(detail.loc[:, 'amounts'].quantile(q=[0, 0.25, 0.5, 0.75, 1]))
# 中位数
# print(detail.loc[:, 'amounts'].mode())
# print(type(detail.loc[:, 'amounts'].mode()))
