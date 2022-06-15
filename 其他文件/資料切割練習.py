import pandas as pd
from datetime import datetime
import pymysql
from sqlalchemy import create_engine
connection = pymysql.connect(
    host='localhost',
    user='root',
    passwd='0000',
    db='0306',
)


#===========================================================
sql = 'SELECT * FROM func3api_hdd where vendor = "希捷Seagate";'
df = pd.read_sql(sql, connection)
df[['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11',
    '12', '13']] = df.commodity.str.split('#', expand=True)
#=============================================================




engine = create_engine(
    "mysql+mysqldb://{}:{}@{}/{}".format('root', '0000', 'localhost:3306', '0306'))
con = engine.connect()
df.to_sql(name='hdd_希捷Seagate', con=con, if_exists='append', index=False)
