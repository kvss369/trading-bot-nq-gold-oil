# Trading Bot Configuration

# Asset symbols
SYMBOLS = ['NQ', 'GOLD', 'OIL']

# Timeframes for analysis (in minutes)
TIMEFRAMES = {
    'scalping': [1, 5],
    'day_trading': [15, 30, 60]
}

# Technical Indicator Periods
EMA_PERIODS = [9, 21, 50, 200]
VWAP_PERIOD = 20
VOLUME_PERIOD = 20
LIQUIDITY_THRESHOLD = 100

# Risk Management
MAX_POSITION_SIZE = 0.02  # 2% of account per trade
STOP_LOSS_PERCENTAGE = 2.0  # 2% stop loss
TAKE_PROFIT_PERCENTAGE = 5.0  # 5% take profit
MAX_DAILY_LOSS = 5.0  # Max loss per day before stopping

# Support/Resistance Detection
SR_WINDOW = 5  # Number of candles for local extremes

# Pattern Recognition
MIN_VOLUME_SPIKE = 1.5  # 1.5x average volume

# Broker Settings (Tradovate or Interactive Brokers)
BROKER = 'TRADOVATE'  # or 'INTERACTIVE_BROKERS'
API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_API_SECRET'

# Logging
LOG_LEVEL = 'INFO'
LOG_FILE = 'trading_bot.log'
