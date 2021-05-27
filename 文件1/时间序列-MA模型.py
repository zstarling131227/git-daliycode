from scipy import  stats
import statsmodels.api as sm  # 统计相关的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

IndexData = DataAPI.MktIdxdGet(indexID=u"",ticker=u"000001",beginDate=u"20130101",endDate=u"20140801",field=u"tradeDate,closeIndex,CHGPct",pandas="1")
IndexData = IndexData.set_index(IndexData['tradeDate'])
data = np.array(IndexData['CHGPct']) # 上证指数日涨跌
IndexData['CHGPct'].plot(figsize=(15,5))


# 画出序列的ACF 定阶
fig = plt.figure(figsize=(20,5))
ax1=fig.add_subplot(111)
fig = sm.graphics.tsa.plot_acf(data,ax=ax1)

# 建模
order = (0,10)
train = data[:-10]
test = data[-10:]
tempModel = sm.tsa.ARMA(train,order).fit()


# 拟合度
delta = tempModel.fittedvalues - train
score = 1 - delta.var()/train.var()
print(score)

# 预测
predicts = tempModel.predict(371, 380, dynamic=True)
print(len(predicts))
comp = pd.DataFrame()
comp['original'] = test
comp['predict'] = predicts
comp.plot()

