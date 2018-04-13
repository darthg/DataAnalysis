# coding=utf-8
import matplotlib.pylab as pyl
import numpy
import numpy.random

'''
#绘制折线图/散点图 plot
x=[1,2,3,4,8]
y=[4,5,6,3,7]
#pyl.plot(x,y)#plot(x数据，y数据，图形类型)
#pyl.show()
#散点图 plot
pyl.plot(x,y,':')
pyl.show()

#pyl.plot(x,y,'c')#设置颜色
#c-cyan--青色
#m--mangent--品红
#g--green-绿色
pyl.title("我是标题")
pyl.xlabel("我是X轴标签")
pyl.ylabel("我是Y轴标签")
pyl.xlim(0,20)#轴范围
pyl.ylim(0,30)

-直线
--虚线
-.-.形式
：细小虚线

#点的样式
s--方形
h--六角形
H--六角形
*--星形



randdata=numpy.random.random_integers(1,20,10)#三个参数，最小值，最大值，生成的随机数的个数
print(randdata)'''
#生成具有正态分布的随机数
data=numpy.random.normal(5,2,100)#（平均数，Σ，个数）
print(data)


#直方图hist-----------------------
pyl.hist(data)
pyl.show()