# coding=utf-8
#数据规约和数据变换

#1、数据变换目的是降低数据复杂性
#2、常用数据变换：开方、平方、对数

'''
数据规范化：
1、离差标准化---消除量纲影响以及变异大小因素的影响、将一些非常大的数据变成小单位方便处理
x1=(x-min)/(max-min)

2、标准差标准化--消除单位影响以及变量自身变异影响
x1=(x-平均数)/标准差

3、小数定标规范化---消除单位影响
x1=x/10**(k)
k=log10(x的绝对值的最大值)
'''

import pymysql
import numpy
import pandas

conn=pymysql.connect(host="127.0.0.1",user="root",passwd="coldfallen525",db="world")
sql="select price,comment from taob"
data=pandas.read_sql(sql)
data.describe()
#离差标准化(最小最大标准化)
devi_st_data=(data-data.min)/(data.max-data.min)

#标准差标准化（零-均值标准化)
std_deviation_data=(data-data.mean)/data.std

#小数定标规范化--移动小数点，将数据变小
k=numpy.ceil(numpy.log10(abs(data.max)))# numpy.ceil函数作为是近1取整
data2=data/10**k


'''
离散化：
1、等宽离散化--将具有相同属性的值，分为相等宽度的 区间，将无限数据变成有限区间数据
2、等频率离散化
3、一维聚类离散化
'''
#等宽离散化
data5=data[u"price"].copy()
data6=data5.T.values#获得数据表内价格数据
k=3#设置划分区块份数
pandas.cut(data6,k,labels=["便宜","适中","奢侈"])#将所有价格都划分为

#非等宽离散化
pandas.cut(data6,[0,50,100,300,500,2000,data5.max()],labels=["","","","",""])