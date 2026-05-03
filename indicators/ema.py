def calculate_ema(prices, period):
    if len(prices) < period:
        raise ValueError('Not enough data points to calculate EMA.')
    multiplier = 2 / (period + 1)
    ema_values = [sum(prices[:period]) / period]  # Starting average
    for price in prices[period:]:
        ema = (price - ema_values[-1]) * multiplier + ema_values[-1]
        ema_values.append(ema)
    return ema_values
