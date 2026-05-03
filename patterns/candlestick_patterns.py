import pandas as pd
import numpy as np

class CandlestickPatterns:
    def __init__(self, data):
        self.data = data

    def is_doji(self, row):
        return abs(row['Close'] - row['Open']) <= (row['High'] - row['Low']) * 0.1

    def is_hammer(self, row):
        return (row['Close'] > row['Open'] and 
                (row['Low'] - row['Open']) > 2 * (row['Close'] - row['Open']) and 
                (row['High'] - row['Close']) < (row['Close'] - row['Open']))

    def is_inverted_hammer(self, row):
        return (row['Close'] < row['Open'] and 
                (row['Low'] - row['Close']) > 2 * (row['Open'] - row['Close']) and 
                (row['High'] - row['Open']) < (row['Open'] - row['Close']))

    def is_engulfing(self, current, previous):
        return (current['Close'] > current['Open'] and 
                previous['Close'] < previous['Open'] and 
                current['Open'] < previous['Close'] and 
                current['Close'] > previous['Open'])

    def is_harami(self, current, previous):
        return (current['Close'] < current['Open'] and 
                previous['Close'] > previous['Open'] and 
                current['Open'] > previous['Close'] and 
                current['Close'] < previous['Open'])

    def is_morning_star(self, current, previous, before_previous):
        return (previous['Close'] < before_previous['Close'] and 
                current['Close'] > previous['Open'] and 
                current['Close'] > previous['Close'])

    def is_evening_star(self, current, previous, before_previous):
        return (previous['Close'] > before_previous['Close'] and 
                current['Close'] < previous['Open'] and 
                current['Close'] < previous['Close'])

    def is_three_white_soldiers(self):
        patterns = []
        for i in range(2, len(self.data)):
            if (self.data['Close'][i] > self.data['Open'][i] and 
                self.data['Close'][i-1] > self.data['Open'][i-1] and 
                self.data['Close'][i-2] > self.data['Open'][i-2] and 
                self.data['Close'][i] > self.data['Close'][i-1] and 
                self.data['Close'][i-1] > self.data['Close'][i-2]):
                patterns.append(i)
        return patterns

    def is_three_black_crows(self):
        patterns = []
        for i in range(2, len(self.data)):
            if (self.data['Close'][i] < self.data['Open'][i] and 
                self.data['Close'][i-1] < self.data['Open'][i-1] and 
                self.data['Close'][i-2] < self.data['Open'][i-2] and 
                self.data['Close'][i] < self.data['Close'][i-1] and 
                self.data['Close'][i-1] < self.data['Close'][i-2]):
                patterns.append(i)
        return patterns

    def detect_patterns(self):
        detected_patterns = {
            'doji': [],
            'hammer': [],
            'inverted_hammer': [],
            'engulfing': [],
            'harami': [],
            'morning_star': [],
            'evening_star': [],
            'three_white_soldiers': self.is_three_white_soldiers(),
            'three_black_crows': self.is_three_black_crows(),
        }
        for i in range(len(self.data)):
            if self.is_doji(self.data.iloc[i]):
                detected_patterns['doji'].append(i)
            if self.is_hammer(self.data.iloc[i]):
                detected_patterns['hammer'].append(i)
            if self.is_inverted_hammer(self.data.iloc[i]):
                detected_patterns['inverted_hammer'].append(i)
            if i > 0 and self.is_engulfing(self.data.iloc[i], self.data.iloc[i - 1]):
                detected_patterns['engulfing'].append(i)
            if i > 0 and self.is_harami(self.data.iloc[i], self.data.iloc[i - 1]):
                detected_patterns['harami'].append(i)
            if i > 1 and self.is_morning_star(self.data.iloc[i], self.data.iloc[i - 1], self.data.iloc[i - 2]):
                detected_patterns['morning_star'].append(i)
            if i > 1 and self.is_evening_star(self.data.iloc[i], self.data.iloc[i - 1], self.data.iloc[i - 2]):
                detected_patterns['evening_star'].append(i)
        return detected_patterns
