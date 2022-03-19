import yfinance as yf
import pendulum
import matplotlib.pyplot as plt

# valid periods: 1d,5d,1mo,3mo,6mo,1y,2y,5y,10y,ytd,max
# valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo

price_history = yf.Ticker('TSLA').history(period='2y', interval='1wk', actions=False)
time_series = list(price_history['Open'])

dt_list = [pendulum.parse(str(dt)).float_timestamp for dt in list(price_history.index)]

plt.style.use('dark_background')
plt.plot(dt_list, time_series, linewidth=2)
