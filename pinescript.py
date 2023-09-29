import numpy as np

def apply_transformation(data):
    result = {} 

    close = list(data['close'])
    open_ = list(data['open'])

    result['close'] = close
    result['open'] = open_

    volume_color = [(245, 245, 245) if c > o else (48, 108, 238) for c, o in zip(close, open_)]
    result['volume_color'] = volume_color

    # Simple Moving Average of Volume
    sma_length = 9
    sma_value_volume = np.convolve(list(data['volume']), np.ones(sma_length) / sma_length, mode='valid')
    result['sma_value_volume'] = sma_value_volume

    # Trend Analysis
    sma_value_trend = np.convolve(close, np.ones(sma_length) / sma_length, mode='valid')

    cross_above = np.where(sma_value_trend[:-1] < close[sma_length:], 1, 0)
    cross_below = np.where(sma_value_trend[:-1] > close[sma_length:], 1, 0)
    trend = np.where(cross_above, 1, np.where(cross_below, -1, 0))

    trend_label = np.where(trend == 1, "Uptrend", np.where(trend == -1, "Downtrend", "Consolidation"))

    arrows = np.where(trend == 1, -1, np.where(trend == -1, 1, None))
    result['sma_value_trend'] = sma_value_trend
    result['trend'] = trend
    result['trend_label'] = trend_label
    result['arrows']=arrows

    return result