# indikator.py

def hitung_ema(data, period=20):
    """
    Menghitung EMA dari data closing price.
    """
    if len(data) < period:
        return None
    ema = []
    k = 2 / (period + 1)
    ema.append(sum(data[:period]) / period)
    for price in data[period:]:
        ema.append((price - ema[-1]) * k + ema[-1])
    return ema


def hitung_rsi(data, period=14):
    """
    Menghitung RSI dari data closing price.
    """
    if len(data) < period + 1:
        return None
    gains = []
    losses = []
    for i in range(1, period + 1):
        delta = data[i] - data[i - 1]
        if delta > 0:
            gains.append(delta)
            losses.append(0)
        else:
            gains.append(0)
            losses.append(abs(delta))

    avg_gain = sum(gains) / period
    avg_loss = sum(losses) / period

    rs = avg_gain / avg_loss if avg_loss != 0 else 0
    rsi = 100 - (100 / (1 + rs))
    return rsi
