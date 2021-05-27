import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

midwest = pd.read_csv("E:\桌面\datasets\midwest_filter.csv")
# 取唯一值
catagories = np.unique(midwest['category'])

colors = [plt.cm.Set1(i / float(len(catagories) - 1)) for i in range(len(catagories))]
plt.figure(figsize=(10, 6), dpi=100, facecolor="w", edgecolor="k")
for i, catagory in enumerate(catagories):
    plt.scatter('area', 'poptotal', data=midwest.loc[midwest.category == catagory, :], s=20, c=colors[i],
                label=str(catagory))
plt.gca().set(xlim=(0.0, 0.1), ylim=(0, 90000))
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("area", fontdict={"fontsize": 10})
plt.xlabel("population", fontdict={"fontsize": 10})
plt.title("Scatterplot of Midwest Area vs Population", fontsize=12)
plt.legend(fontsize=10)
plt.show()
