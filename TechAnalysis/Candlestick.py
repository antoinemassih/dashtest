import talib
import pandas as pd


class CandlePattern:
    data = pd.DataFrame()
    bearishCandles = []
    bullishCandles = []
    pattern = ''

    def engulfing(self, data):
        self.data = data
        self.pattern = 'engulfing'
        candles = talib.CDLENGULFING(data['open'], data['high'], data['low'], data['close'])
        for index,c in enumerate(candles):
            if c == 100:
                self.bullishCandles.append(index)
            if c == -100:
                self.bearishCandles.append(index)

# CDLENGULFING
