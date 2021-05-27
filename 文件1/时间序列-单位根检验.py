# '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from statsmodels.tsa.api import Holt
# 读取数据，pd.read_csv默认生成DataFrame对象，需将其转换成Series对象
df=pd.read_excel("H:\\wait_data\\shuidi-PV.xlsx",sheet_name="Sheet3")
print(type(df))
print(df.head())
# print("index",df.index)
train=df[:365]
test=df[366:]
print("train",len(train),type(train),"test",len(test),type(test))
print(df["date"].dtype)
print(type(df["date"]))


df["timestamp"]=pd.to_datetime(df["date"],format='%d-%m-%Y')
df.index=df["timestamp"]
df=df.resample("D").mean()
train["timestamp"]=pd.to_datetime(train["date"],format='%d-%m-%Y')
train.index=train["timestamp"]
train=train.resample("D").mean()
test["timestamp"]=pd.to_datetime(test["date"],format='%d-%m-%Y')
test.index=test["timestamp"]
test=test.resample("D").mean()
# print("train",len(train),type(train),"test",len(test),type(test))

train.PV.plot(figsize=(15,8),title="shuidi-PV",fontsize=14)
test.PV.plot(figsize=(15,8),title="shuidi-PV",fontsize=14)
plt.show()

train.UV.plot(figsize=(15,8),title="shuidi-UV",fontsize=14)
test.UV.plot(figsize=(15,8),title="shuidi-UV",fontsize=14)
plt.show()

sm.tsa.seasonal_decompose(train["PV"]).plot()
re_PV=sm.tsa.stattools.adfuller(train["PV"])
print(re_PV)
plt.show()

sm.tsa.seasonal_decompose(train["UV"]).plot()
re_UV=sm.tsa.stattools.adfuller(train["UV"])
print(re_UV)
plt.show()

train_diff_pv=np.diff(train["PV"])     # 默认一阶差分，且是列差分。
# train_diff=train["PV"].diff(periods=2).dropna()     # 二阶差分
# print(train_diff_pv, len(train_diff_pv), type(train_diff_pv))
re_diff_pv=sm.tsa.stattools.adfuller(train_diff_pv)
print(re_diff_pv)


train_diff_uv=np.diff(train["UV"])     # 默认一阶差分，且是列差分。
# print(train_diff_uv, len(train_diff_uv), type(train_diff_uv))
re_diff_uv=sm.tsa.stattools.adfuller(train_diff_uv)
print(re_diff_uv)

# fit=Holt(np.asarray(train["PV"])).fit()
# fore_data=fit.forecast()

from statsmodels.tsa.stattools import coint

print(coint(train["PV"],train["UV"]))


