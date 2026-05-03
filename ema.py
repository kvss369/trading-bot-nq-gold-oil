import pandas as pd

def calculate_multiple_emas(data, periods=[9, 21, 50, 200]):
    """
    Calculate multiple Exponential Moving Averages (EMA) based on the given periods.

    Parameters:
    data (pd.Series): The data series to calculate EMAs on.
    periods (list): A list of periods for which to calculate EMAs.

    Returns:
    dict: A dictionary containing the EMAs for the specified periods.
    """
    emas = {}
    for period in periods:
        emas[period] = data.ewm(span=period, adjust=False).mean()
    return emas

# Example usage:
# data = pd.Series([...])  # Add your data series here
# emas = calculate_multiple_emas(data)
# print(emas)