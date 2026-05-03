def find_support_resistance(prices, window=5):
    """
    Find support and resistance levels using local highs and lows.
    window: number of candles to look left and right for local extremes.
    """
    if len(prices) < 2 * window + 1:
        raise ValueError('Not enough price data.')
    
    support_levels = []
    resistance_levels = []
    
    for i in range(window, len(prices) - window):
        is_local_low = all(prices[i] <= prices[j] for j in range(i - window, i + window + 1))
        is_local_high = all(prices[i] >= prices[j] for j in range(i - window, i + window + 1))
        
        if is_local_low:
            support_levels.append((i, prices[i]))
        if is_local_high:
            resistance_levels.append((i, prices[i]))
    
    return support_levels, resistance_levels

def nearest_support_resistance(current_price, support_levels, resistance_levels):
    """
    Find the nearest support below and resistance above the current price.
    """
    support = None
    resistance = None
    
    for _, level in support_levels:
        if level < current_price:
            if support is None or level > support:
                support = level
    
    for _, level in resistance_levels:
        if level > current_price:
            if resistance is None or level < resistance:
                resistance = level
    
    return support, resistance
