# 计算均方根误差，检查模型在测试数据集上的准确率：值越低越好

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
from math import sqrt

# 读取数据，pd.read_csv默认生成DataFrame对象，需将其转换成Series对象
df = pd.read_csv('train.csv')
print(df.head())

# Subsetting the dataset
# Index 11856 marks the end of year 2013
df = pd.read_csv('train.csv', nrows=11856)


# Creating train and test set
# Index 10392 marks the end of October 2013
train = df[0:10392]  ## 2012年8月25日到2013年10月31日   10392个  # 生成pd.Series对象
print("train-hour", len(train))
test = df[10392:]  ## 2013年11月1日到2014年9月25日  11856-10392等于1464个  # 生成pd.Series对象
print("test-hour", len(test))

# Aggregating the dataset at daily level
df['Timestamp'] = pd.to_datetime(df['Datetime'], format='%d-%m-%Y %H:%M')  # 格式化日期并将字段名改tinestamp
df.index = df['Timestamp']  # 将日期作为索引
df = df.resample('D').mean()  # 将数据做每天的平均值统计。
print("df", len(df))
print(df.head())

train['Timestamp'] = pd.to_datetime(train['Datetime'], format='%d-%m-%Y %H:%M')
train.index = train['Timestamp']
train = train.resample('D').mean()
print("train-day", len(train))

test['Timestamp'] = pd.to_datetime(test['Datetime'], format='%d-%m-%Y %H:%M')
test.index = test['Timestamp']
test = test.resample('D').mean()
print("test-day", len(test),type(test))

##  l两图表在一坐标里
# Plotting data
train.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
test.Count.plot(figsize=(15, 8), title='Daily Ridership', fontsize=14)
plt.show()

## 方法1：朴素法   用测试组的最后一个值做y-hat值
"""
如果数据集在一段时间内都很稳定，我们想预测第二天的价格，可以取前面一天的价格，预测第二天的值。这种假设第一个预测点和上一个观察点相等的预测方法就叫朴素法。
朴素法并不适合变化很大的数据集，最适合稳定性很高的数据集。
"""

'''
dd = np.asarray(train['Count'])
print("dd", len(dd))
print(dd[-1])
y_hat = test.copy()
y_hat['naive'] = dd[len(dd) - 1]
# print(y_hat['naive'])
plt.figure(figsize=(12, 8))
plt.plot(train.index, train['Count'], label='Train')
plt.plot(test.index, test['Count'], label='Test')
plt.plot(y_hat.index, y_hat['naive'], label='Naive Forecast')
plt.legend(loc='best')
plt.title("Naive Forecast")
plt.show()

rms = sqrt(mean_squared_error(test['Count'], y_hat['naive']))
print(rms)
 '''

# 方法2：简单平均法
"""
将预期值等同于之前所有观测点的平均值的预测方法就叫简单平均法。
"""

'''
y_hat_avg = test.copy()
y_hat_avg['avg_forecast'] = train['Count'].mean()

rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['avg_forecast']))
print(rms)

plt.figure(figsize=(12, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['avg_forecast'], label='Average Forecast')
plt.legend(loc='best')
plt.show()

'''

# 方法3：移动平均法
"""
只取最近几个时期的价格平均值。很明显这里的逻辑是只有最近的值最要紧。这种用某些窗口期计算平均值的预测方法就叫移动平均法。
"""

'''
y_hat_avg = test.copy()
y_hat_avg['moving_avg_forecast'] = train['Count'].rolling(60).mean().iloc[-1]   # 60作为P值，roll移动平均。

# loc是根据dataframe的具体标签选取列，而iloc是根据标签所在的位置，从0开始计数。
# 你想要选取某一行的数据，可以使用df.loc[[i]]或者df.iloc[[i]]
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['moving_avg_forecast'], label='Moving Average Forecast')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['moving_avg_forecast']))
print(rms)
'''

"""

####  指数平滑法
# 指数平滑即指数移动平均（exponential moving average），是以指数式递减加权的移动平均。
   各数值的权重随时间指数式递减，越近期的数据权重越高。
# 常用的指数平滑方法有一次指数平滑、二次指数平滑和三次指数平滑。
相比更早时期内的观测值，它会给近期的观测值赋予更大的权重。
# 指数平滑法，它比移动平均法的一个进步之处就是相当于对移动平均法进行了加权。加权移动平均其实还是一
种移动平均法，只是“滑动窗口期”内的值被赋予不同的权重，通常来讲，最近时间点的值发挥的作用更大了。
"""

