import matplotlib.pyplot as plt
import numpy as np

# 生成10个类别的随机数据
num_classes = 10
num_points = 100
x = np.random.randn(num_classes, num_points, 2)

# 画一个十分类的散点图
fig, ax = plt.subplots()
for i in range(num_classes):
    ax.scatter(x[i,:,0], x[i,:,1], label=f'Class {i+1}')

# 设置图形标题和轴标签
ax.set_title('10-class scatter plot')
ax.set_xlabel('X values')
ax.set_ylabel('Y values')

# 设置图例位置和样式
ax.legend(loc='upper right', fancybox=True, shadow=True)

# 显示图形
plt.show()
