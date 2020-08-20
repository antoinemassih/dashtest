import talib
import pandas as pd


class CandlePattern:
    data = pd.DataFrame()

    def engulfing(self,data):
        self.data = data
        candles = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
        for c in candles:
            if c!=0:






for c in candles:
        print(c)

#CDLENGULFING

