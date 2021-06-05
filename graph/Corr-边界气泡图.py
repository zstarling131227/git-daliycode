import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

from matplotlib import patches
from scipy.spatial import ConvexHull  # 更多参考scipy.spatial.ConvexHull

sns.set_style("whitegrid")

# Step 1: Prepare Data
midwest = pd.read_csv("E:\桌面\datasets\midwest_filter.csv")

# As many colors as there are unique midwest['category']
categories = np.unique(midwest['category'])
colors = [
    plt.cm.Set1(i / float(len(categories) - 1)) for i in range(len(categories))
]

# Step 2: Draw Scatterplot with unique color for each category
# 建成的是空白区域
fig = plt.figure(figsize=(10, 6), dpi=80, facecolor='w', edgecolor='k')
# 绘制散点图
for i, category in enumerate(categories):
    plt.scatter('area',
                'poptotal',
                data=midwest.loc[midwest.category == category, :],
                s='dot_size',  # 圆的大小
                c=colors[i],
                label=str(category),  # 图例名称
                edgecolors='black',
                linewidths=.5)

plt.show()

# Step 3: Encircling
# https://stackoverflow.com/questions/44575681/how-do-i-encircle-different-data-sets-in-scatter-plot
def encircle(x, y, ax=None, **kw):  # 定义encircle函数，圈出重点关注的点
    # 创建ax子图
    if not ax: ax = plt.gca()
    # np.r_是按列连接两个矩阵，就是把两矩阵上下相加，要求列数相等。
    # np.c_是按行连接两个矩阵，就是把两矩阵左右相加，要求行数相等。
    p = np.c_[x, y]
    # 凸包算法：，给定二维平面上的点集，凸包就是将最外层的点连接起来构成的凸多边型，它能包含点集中所有的点。
    hull = ConvexHull(p)
    # 创建相对应的形状，常用的是Rectangle矩形、Circle圆形、Polygon多边形这三个，plt.形状名(x，y)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    # 将创建的形状图形添加进“ Axes ”对象里面去，即我们所创建的ax对象，此处指的是散点图
    ax.add_patch(poly)


# 图形1
# Select data to be encircled
midwest_encircle_data1 = midwest.loc[midwest.state == 'IN', :]
#   刻画内部区域
encircle(midwest_encircle_data1.area,
         midwest_encircle_data1.poptotal,
         ec="pink",  # 边框色
         fc="#74C476",  # 背景色
         alpha=0.5)  # 指背景色的透明度
#   描绘边框，会覆盖内部区域构建的边框
encircle(midwest_encircle_data1.area,
         midwest_encircle_data1.poptotal,
         ec="g",
         fc="none",
         linewidth=1.5)

# 图形2
midwest_encircle_data6 = midwest.loc[midwest.state == 'WI', :]
#   刻画内部区域
encircle(midwest_encircle_data6.area,
         midwest_encircle_data6.poptotal,
         ec="pink",
         fc="black",
         alpha=0.3)
#   描绘边框，会覆盖内部区域构建的边框
encircle(midwest_encircle_data6.area,
         midwest_encircle_data6.poptotal,
         ec="black",
         fc="none",
         linewidth=1.5,
         linestyle='--')

# Step 4: Decorations
plt.gca().set(
    xlim=(0.0, 0.1),
    ylim=(0, 90000),
)

plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Area', fontdict={'fontsize': 14})
plt.ylabel('Population', fontdict={'fontsize': 14})
plt.title("Bubble Plot with Encircling", fontsize=14)
plt.legend(fontsize=10)
plt.show()
