def analyze_volume(volumes, period=20):
    """
    Analyze volume trends and identify unusual volume spikes.
    Returns average volume and list of spike indicators.
    """
    if len(volumes) < period:
        raise ValueError('Not enough volume data points.')
    
    average_volume = sum(volumes[-period:]) / period
    volume_spikes = []
    
    for vol in volumes:
        spike_ratio = vol / average_volume if average_volume > 0 else 0
        volume_spikes.append(spike_ratio)
    
    return average_volume, volume_spikes

def volume_confirmation(volume, avg_volume, threshold=1.5):
    """
    Check if volume confirms a trading signal (spike above average).
    """
    return volume > avg_volume * threshold
