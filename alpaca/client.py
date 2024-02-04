from alpaca_trade_api import REST


class AlpacaNewsFetcher:
    """
    A class for fetching news articles related to a specific stock from Alpaca API.

    Attributes:
    - api_key (str): Alpaca API key for authentication.
    - api_secret (str): Alpaca API secret for authentication.
    - rest_client (alpaca_trade_api.REST): Alpaca REST API client.
    """

    def __init__(self, api_key, api_secret):
        """
        Initializes the AlpacaNewsFetcher object.

        Args:
        - api_key (str): Alpaca API key for authentication.
        - api_secret (str): Alpaca API secret for authentication.
        """
        self.api_key = api_key
        self.api_secret = api_secret
        self.rest_client = REST(api_key, api_secret)

    def fetch_news(self, symbol, start_date, end_date):
        """
        Fetches news articles for a given stock symbol within a specified date range.

        Args:
        - symbol (str): Stock symbol for which news articles are to be fetched (e.g., "AAPL").
        - start_date (str): Start date of the range in the format "YYYY-MM-DD".
        - end_date (str): End date of the range in the format "YYYY-MM-DD".

        Returns:
        - list: A list of dictionaries containing relevant information for each news article.
        """
        news_articles = self.rest_client.get_news(symbol, start_date, end_date)
        formatted_news = []

        for article in news_articles:
            summary = article.summary
            title = article.headline
            timestamp = article.created_at

            relevant_info = {
                'timestamp': timestamp,
                'title': title,
                'summary': summary
            }

            formatted_news.append(relevant_info)

        return formatted_news