# 方法4：简单指数平滑法也就是一次指数平滑
"""
时间 t+1 处的预测值为最近观测值yt和最近预测值 y^t|t−1之间的加权平均值。
适合用来预测没有明显趋势和季节性的时间序列。其预测结果是一条水平的直线。
"""

from statsmodels.tsa.api import SimpleExpSmoothing

'''
y_hat_avg = test.copy()
print(y_hat_avg.tail())
fit = SimpleExpSmoothing(np.asarray(train['Count'])).fit(smoothing_level=0.6, optimized=False)   # alpha=0.6
y_hat_avg['SES'] = fit.forecast(len(test))    #  新增一列SES
print(y_hat_avg.tail())

plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['SES'], label='SES')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['SES']))
print(rms)
'''

# 方法5：霍尔特(Holt)线性趋势法也叫二次指数平滑

"""
每个时序数据集可以分解为相应的几个部分：趋势（Trend），季节性(Seasonal)和残差(Residual)。任何呈现某种趋势的数据集都可以用霍尔特线性趋势法用于预测。
模型的预测结果是一条斜率不为0的直线
"""
import statsmodels.api as sm
from statsmodels.tsa.api import Holt

# '''
sm.tsa.seasonal_decompose(train['Count'],model="additive").plot()  # model也可以写为multiplicative乘法
result = sm.tsa.stattools.adfuller(train['Count'])    # ADF检验
print(result)
plt.show()

y_hat_avg = test.copy()

fit = Holt(np.asarray(train['Count'])).fit(smoothing_level=0.3, smoothing_slope=0.1)
y_hat_avg['Holt_linear'] = fit.forecast(len(test))

plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['Holt_linear'], label='Holt_linear')
plt.legend(loc='best')
plt.show()
rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['Holt_linear']))
print(rms)
# '''

# 方法6：Holt-Winters季节性预测模型也叫三次指数平滑
"""
如果数据集在一定时间段内的固定区间内呈现相似的模式，那么该数据集就具有季节性。
Winters季节性预测模型，它是一种三次指数平滑预测，其背后的理念就是除了水平和趋势外，还将指数平滑应用到季节分量上。

Holt-Winters季节性预测模型由预测函数和三次平滑函数——一个是水平函数ℓt，一个是趋势函数bt，一个是季节分量 st，以及平滑参数α,β和γ。
"""

'''
from statsmodels.tsa.api import ExponentialSmoothing

y_hat_avg = test.copy()
#  此处的加法模型add可以改为乘法模型mul
fit1 = ExponentialSmoothing(np.asarray(train['Count']), seasonal_periods=7, trend='add', seasonal='add', ).fit()
y_hat_avg['Holt_Winter'] = fit1.forecast(len(test))
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['Holt_Winter'], label='Holt_Winter')
plt.legend(loc='best')
plt.show()

rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['Holt_Winter']))
print(rms)
'''

# 方法7：自回归移动平均模型（ARIMA）
"""
# 线性的指数平滑方法可以看作是 ARIMA 的特例。
# 例如简单指数平滑等价于 ARIMA(0, 1, 1)，
# Holt's linear trend method 等价于 ARIMA(0, 2, 2)，
# 而 Damped trend methods 等价于 ARIMA(1, 1, 2) 等。
指数平滑模型都是基于数据中的趋势和季节性的描述，而自回归移动平均模型的目标是描述数据中彼此之间的关系。
ARIMA的一个优化版就是季节性ARIMA。它像Holt-Winters季节性预测模型一样，也把数据集的季节性考虑在内。
"""

'''
import statsmodels.api as sm

y_hat_avg = test.copy()
fit1 = sm.tsa.statespace.SARIMAX(train.Count, order=(2, 1, 4), seasonal_order=(0, 1, 1, 7)).fit()
y_hat_avg['SARIMA'] = fit1.predict(start="2013-11-1", end="2013-12-31", dynamic=True)
plt.figure(figsize=(16, 8))
plt.plot(train['Count'], label='Train')
plt.plot(test['Count'], label='Test')
plt.plot(y_hat_avg['SARIMA'], label='SARIMA')
plt.legend(loc='best')
plt.show()
rms = sqrt(mean_squared_error(test['Count'], y_hat_avg['SARIMA']))
print(rms)
'''
