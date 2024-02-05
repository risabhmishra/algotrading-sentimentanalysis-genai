import backtrader as bt

from strategies.technical_with_sentiment_strategy.optimized_strategy import OptimizedStrategy
from strategies.technical_with_sentiment_strategy.sentiment_data import SentimentData


class BacktestRunner:
    @staticmethod
    def run_backtest(data, stock_ticker, start_date, end_date):
        """
        Run Backtrader backtest with the provided data.

        Args:
            data (pd.DataFrame): Merged stock and sentiment data.
            stock_ticker (str): Stock Ticker name.
            start_date (str): Start date for backtesting.
            end_date (str): End date for backtesting.
        """
        cerebro = bt.Cerebro()

        # Convert data to Backtrader format
        data_feed = SentimentData(dataname=data)


        # Add data to cerebro
        cerebro.adddata(data_feed)

        # Add strategy with parameters
        cerebro.addstrategy(OptimizedStrategy)

        # Set initial cash and commission
        cerebro.broker.set_cash(100000)
        cerebro.broker.setcommission(commission=0.001)

        # Add built-in analyzers
        cerebro.addanalyzer(bt.analyzers.Returns)
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, riskfreerate=0.0)
        cerebro.addanalyzer(bt.analyzers.DrawDown)
        cerebro.addanalyzer(bt.analyzers.TradeAnalyzer)
        cerebro.addanalyzer(bt.analyzers.SQN)
        cerebro.addanalyzer(bt.analyzers.VWR)
        cerebro.addanalyzer(bt.analyzers.PyFolio)

        thestrats = cerebro.run()
        thestrat = thestrats[0]

        # Get results from analyzers
        returns = thestrat.analyzers.returns.get_analysis()
        sharpe_ratio = thestrat.analyzers.sharperatio.get_analysis()
        drawdown = thestrat.analyzers.drawdown.get_analysis()
        trades = thestrat.analyzers.tradeanalyzer.get_analysis()
        sqn = thestrat.analyzers.sqn.get_analysis()
        vwr = thestrat.analyzers.vwr.get_analysis()
        pyfolio = thestrat.analyzers.getbyname('pyfolio')

        pyfolio_returns, positions, transactions, gross_lev = pyfolio.get_pf_items()

        # Print the backtesting report
        print("\n--- Backtesting Report ---")
        print("Stock Ticker: {}".format(stock_ticker))
        print("Start Date: {}".format(start_date))
        print("End Date: {}".format(end_date))
        print("Initial Portfolio Value: ${:.2f}".format(cerebro.broker.startingcash))
        print("Final Portfolio Value: ${:.2f}".format(cerebro.broker.getvalue()))
        print("Total Return: {:.2f}%".format(returns['rtot'] * 100))
        print("Annualized Return: {:.2f}%".format(returns['ravg'] * 100 * 252))  # Assuming 252 trading days in a year
        print("Max Drawdown: {:.2f}%".format(drawdown['max']['drawdown'] * 100))

        # Print Additional Metrics
        print("\n--- Additional Metrics ---")
        print("{:<15} {:<15} {:<15}".format("Value at Risk", "VWR", "Total Trades"))
        print("{:<15.2f} {:<15.4f} {:<15}".format(vwr['vwr'], vwr['vwr'], trades.total.total))