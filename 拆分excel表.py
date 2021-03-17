#!/usr/bin/python
# -*- coding:utf-8 -*-
import xlwt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

data = pd.read_excel(r"H:\wait_data\恒丰数据-上分-2021.3.12.xlsx", sheet_name=u'进件')
# print(data.head())

# data.drop(["一级分行",'二级分行','合作商','进件介质','推广机制代码'],axis=1)
# print(data.head())

rows = data.shape[0]  # 获取行数 shape[1]获取列数
department_list = []

for i in range(rows):
    temp = data[u"渠道"][i]
    if temp not in department_list:  # 防止重复
        department_list.append(temp)  # 将销售部门的分类存在一个列表中

n = len(department_list)  # 销售部门科目数
print(n)

df_one = pd.DataFrame()  # 用于存储一科的dataframe
df_two = pd.DataFrame()  # 用于存储二科的dataframe
df_three = pd.DataFrame()  # 用于存储三科的dataframe
df_four = pd.DataFrame()  # 用于存储四科的dataframe
df_list = [df_one, df_two, df_three, df_four]

for department in range(n):
    for i in range(0, rows):
        if data[u"渠道"][i] == department_list[department]:
            df_list[department] = pd.concat([df_list[department], data.iloc[[i], :]], axis=0, ignore_index=True)


# with open("H:\\wait_data:\\new.xlsx","a") as file_obj:
#     for i in range(n):
#         file_obj.write(df_list[i])

writer = pd.ExcelWriter("H:\\wait_data:\\new.xls")  # 利用pd.ExcelWriter()存多张sheets

for i in range(n):
    df_list[i].to_excel(writer, sheet_name=str(department_list[i]), index=False)  # 注意加上index=FALSE 去掉index列
writer.save()

