# -*- coding: utf-8 -*-

# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from datetime import datetime
from DataConnection.StockData import StockDataFrame as SDF


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
StockData = SDF('AAPL')
StockData.get_historical(datetime(2018, 1, 1), datetime(2020, 1, 1))

df = StockData.data

trace = go.Ohlc(x=df['Date'],
                    open=df['open'],
                    high=df['high'],
                    low=df['low'],
                    close=df['close'])

highlight_inds = [1, 3]
track_highlight = go.Candlestick(
    x=[df['Date'][i] for i in highlight_inds],
    open=[df['open'][i] for i in highlight_inds],
    high=[df['high'][i] for i in highlight_inds],
    low=[df['low'][i] for i in highlight_inds],
    close=[df['close'][i] for i in highlight_inds],
    increasing={'line': {'color': 'yellow'}},
    decreasing={'line': {'color': 'purple'}},
    name='highlight'
)

fig = go.Figure(data=(trace,track_highlight))

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)