# !pip install transformers
from transformers import pipeline

from alpaca.client import AlpacaNewsFetcher


class NewsSentimentAnalysis:
    """
  A class for sentiment analysis of news articles using the Transformers library.

  Attributes:
  - classifier (pipeline): Sentiment analysis pipeline from Transformers.
  """

    def __init__(self):
        """
    Initializes the NewsSentimentAnalysis object.
    """
        self.classifier = pipeline('sentiment-analysis')

    def analyze_sentiment(self, news_article):
        """
    Analyzes the sentiment of a given news article.

    Args:
    - news_article (dict): Dictionary containing 'summary', 'headline', and 'created_at' keys.

    Returns:
    - dict: A dictionary containing sentiment analysis results.
    """
        summary = news_article['summary']
        title = news_article['headline']
        timestamp = news_article['created_at']

        relevant_text = summary + title
        sentiment_result = self.classifier(relevant_text)

        analysis_result = {
            'timestamp': timestamp,
            'title': title,
            'summary': summary,
            'sentiment': sentiment_result
        }

        return analysis_result


if __name__ == '__main__':
    # Example Usage:
    # Initialize the AlpacaNewsFetcher object
    api_key = "your_api_key"
    api_secret = "your_api_secret"
    news_fetcher = AlpacaNewsFetcher(api_key, api_secret)

    # Fetch news for AAPL from 2021-01-01 to 2021-12-31
    news_data = news_fetcher.fetch_news("AAPL", "2021-01-01", "2021-12-31")

    # Initialize the NewsSentimentAnalysis object
    news_sentiment_analyzer = NewsSentimentAnalysis()

    # Assume 'news_data' is a list of news articles (each as a dictionary)
    for article in news_data:
        sentiment_analysis_result = news_sentiment_analyzer.analyze_sentiment(article)

        # Display sentiment analysis results
        print(f'Timestamp: {sentiment_analysis_result["timestamp"]}, '
              f'Title: {sentiment_analysis_result["title"]}, '
              f'Summary: {sentiment_analysis_result["summary"]}')

        print(f'Sentiment: {sentiment_analysis_result["sentiment"]}', '\n')
