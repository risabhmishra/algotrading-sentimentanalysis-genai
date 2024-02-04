import yfinance as yf
import pandas as pd


class StockDataProcessor:
    def __init__(self, stock_ticker, start_date, end_date, sentiment_data_path):
        self.stock_ticker = stock_ticker
        self.start_date = start_date
        self.end_date = end_date
        self.sentiment_data_path = sentiment_data_path
        self.data = self.download_stock_data()

    def download_stock_data(self):
        """
        Download stock data from Yahoo Finance.

        Returns:
            pd.DataFrame: Stock data.
        """
        return yf.download(self.stock_ticker, start=self.start_date, end=self.end_date)

    def preprocess_sentiment_data(self):
        """
        Preprocess sentiment data and merge with stock data.

        Returns:
            pd.DataFrame: Merged DataFrame.
        """
        sentiment_data = pd.read_csv(self.sentiment_data_path)

        # Create a column for buy/sell signals based on sentiment
        sentiment_data['signal'] = 0
        sentiment_data.loc[sentiment_data['sentiment'] == ' Positive', 'signal'] = 1
        sentiment_data.loc[sentiment_data['sentiment'] == ' Negative', 'signal'] = -1

        # Assuming df is your existing DataFrame
        sentiment_data['timestamp'] = pd.to_datetime(sentiment_data['timestamp']).dt.date

        # Group by day and sum up 'Signal' values
        sentiment_daily_sum = sentiment_data.groupby('timestamp')['signal'].sum().reset_index()
        sentiment_daily_sum = sentiment_daily_sum.rename(columns={'timestamp': 'date', 'signal': 'signal'})

        sentiment_daily_sum['date'] = pd.to_datetime(sentiment_daily_sum['date'])

        # sentiment_daily_sum.to_csv('sentiment_daily_sum.csv')

        # Merge DataFrames on 'Date'
        merged_df = pd.merge(self.data, sentiment_daily_sum, left_index=True, right_on='date', how='left')
        merged_df.set_index('date', inplace=True)

        # merged_df.to_csv('merged_df.csv')

        return sentiment_data
