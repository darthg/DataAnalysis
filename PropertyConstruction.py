# coding=utf-8
import pymysql
import numpy
import pandas
import sklearn.decomposition as PCA

conn=pymysql.connect(host="127.0.0.1",user="root",passwd="coldfallen525",db="world")
sql="select price,comment from taob"
data=pandas.read_sql(sql)
data.describe()

ch=data[u"comment"]/data["hits"]
data[u"评点比"]=ch#构造一列新的属性，评点比
filepath="./hexun.xls"
data.to_excel(filepath,index=False)

#---主成分分析进行中-------------

paca1=PCA()
paca1.fit(data)  #加载数据
characteristic=paca1.components_#返回模型中各个特征量
print(characteristic)




