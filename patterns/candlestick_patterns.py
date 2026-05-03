def identify_engulfing(candles):
    """
    Identify engulfing candlestick patterns.
    Bullish: Small candle followed by larger candle that engulfs it (opens lower, closes higher).
    Bearish: Small candle followed by larger candle that engulfs it (opens higher, closes lower).
    Returns: 'bullish_engulfing', 'bearish_engulfing', or None
    """
    if len(candles) < 2:
        return None
    
    prev_candle = candles[-2]
    current_candle = candles[-1]
    
    prev_open, prev_close, prev_high, prev_low = prev_candle['open'], prev_candle['close'], prev_candle['high'], prev_candle['low']
    curr_open, curr_close, curr_high, curr_low = current_candle['open'], current_candle['close'], current_candle['high'], current_candle['low']
    
    if curr_open < prev_low and curr_close > prev_high:
        return 'bullish_engulfing'
    elif curr_open > prev_high and curr_close < prev_low:
        return 'bearish_engulfing'
    
    return None

def identify_hammer(candle):
    """
    Identify hammer candlestick pattern (reversal signal).
    Small body at top, long lower wick.
    """
    open_price = candle['open']
    close_price = candle['close']
    high_price = candle['high']
    low_price = candle['low']
    
    body = abs(close_price - open_price)
    lower_wick = min(open_price, close_price) - low_price
    upper_wick = high_price - max(open_price, close_price)
    
    if lower_wick > 2 * body and upper_wick < 0.5 * body:
        return 'hammer'
    
    return None

def identify_doji(candle, threshold=0.1):
    """
    Identify Doji candlestick pattern (indecision).
    Open and close prices are nearly equal.
    """
    open_price = candle['open']
    close_price = candle['close']
    high_price = candle['high']
    low_price = candle['low']
    
    body = abs(close_price - open_price)
    total_range = high_price - low_price
    
    if total_range > 0 and body / total_range < threshold:
        return 'doji'
    
    return None

def identify_pin_bar(candle):
    """
    Identify Pin Bar (Pinocchio) pattern.
    Long wick on one end, small body on the other.
    """
    open_price = candle['open']
    close_price = candle['close']
    high_price = candle['high']
    low_price = candle['low']
    
    body = abs(close_price - open_price)
    upper_wick = high_price - max(open_price, close_price)
    lower_wick = min(open_price, close_price) - low_price
    
    if (upper_wick > 2 * body and lower_wick < 0.5 * body) or (lower_wick > 2 * body and upper_wick < 0.5 * body):
        return 'pin_bar'
    
    return None
