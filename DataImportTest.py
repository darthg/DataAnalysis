import pandas
import pymysql
'''
#--------------导入CSV格式数据---------------
fr=pandas.read_csv(r"E:\GitHub\DATAIMPORT.csv",encoding='GBK')#打开文件路径不能包含中文名，编码要选择GKB才能正确解析中文


#--------------导入xls格式数据---------------
fr2=pandas.read_excel(r"E:\GitHub\DATAIMPORT.csv",encoding='GBK')
fr.sort_values(by="")#按照某一列排序

#---------导入mysql数据--------------------------
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="coldfallen525",db="world")
sql="select * from city"
k=pandas.read_sql(sql,conn)
print(k)
'''

#------------导入HTML网页
f=pandas.read_html("http://www.114best.com/dh/114.aspx?w=02155394800")
print(f)


#---------导入文本数据--------------------
pandas.read_table()