def analyze_liquidity(volumes, prices, period=20):
    """
    Analyze liquidity by examining volume relative to price movement.
    Low volume + high price movement = low liquidity (risky).
    High volume + small price movement = high liquidity (good).
    """
    if len(volumes) < period or len(prices) < period:
        raise ValueError('Not enough data for liquidity analysis.')
    
    recent_volumes = volumes[-period:]
    recent_prices = prices[-period:]
    
    avg_volume = sum(recent_volumes) / period
    price_range = max(recent_prices) - min(recent_prices)
    
    if price_range == 0:
        liquidity_ratio = 0
    else:
        liquidity_ratio = avg_volume / price_range
    
    return liquidity_ratio, avg_volume

def is_liquid(liquidity_ratio, min_threshold=100):
    """
    Determine if an asset has sufficient liquidity for trading.
    Higher ratio = better liquidity.
    """
    return liquidity_ratio > min_threshold
