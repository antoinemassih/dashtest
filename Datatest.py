from datetime import datetime
from DataConnection.StockData import StockDataFrame as SDF
from DataConnection.PandasMySQl import DFDBObject as SDFDB

StockData = SDF('AAPL')
StockData.get_historical(datetime(2018, 1, 1), datetime(2020, 1, 1))

df = StockData.data
dataconnection = SDFDB(df)
dataconnection.SendToDB()

