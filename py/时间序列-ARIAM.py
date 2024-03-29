from scipy import  stats
import statsmodels.api as sm  # 统计相关的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

IndexData = DataAPI.MktIdxdGet(indexID=u"",ticker=u"000001",beginDate=u"20130101",endDate=u"20140801",field=u"tradeDate,closeIndex,CHGPct",pandas="1")
IndexData = IndexData.set_index(IndexData['tradeDate'])
data = np.array(IndexData['CHGPct']) # 上证指数日涨跌
IndexData['CHGPct'].plot(figsize=(15,5))

# 观察上证综指的日指数序列
data2 = IndexData['closeIndex'] # 上证指数
data2.plot(figsize=(15,5))

# 进行ADF单位根检验
temp = np.array(data2)
t = sm.tsa.stattools.adfuller(temp)  # ADF检验
output=pd.DataFrame(index=['Test Statistic Value', "p-value", "Lags Used", "Number of Observations Used","Critical Value(1%)","Critical Value(5%)","Critical Value(10%)"],columns=['value'])
output['value']['Test Statistic Value'] = t[0]
output['value']['p-value'] = t[1]
output['value']['Lags Used'] = t[2]
output['value']['Number of Observations Used'] = t[3]
output['value']['Critical Value(1%)'] = t[4]['1%']
output['value']['Critical Value(5%)'] = t[4]['5%']
output['value']['Critical Value(10%)'] = t[4]['10%']
output

# 序列进行1次差分后再次检验！
data2Diff = data2.diff()  # 差分
data2Diff.plot(figsize=(15,5))

# ADF检验：
temp = np.array(data2Diff)[1:] # 差分后第一个值为NaN,舍去
t = sm.tsa.stattools.adfuller(temp)  # ADF检验
print("p-value:   ",t[1])


# PACF、ACF 判断模型阶次 P.Q
temp = np.array(data2Diff)[1:] # 差分后第一个值为NaN,舍去
fig = plt.figure(figsize=(20,10))
ax1=fig.add_subplot(211)
fig = sm.graphics.tsa.plot_acf(temp,lags=30,ax=ax1)
ax2 = fig.add_subplot(212)
fig = sm.graphics.tsa.plot_pacf(temp,lags=30,ax=ax2)

# 信息准则定阶P ,Q
AIC=sm.tsa.arma_order_select_ic(temp,max_ar=6,max_ma=4,ic='aic')['aic_min_order']  # AIC

# 建立ARMA(2,2)模型：
order = (2,2)
data = np.array(data2Diff)[1:] # 差分后，第一个值为NaN
rawdata = np.array(data2)
train = data[:-10]
test = data[-10:]
model = sm.tsa.ARMA(train,order).fit()
# 拟合效果
plt.figure(figsize=(15,5))
plt.plot(model.fittedvalues,label='fitted value')
plt.plot(train[1:],label='real value')
plt.legend(loc=0)

delta = model.fittedvalues - train
score = 1 - delta.var()/train[1:].var()
print(score)
# 预测效果
predicts = model.predict(10,381, dynamic=True)[-10:]
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = test
comp['predict'] = predicts
comp.plot(figsize=(8,5))


# 将预测值还原（即在上一时刻指数值的基础上加上差分差值的预估）：
rec = [rawdata[-11]]
pre = model.predict(371, 380, dynamic=True) # 差分序列的预测
for i in range(10):
    rec.append(rec[i]+pre[i])

plt.figure(figsize=(10,5))
plt.plot(rec[-10:],'r',label='predict value')
plt.plot(rawdata[-10:],'blue',label='real value')

