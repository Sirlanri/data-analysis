# 导包
import pandas as pd

# 常用的文件 excel文件 csv文件
# 利用pandas读取文件
# pd.read_xxx() 语法
# 保存文件
# df.to_xxx() 语法

# excel文件 ---表格文件，以.xls  .xlsx为结尾的文件
# 参数：文件路径 + 名称
# 参数： 表格的下标
# detail = pd.read_excel('./meal_order_detail.xlsx', sheetname=0)
# print(detail)
# print(type(detail))

# .csv文件 ----以逗号分隔的、文本的序列化文件
# 参数：文件路径+名称
# 编码格式
# info = pd.read_csv('./meal_order_info.csv', sep=',', encoding='ansi')
# print(info)
# print(type(info))

# 进行保存
# 将 info 保存为excel文件
# info.to_excel('./aaaa.xlsx', index=False)
#
# # 将info 保存为.csv文件
# info.to_csv('./bbb.csv', index=False)
