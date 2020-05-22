import matplotlib.pyplot as plt
import numpy as np

# 1、创建画布
# 参数：画布大小
# 参数：像素
# 返回画布对象
plt.figure()
# 支持中文
plt.rcParams['font.sans-serif'] = 'SimHei'
# 支持负号
plt.rcParams['axes.unicode_minus'] = False
# 2、绘图、及修饰
# 下一周 天气温度走势 ---折线图
# 折线图-->点  --->(x,y)
# (x1,y1)  (x2,y2)  (x3,y3) ??? ---不需要
# 长度一致
#  x ---数组
x = np.arange(1, 8, 1)
#  y ---数组
y = np.array([15, 20, 22, 23, 20, 18, 16])
y1 = np.array([-10, -8, -12, -10, -8, -6, 1])
# print(x)
# print(y)
# 绘制折线图
# color --线的颜色
# linestyle--线的样式
# linewidth--线宽
# marker --点的样式
# markersize -点的大小
# markerfacecolor --点的填充颜色
# markeredgecolor --点的边缘颜色
plt.plot(x, y, color='r', linestyle=':', linewidth=1.2, marker="*", markersize=7, markerfacecolor='b',
         markeredgecolor='g')
plt.plot(x, y1, color='k', linestyle='-.', linewidth=1.2, marker="d", markersize=7, markerfacecolor='r',
         markeredgecolor='r')

# 修饰
# 添加标题
plt.title('下一周各个城市天气温度走势图')
# 添加横轴名称
plt.xlabel('日期')
# 添加纵轴名称
plt.ylabel('温度（℃）')

# 构建中文列表
xticks = ['周一', '周二', '周三', '周四', '周五', '周六', '周日', ]
# 修改横轴刻度
# 如果想要将 序号修改为中文
# 参数1 需要被替换的序号
# 参数2 需要填充的中文
plt.xticks(x, xticks, rotation=45)

# 修改纵轴刻度
# 构建yticks
yticks = np.arange(-15, 25, 3)
# 如果只是重新设置刻度范围，那么只需要填入新的刻度范围即可
plt.yticks(yticks)

# 添加图例
plt.legend(['北京天气', '哈尔滨天气'], loc=4)

# 标注---plt.text --每次的标注，只能标注一个点 --循环标注
# (x1,y1) (x2,y2) --具体的点
for i, j in zip(x, y):
    # 标注
    # 参数1 标注横轴坐标
    # 参数2 标注的纵轴坐标
    # 参数3 标注内容---str
    # horizontalalignment='center'  ---标注水平居中
    plt.text(i, j + 0.5, '%d℃' % j, horizontalalignment='center')

for i, j in zip(x, y1):
    # 标注
    # 参数1 标注横轴坐标
    # 参数2 标注的纵轴坐标
    # 参数3 标注内容---str
    # horizontalalignment='center'  ---标注水平居中
    plt.text(i, j + 0.5, '%d℃' % j, horizontalalignment='center')

# 3、保存及展示

# 保存图片
plt.savefig('./下一周各个城市天气温度走势图.png')
# 展示
plt.show()

# 用来确定事件的发展趋势

# (x,y) -- 二维
# (a,b,c,d,e,f) -- 六维---如何将多维数据可视化出来？
# 雷达图 ---可以将多维数据以平面图形的形式展示出来
