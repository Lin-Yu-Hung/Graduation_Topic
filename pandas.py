import pymysql
import pandas as pd

 # 顯示所有列
pd.set_option('display.max_columns', None)
# 顯示所有行
pd.set_option('display.max_rows', None)
# 設定value的顯示長度為100，預設為50
pd.set_option('max_colwidth', 100)

connection = pymysql.connect(
        host='localhost',
        user='root',
        passwd='0000',
        db='toad',
    )
sql= 'SELECT name FROM func3api_cpu;'
df = pd.read_sql(sql, connection)
df = pd.DataFrame(df)
print(df)
