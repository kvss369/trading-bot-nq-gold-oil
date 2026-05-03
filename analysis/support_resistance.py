def calculate_support_resistance(prices):
    """
    Calculate support and resistance levels based on pivot points and price action.
    """
    pivot_point = (max(prices) + min(prices) + prices[-1]) / 3
    support_level = 2 * pivot_point - max(prices)
    resistance_level = 2 * pivot_point - min(prices)
    return support_level, resistance_level

# Example usage
prices = [100, 102, 103, 101, 99, 98, 95]
support, resistance = calculate_support_resistance(prices)
print(f'Support: {support}, Resistance: {resistance}')