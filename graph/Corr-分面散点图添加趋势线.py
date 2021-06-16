import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
# plt.figure(dpi=200)

df = pd.read_csv("E:\桌面\datasets\mpg_ggplot2.csv")
df_select = df.loc[df.cyl.isin([4, 8]), :]

# Each line in its own column
gridobj = sns.lmplot(x="displ",     #  原始数据字段名
                     y="hwy",      # 原始数据字段名
                     data=df_select,
                     height=7,
                     #robust:(可选)此参数接受布尔值，如果为True，
                     #则使用statsmodels估计稳健的回归。这将是de-weight个异常值。
                     # 请注意，这比标准线性回归的计算量大得多，因此您可能希望减少
                     # 引导程序重采样的次数(n_boot)或将ci设置为None。
                     robust=True,
                     palette='Set1',
                     col="cyl",  # 根据所指定属性在列上分类
                     scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

# Decorations
sns.set(style="whitegrid", font_scale=1.5)
gridobj.set(xlim=(0.5, 7.5), ylim=(10, 45))
gridobj.fig.set_size_inches(10, 6)
plt.show()

