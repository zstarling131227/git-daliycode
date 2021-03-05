import time
import numpy


def singleNumber1(nums: list) -> list:
    start = time.clock()
    d = dict()
    for i in nums:
        if not i in d.keys():
            d[i] = 0
        d[i] += 1
    r = list()
    for i in d.keys():
        if (d[i] == 1):
            r.append(i)
    end = time.clock()
    print('singleNumber1程序执行时间: ', end - start)
    return r


def singleNumber2(nums: list) -> list:
    start = time.clock()
    r = list()
    for i in set(nums):
        if nums.count(i) == 1:
            r.append(i)
    end = time.clock()
    print('singleNumber2程序执行时间: ', end - start)
    return r


list1 = list("20725316")
data1=list(numpy.random.randint(1,1001,10000))
print(len(data1))
print("singleNumber1", singleNumber1(data1))
print("singleNumber2", singleNumber2(data1))
print("singleNumber1", singleNumber1(list1))
print("singleNumber2", singleNumber2(list(list1)))

print(list1[-1])
print(list1[:])



