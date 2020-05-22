import pandas as pd

#  Timestamp : pandas默认支持的时间点的类型
#  DatetimeIndex : pandas默认支持的时间序列类型
#  datetime64[ns]: numpy中的时间点的类型

# '2020-05-20' ---时间点
# 可以使用
# res = pd.to_datetime('2020-05-20')
# print(res)
# print(type(res))  # <class 'pandas._libs.tslib.Timestamp'>

# 多个时间点的序列
# ['2020-05-20','2020-05-21','2020-05-22']
# res = pd.to_datetime(['2020-05-20', '2020-05-21', '2020-05-22'])
# print(res)
# print(type(res))  # <class 'pandas.core.indexes.datetimes.DatetimeIndex'>

# 加载detail
detail = pd.read_excel('./meal_order_detail.xlsx')
print(detail)
print(detail.columns)
print(detail.dtypes)
# 转化成pandas支持的时间数据
detail.loc[:,'place_order_time'] = pd.to_datetime(detail.loc[:,'place_order_time'])

# 提取时间属性
# 列表推导式 获取 年、月、日 、时 、分 、秒
# year = [i.year for i in detail.loc[:,'place_order_time']]
# print(year)

month = [i.month for i in detail.loc[:,'place_order_time']]
print(month)