
from sqlalchemy.types import Integer, Text, String, DateTime, Float
from datetime import datetime
from DataConnection.StockData import StockDataFrame as SDF
from DataConnection.dbconnect import DBConnect


StockData = SDF('AAPL')
StockData.get_historical(datetime(2018, 1, 1), datetime(2020, 1, 1))

df = StockData.data

df.to_sql(
    DBConnect.table,
    DBConnect.engine,
    if_exists='replace',
    index=False,
    chunksize=500,
    dtype={
        "spot_id": Integer,
        "Date": DateTime,
        "Open": Float,
        "High":  Float,
        "Low": Float,
        "Close": Float,
        "Volume": Integer
    }
)

