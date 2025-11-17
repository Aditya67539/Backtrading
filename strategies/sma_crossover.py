from indicators.sma import sma

def sma_crossover(series, short_window=50, long_window=200):
    short_sma = sma(series["Price"], short_window)
    long_sma = sma(series["Price"], long_window)

    signal = (short_sma > long_sma).astype(int)
    signal = signal.diff().fillna(0)

    signal[signal > 0] = 1
    signal[signal < 0] = -1

    return signal