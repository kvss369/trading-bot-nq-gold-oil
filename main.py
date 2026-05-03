import sys
import logging
from datetime import datetime
from config import *
from indicators.ema import calculate_ema
from indicators.vwap import calculate_vwap
from indicators.volume import analyze_volume, volume_confirmation
from indicators.liquidity import analyze_liquidity, is_liquid
from patterns.candlestick_patterns import identify_engulfing, identify_hammer, identify_doji
from analysis.support_resistance import find_support_resistance, nearest_support_resistance

# Setup logging
logging.basicConfig(
    level=LOG_LEVEL,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

class TradingBot:
    def __init__(self):
        logger.info("Initializing Trading Bot...")
        self.symbols = SYMBOLS
        self.timeframes = TIMEFRAMES
        self.trades = []
        logger.info("Trading Bot initialized successfully!")
    
    def analyze_candles(self, candles, symbol):
        """
        Analyze candlestick data and generate trading signals.
        candles: list of dicts with keys: open, close, high, low, volume
        """
        if len(candles) < 50:
            logger.warning(f"Not enough candles for {symbol}. Need at least 50.")
            return None
        
        closes = [c['close'] for c in candles]
        volumes = [c['volume'] for c in candles]
        
        # Calculate indicators
        ema_9 = calculate_ema(closes, 9)
        ema_21 = calculate_ema(closes, 21)
        vwap = calculate_vwap(closes, volumes)
        avg_volume, volume_spikes = analyze_volume(volumes)
        liquidity_ratio, _ = analyze_liquidity(volumes, closes)
        
        # Support & Resistance
        support_levels, resistance_levels = find_support_resistance(closes)
        current_price = closes[-1]
        support, resistance = nearest_support_resistance(current_price, support_levels, resistance_levels)
        
        # Pattern Recognition
        engulfing = identify_engulfing(candles[-2:])
        hammer = identify_hammer(candles[-1])
        doji = identify_doji(candles[-1])
        
        # Check Liquidity
        liquidity_ok = is_liquid(liquidity_ratio)
        
        signal = {
            'symbol': symbol,
            'timestamp': datetime.now(),
            'current_price': current_price,
            'ema_9': ema_9[-1],
            'ema_21': ema_21[-1],
            'vwap': vwap[-1],
            'volume': volumes[-1],
            'avg_volume': avg_volume,
            'liquidity_ratio': liquidity_ratio,
            'support': support,
            'resistance': resistance,
            'pattern': engulfing or hammer or doji,
            'liquidity_ok': liquidity_ok,
            'volume_confirmed': volume_confirmation(volumes[-1], avg_volume),
            'signal': None
        }
        
        # Generate Trading Signal
        if signal['liquidity_ok'] and signal['volume_confirmed']:
            if engulfing == 'bullish_engulfing' and current_price > ema_21[-1]:
                signal['signal'] = 'BUY'
            elif engulfing == 'bearish_engulfing' and current_price < ema_21[-1]:
                signal['signal'] = 'SELL'
            elif hammer and current_price > support:
                signal['signal'] = 'BUY'
        
        return signal
    
    def log_signal(self, signal):
        """Log trading signal."""
        logger.info(f"Signal for {signal['symbol']}: {signal['signal']}")
        logger.info(f"  Price: {signal['current_price']}")
        logger.info(f"  Support: {signal['support']}, Resistance: {signal['resistance']}")
        logger.info(f"  Pattern: {signal['pattern']}")
        logger.info(f"  Liquidity OK: {signal['liquidity_ok']}")

if __name__ == '__main__':
    bot = TradingBot()
    logger.info("Trading Bot started successfully!")
