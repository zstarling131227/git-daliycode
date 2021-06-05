# 1英寸=2.54cm

import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sn
import warnings

df = pd.read_csv("E:\桌面\datasets\mpg_ggplot2.csv")
print(df.head())
# plt.figure(dpi=500)  # 像素为500
# 选择cyl中值为4和8的行，所有列。
df_select = df.loc[df.cyl.isin([4, 8]), :]
# lmplot 绘制回归模型
gridobj = sn.lmplot(
    x="displ",  # x轴标签，是data数据中，列的名字。
    y="hwy",  # Y轴标签，是data数据中，列的名字。
    hue="cyl",  # 图例，是data数据中，列的名字。
    data=df_select,
    height=7,  # 每个构面的高度(以英寸为单位)。
    aspect=1.6,  # 每个构面的纵横比，因此，aspect * height给出每个构面的宽度。
    palette="Set1",  # 此参数是调色板名称，列表或字典，用于不同级别的hue变量的颜色。
    # 标记点的属性设置。s表示内部大小，linewidths表示外框线的粗细，edgecolors表示外框线为黑色
    scatter_kws=dict(s=60, linewidths=0.7, edgecolors="black"),  # 词典
    legend=True,  # 如果为True且有色相变量，请添加图例
    legend_out=True,  # 如果为True，则图形尺寸将被扩展，并且图例将绘制在右中图的外部。
    fit_reg=True  # 是否显示回归模型。默认为True显示。
)

sn.set(style="whitegrid", font_scale=1.5)   # seaborn绘图时默认的5种风格之一。整体风格字体大小。
gridobj.set(xlim=(0.5, 7.5), ylim=(10, 50))  # 设置x,Y坐标范围。左边为起点，右边为终点。
gridobj.fig.set_size_inches(10, 6)  # 输出图设置大小
plt.title("Scatterplot with line of best fit grouped by number of cylinder",y=0.9)  #  Y表示标题位置 ，表示在Y正坐标轴90%的位置处。
plt.show()
