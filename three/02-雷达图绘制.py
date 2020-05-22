import matplotlib.pyplot as plt
import numpy as np

# 创建画布
plt.figure()
# 支持中文 和 负号
# 支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 支持负号
plt.rcParams['axes.unicode_minus'] = False
# 绘图
# 准备数据
x = np.array([2, 3.5, 4, 4.5, 5])
# 闭合数据
x = np.concatenate((x,[x[0]]),axis=0)
print(x)

# 需要将2π 的弧度进行划分 角度 ---划分为5个角度
# 定义划分角度的个数
datalength = 5
# 创建一个 等差数组
angle = np.linspace(0, 2 * np.pi, datalength, endpoint=False)
# 闭合角度
# 将 角度的第0 个元素追加到 angle的尾部
angle = np.concatenate((angle, [angle[0]]), axis=0)
print(angle)

# 绘制雷达图
plt.polar(angle, x)

# 增加标题
plt.title('该玩家的王者对战信息')
# 修改刻度
labels = ['生存评分', ' 输出评分 ', '团战评分 ', 'KDA', ' 发育评分']
plt.xticks(angle, labels)

# 展示
plt.show()
