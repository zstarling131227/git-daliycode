import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

midwest = pd.read_csv("E:\桌面\datasets\midwest_filter.csv")
# 去重获取图例
catagories = np.unique(midwest['category'])
# 对图例设置颜色
colors = [plt.cm.Set1(i / float(len(catagories) - 1)) for i in range(len(catagories))]

# figsize=(10, 6)表示行刻度为10，列刻度为6。dpi参数指定绘图对象的分辨率。背景色为白色，边框线为黑色。
plt.figure(figsize=(10, 6), dpi=100, facecolor="w", edgecolor="k")
for i, catagory in enumerate(catagories):
    plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category == catagory, :], s=20, c=colors[i],
                label=str(catagory))
# plt.gca()获取当前图表
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000))
plt.xticks(fontsize=50)
plt.yticks(fontsize=10)
plt.xlabel("area", fontdict={"fontsize": 10})
plt.xlabel("population", fontdict={"fontsize": 10})
plt.title("Scatterplot of Midwest Area vs Population", fontsize=12)
plt.legend(loc='best',fontsize=10)  # legend 是多图例的设置，此处表示设置图例字体大小，位置为选择最佳位置。
plt.show()
