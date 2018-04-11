import numpy
import pandas

'''
x=numpy.array([1,2,4,5])
x.sort()#排序
x.max()

#-----------------切片
#numpy的运行效率跟C语言一样快，比列表快很多
#数组as
print(x[1:3])
'''

##---------pandas
a=pandas.Series([8,9,2,1])
#print(a)#序列，每个数据有一个索引，并且可以给索引命名，有点像字典
print(a.index)
c=pandas.DataFrame([[1,2,3,4],[2,3,4,6]])#构建数据矩阵


d=pandas.DataFrame([[1,2,3,4],[2,3,4,6]],columns=["one","two","three","four"])#构建数据矩阵


e=pandas.DataFrame({
"one":4,
"two":[6,2,3],
} )
print("e:"+str(e))

e.head(5)#取e数据的前5行
e.tail(4)#取e数据的后4行
print(e.describe())#计数、平均、std标准差、最小值、每一列的分位数
print(e.T)#转置

