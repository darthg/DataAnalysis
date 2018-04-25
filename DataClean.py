# coding=utf-8
#数据清洗：
#发现缺失值

import matplotlib.pylab as pyl
import pandas
import numpy
import pymysql

conn=pymysql.connect(host="127.0.0.1",user="root",passwd="coldfallen525",db="world")
sql="select * from city "
data=pandas.read_sql(sql,conn)
print(data.describe()) #浏览基本信息，寻找异常数据
print("\n")
print("数据长度为："+str(len(data)))
print("data.columns="+str(data.columns))
print("表格转置后为："+str(data.T))
print(data.T.values[1])

#----------------插补空白数值
'''
data["ID"][(data["ID"]==1)]=None
for i in data.columns:  #遍历表头，也就是获得了有几列到i
     for j in range(len(data)):#遍历每列的行数据
          if(data[i].isnull())[j]: #if data[i][j]==null:一样的吧？？
               data[i][j]="36"
'''
#异常值处理
#画散点图定位异常值
cityname=data.T.values[1]
population=data.T.values[4]
pyl.plot(cityname,population)
pyl.show()