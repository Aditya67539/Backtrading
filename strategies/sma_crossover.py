from indicators.sma import sma
from utils.plot import Plot

def sma_crossover(series, short_window=50, long_window=200):
    short_sma = sma(series["Price"], short_window)
    long_sma = sma(series["Price"], long_window)

    pt = Plot()
    pt.add(series["Date"], series["Price"])
    pt.add(series["Date"], short_sma)
    pt.add(series["Date"], long_sma)
    pt.plot()

    signal = (short_sma > long_sma).astype(int)
    signal = signal.diff().fillna(0)

    signal[signal > 0] = 1
    signal[signal < 0] = -1

    return signal