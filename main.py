import os
import pandas as pd

from processor.stock_data_processor import StockDataProcessor
from runner.backtest_runner import BacktestRunner

if __name__ == '__main__':
    # Configuration
    STOCK_TICKER = 'AAPL'
    START_DATE = '2022-03-21'
    END_DATE = '2022-12-31'
    SENTIMENT_DATA_PATH = 'data/stock_sentiment_data.csv'

    # Create output directory
    os.makedirs('output', exist_ok=True)

    # Initialize the StockDataProcessor
    processor = StockDataProcessor(STOCK_TICKER, START_DATE, END_DATE, SENTIMENT_DATA_PATH)

    # Download stock data
    stock_data = processor.download_stock_data()

    # Preprocess sentiment data and merge with stock data
    sentiment_data = processor.preprocess_sentiment_data()
    merged_df = pd.merge(stock_data, sentiment_data, left_index=True, right_index=True, how='left')


    # Run backtest
    BacktestRunner.run_backtest('data/merged_df.csv', STOCK_TICKER, START_DATE, END_DATE)
