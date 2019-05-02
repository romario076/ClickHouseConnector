
from clickhouse_driver import Client
import pandas as pd

class pandasConnector(object):
    def __init__(self, host, user='default', password='', db=''):
        self.db= db
        self.conn = Client(host=host, user=user, password=password)
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
        return (dataDataFrame)
