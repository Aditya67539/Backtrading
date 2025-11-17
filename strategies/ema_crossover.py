from indicators.ema import ema
from utils.plot import Plot

def ema_crossover(series, short_window=50, long_window=200):
    short_ema = ema(series["Price"], short_window)
    long_ema = ema(series["Price"], long_window)

    pt = Plot()
    pt.add(series["Date"], series["Price"])
    pt.add(series["Date"], short_ema)
    pt.add(series["Date"], long_ema)
    pt.plot()

    signal = (short_ema > long_ema).astype(int)
    signal = signal.diff().fillna(0)

    signal[signal > 0] = 1
    signal[signal < 0] = -1

    return signal