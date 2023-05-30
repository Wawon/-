import matplotlib.pyplot as plt
plt.style.use('classic') # 其它style可以试试seaborn, bmh, ggplot, grayscale
import numpy as np


fig = plt.figure()  # 创建图形
ax = plt.axes()  # 创建维度

x = np.linspace(0, 10, 1000)  # 在0到10之间生成1000个等间隔的数

# 已有x, 画出sin(x)的数据, 颜色设置为红,加入label用于制作图例
ax.plot(x, np.sin(x), color='red', label='sin(x)')


# 在同一幅图形中绘制多根线条，只需要多次调用plot函数即可
# 颜色设置为16进制金色，16进制需要前面打井号
# linestyle 可以是 -  --  -.  :
ax.plot(x, np.cos(x), color='#ffd700', linestyle='--', label='cos(x)')

plt.xlim(0, 11)  # 调整x轴的范围
plt.ylim(-1.5, 1.5)  # 调整y轴的范围
# 同样功能的函数：plt.axis([xmin, xmax, ymin, ymax])
# 如： plt.axis([-10, 10, -2, 2])
# plt.axis('tight')  # 可以将坐标轴压缩到刚好足够绘制折线图像的大小
# plt.axis('equal')  # 设置x轴与y轴使用相同的长度单位

plt.title("A Sine Curve")  # 设置标题
plt.xlabel("x")  # 设置x轴标签
plt.ylabel("sin(x)")  # 设置y轴标签
plt.legend()  # 召唤标签
plt.show()  # 显示图像
