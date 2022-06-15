from selenium import webdriver
import mysql.connector
import time
import random
import string
#使用quote進行中文轉碼
from urllib.parse import quote
from web_crawler import *
connection = mysql.connector.connect(host='localhost',
                                     port='3306',
                                     user='root',
                                     password='0000',
                                     database='test',)

cursor = connection.cursor()
a = [1,2,3]
print(a[1])
try:
    for i in range(10):
        i+1
        sql = 'INSERT INTO `test`.`test` (`id`,`name`, `price`, `Commodity`, `url_list`, `pc_images`) VALUES (%s,%s, %s, %s, %s, %s);'
        cursor.execute(
        sql, (i, a[i], a[i], a[i], 4, 5))

        connection.commit()
        print("成功")

except:
        connection.rollback()
        print("失敗")
