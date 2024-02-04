import backtrader as bt


class SentimentData(bt.feeds.GenericCSVData):
    """
    Custom Backtrader data feed class for sentiment data.

    Parameters:
    - dtformat (str): Date format for parsing the date column.
    - date (int): Column index for the date in the CSV file.
    - signal (int): Column index for the sentiment signal in the CSV file.
    - openinterest (int): Column index for the open interest in the CSV file.
    """

    lines = ('signal',)

    params = (
        ('dtformat', '%Y-%m-%d'),
        ('date', 0),
        ('signal', 7),
        ('openinterest', -1)
    )
