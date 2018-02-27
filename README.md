# ClickHouseConnector
ClickHouse connector for python using pandas.

Using your query returns pandas DataFrame.

repo: https://github.com/mymarilyn/clickhouse-driver

### Installing:
```
git clone https://github.com/mymarilyn/clickhouse-driver

After that, put all contents into: C:\Users\UserName\Anaconda2\Lib\site-packages
```

### Requirements:
* anaconda 2+
* pandas

### Usage:
```
from clickhouse_driver.pandasConnector import pandasConnector as clickConn

conn = clickConn(host="host", db="dbName")
data1= conn.read_sql_query("select * from Tbl limit 10", tableName="Tbl")
data2= conn.read_sql_query("select * from Tbl  where Date> '2018-01-02' limit 10", tableName="Tbl")
data3= conn.read_sql_query("select column1, column2 from Tbl2 limit 10", tableName="Tbl2")
```
