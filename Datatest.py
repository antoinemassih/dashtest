from datetime import datetime
from DataConnection.StockData import StockDataFrame as SDF
from DataConnection.PandasMySQl import DFDBObject as SDFDB
from TechAnalysis.Candlestick import CandlePattern as cpattern

StockData = SDF('AAPL')
StockData.get_historical(datetime(2018, 1, 1), datetime(2020, 1, 1))

df = StockData.data
engulfing = cpattern()
engulfing.engulfing(df)
print(engulfing.bearishCandles)
#dataconnection = SDFDB(df)
#dataconnection.SendToDB()



