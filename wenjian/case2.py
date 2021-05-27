# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%d*%d=%d ' % (j, i, i * j), end="")
#     print("")


# 9_9乘法表
'''
i = 0
while i < 9:
    i += 1
    j = 0
    while j < i:
        j += 1
        # print('%d*%d=%2d ' % (j, i, i * j), end="")
        # print('%d*%d=%2d' % (j, i, i * j), end=" ")
        print('%d*%d=%d' % (j, i, i * j), end="\t")
    print("")
'''

# 多条件匹配
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data1=pd.read_excel("E:\\桌面\\恒丰练习.xlsx")
print(data1.columns)

data2=pd.read_excel("E:\桌面\恒丰链接替换.xlsx")
print(data2.head())
print(data2.columns)

data1.loc[(data2['识别码'] == data1['渠道码']) & (data1['进件日期']>= data2["上线时间"])&(data1["进件日期"]<=data2["下线时间"])
                 ,"渠道2"]=data2["渠道"]