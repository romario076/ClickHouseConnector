
from clickhouse_driver import Client
import pandas as pd

class pandasConnector(object):
    def __init__(self, host, db):
        self.db= db
        self.conn = Client(host)
        self.useDB()
        self.checkTables()

    def useDB(self):
        self.dbCorrect= True
        try:
            useDb = self.conn.execute("use " + str(self.db), columnar=True)
        except:
            self.dbCorrect= False
            print("Wrong DB!")

    def checkTables(self):
        if self.dbCorrect:
             self.tables= self.conn.execute("show tables", columnar=True)
             if len(self.tables)>0:
                 self.tables= list(self.tables[0])

    def read_sql_query(self, query, tableName):
        dataDataFrame= pd.DataFrame()
        if self.dbCorrect:
            if len(self.tables)>0:
                if tableName in self.tables:
                    dataList = self.conn.execute(query, columnar=True,  with_column_types=True)
                    if len(dataList)>0:
                        dataAll= dataList[0]
                        if len(dataAll)>0:
                            columns = [x[0] for x in dataList[1]]
                            #columns = self.conn.execute("DESC TABLE "+self.db+"."+tableName , columnar=True)
                            dataDataFrame= pd.DataFrame(dataAll).T
                            #columns = columns[0]
                            dataDataFrame.columns = columns
                else:
                    print("Wrong table name!")
        return dataDataFrame



# symbols= ["BTC-USD", "LTC-USD", "LTC-BTC"]
# date= '2018-01-19'
# t1="09:20:00"
# t2="17:00:00"
# host="10.12.1.60"
# db="tick"
#
# conn = Client(host)
# conn.execute("use " + str(db), columnar=True)
# tt= conn.execute("select Ticker, Time, tPrice from Crypto limit 10", columnar=True, with_column_types=True)
# columns= [x[0] for x in tt[1]]
#
# ss= "','".join(symbols)
# conn = pandasConnector(host="10.12.1.60", db="tick")
# query= "select concat(cast(XTime as char),'.',cast(XTimeMicro as char)) as Time1, \
#             Ticker, Type, Level, L1_AskP, L1_BidP from Crypto where \
#         TradeDate='"+date+"' and Ticker in ('"+ss+"') and (Level=1) limit 10"
#data= conn.read_sql_query(query, tableName="Crypto")

