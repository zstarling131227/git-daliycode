# 载入相关的库
from scipy import  stats
import statsmodels.api as sm  # 统计相关的库
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
temp = DataAPI.EcoDataProGet('2180000195','20100101','20151231')
temp = temp.set_index('periodDate')
temp = temp.sort()
temp['dataValue'].plot(figsize=(15,6),grid=True)


compare={}
for index in temp['dataValue'].index:
    year = index[:4]
    month = index[5:7]
    if year not in compare.keys():
        compare.update({year:{month:temp['dataValue'][index]}})
    else:
        compare[year].update({month:temp['dataValue'][index]})
compare = pd.DataFrame(compare)

compare.plot(figsize=(20,6))
plt.legend(loc=0)

# 计算一下上面数据的季节指数
ave_k = compare.mean(axis=1)
ave = ave_k.mean()
compare['S'] = ave_k/ave
print(compare)



##  造数据观察季节性
T = np.array([4,7,8,4,1,1,3])
data = T
for i in range(1,20):
    x = T + i
    data = np.append(data,x)
plt.figure(figsize=(10,6))
plt.plot(data)
#计算季节指数：
ave = data.mean()
term = len(T)
numOfTerm = len(data)/len(T)
S = []
for i in range(term):
    s = 0
    for j in range(numOfTerm):
        s += data[i+j*term]
    S.append(s/numOfTerm)
S = S/ave
print(S)

#季节性差分
dataDiff = temp['dataValue'].diff(12)[12:]
dataDiff.plot(figsize=(15,6))

diffdiff = dataDiff.diff()[1:]
diffdiff.plot(figsize=(15,6))

t = sm.tsa.stattools.adfuller(diffdiff)  # ADF检验
print( "p-value:   ",t[1])

# 多重季节性模型
# 建模
data = diffdiff[:-5]  # 最后5个用来预测
test = diffdiff[-5:]
var = data.var()
length = len(data)
acf,q,p = sm.tsa.acf(data,nlags =length,qstat=True)  ## 计算自相关系数 及p-value
out = np.c_[range(1,length), acf[1:], q, p]
output=pd.DataFrame(out, columns=['lag', "AC", "Q", "P-value"])
output = output.set_index('lag')
print( 'ACF1',output.ix[1]['AC'])
print ('ACF12',output.ix[12]['AC'])


cov_1 = output.ix[1]['AC']*var
cov_12 = output.ix[12]['AC']*var
# 求二元一次方程，返回绝对值大于1的解
def calc(a,b,c):
    if b**2-4*a*c<0:
        return np.nan
    elif b**2-4*a*c==0:
        return -b/(2*a)
    else:
        if abs((-b+(b**2-4*a*c)**(1/2))/(2*a))<1 :
            return (-b+(b**2-4*a*c)**(1/2))/(2*a)
        elif abs((-b-(b**2-4*a*c)**(1/2))/(2*a))<1:
            return (-b-(b**2-4*a*c)**(1/2))/(2*a)
        else:
            return np.nan

print (var/cov_1,var/cov_12)
theta = calc(1,var/cov_1,1)
Theta = calc(1,var/cov_12,1)
print (theta,Theta)
# 未能求出满足要求的θ和Θ的值。。。也就是序列难以用以上模型表达，即使用其他方法求出最优估计，应该满足的3条性质也无法满足
# 另一方面，在求季节指数时我们发现该序列季节性不强，这也是原因之一。



# 其他模型综合分析模型（加法模型、乘法模型、混合模型）

# 建模
T = np.array([4,7,8,4,1,1,3])
data = T
for i in range(1,20):
    temp = T + i
    data = np.append(data,temp)
plt.figure(figsize=(10,6))
plt.plot(data)

seasonRemove = pd.rolling_mean(data,7)
st = data - seasonRemove
plt.figure(figsize=(10,5))
plt.plot(seasonRemove,label = 'seasonRemove')
plt.plot(st,label = 'st')
plt.legend(loc=0)

# 去除季节性后的序列，我们用最小二乘来拟合
from sklearn import linear_model
train = np.mat(range(7,len(seasonRemove))).T
clf = linear_model.LinearRegression()
clf.fit(train,seasonRemove[7:])
k = clf.coef_
print('k=',k)
x = range(7,len(seasonRemove))
y = k*x
b = (seasonRemove[7:] - y).mean()
print('b=',b)
y = y +b
plt.figure(figsize=(10,6))
plt.plot(x,y,label='Tt')
plt.plot(seasonRemove,label='seasonal removed')
plt.legend(loc=0)

# 接着根据残差计算It
It=[]
for i in range(len(seasonRemove[7:])):
    It.append(y[i]-seasonRemove[7+i])
plt.figure(figsize=(10,6))
plt.plot(It,label='It')
plt.legend()

result = sm.tsa.seasonal_decompose(np.array(data),model='additive',freq=1) #加法模型
plt.figure(figsize=(15,8))
plt.subplot(411)
plt.plot(result.observed, label='Original')
plt.legend(loc=0)
plt.subplot(412)
plt.plot(result.trend, label='Trend')
plt.legend(loc=0)
plt.subplot(413)
plt.plot(result.seasonal,label='Seasonality')
plt.legend(loc=0)
plt.subplot(414)
plt.plot(result.resid, label='Residuals')
plt.legend(loc=0)