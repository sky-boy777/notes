#导入第三方库
from pymysql import connect


#链接到MySQL数据库（先打开数据库）
c=connect(host='localhost',user='root',password='root',port=3306,
          db='mysql',charset='utf8')

#创建游标对象
k=c.cursor()


#sql代码
  
k.execute('show databases')  #显示所有数据库
print(k.fetchall())







#关闭游标
k.close()

#关闭链接
c.close()
