def calculate_vwap(prices, volumes, period=20):
    """
    Calculate Volume Weighted Average Price (VWAP).
    VWAP = Cumulative(Typical Price × Volume) / Cumulative Volume
    """
    if len(prices) != len(volumes):
        raise ValueError('Prices and volumes must have the same length.')
    
    vwap_values = []
    cumulative_tp_volume = 0
    cumulative_volume = 0
    
    for i in range(len(prices)):
        typical_price = prices[i]
        cumulative_tp_volume += typical_price * volumes[i]
        cumulative_volume += volumes[i]
        
        if cumulative_volume > 0:
            vwap = cumulative_tp_volume / cumulative_volume
            vwap_values.append(vwap)
        else:
            vwap_values.append(None)
    
    return vwap_values
