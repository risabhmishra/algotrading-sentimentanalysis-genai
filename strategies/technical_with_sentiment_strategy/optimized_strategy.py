import backtrader as bt


class OptimizedStrategy(bt.Strategy):
    """
    Custom Backtrader strategy with optimized parameters for moving averages, RSI, and sentiment analysis.

    Parameters:
    - fast_ma (int): Period for the fast moving average.
    - slow_ma (int): Period for the slow moving average.
    - rsi_period (int): Period for the Relative Strength Index (RSI).
    - rsi_oversold (float): RSI level considered as oversold for buying.
    - rsi_overbought (float): RSI level considered as overbought for selling.
    """

    params = (
        ("fast_ma", 20),
        ("slow_ma", 50),
        ("rsi_period", 14),
        ("rsi_oversold", 30),
        ("rsi_overbought", 70),
    )

    def __init__(self):
        """
        Initializes the OptimizedStrategy.

        Creates and initializes the required indicators and sentiment data:
        - fast_ma: Fast Simple Moving Average (SMA)
        - slow_ma: Slow Simple Moving Average (SMA)
        - rsi: Relative Strength Index (RSI)
        - sentiment: Custom sentiment data
        """
        self.fast_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.fast_ma)
        self.slow_ma = bt.indicators.SimpleMovingAverage(self.data.close, period=self.params.slow_ma)
        self.rsi = bt.indicators.RelativeStrengthIndex(period=self.params.rsi_period)
        self.sentiment = self.datas[0].signal

    def next(self):
        """
        Executes the trading logic on each iteration.

        Buys if conditions for a bullish trend are met:
        - Fast MA is above Slow MA
        - RSI is below the oversold threshold
        - Sentiment is positive

        Sells if conditions for a bearish trend are met:
        - Fast MA is below Slow MA or RSI is above the overbought threshold
        - Sentiment is negative
        """
        if self.fast_ma > self.slow_ma and self.rsi < self.params.rsi_oversold and self.sentiment > 0:
            self.buy()

        elif (self.fast_ma < self.slow_ma or self.rsi > self.params.rsi_overbought) and self.sentiment < 0:
            self.sell()
