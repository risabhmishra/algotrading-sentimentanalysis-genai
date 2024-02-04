from openai import OpenAI


class OpenAISentimentAnalysis:
    """
    A class for sentiment analysis using the OpenAI GPT-3.5 Turbo model.

    Attributes:
    - api_key (str): OpenAI API key for authentication.
    - client (OpenAI): OpenAI client for making API requests.
    """

    _instance = None

    def __new__(cls, api_key):
        """
        Creates a singleton instance of OpenAISentimentAnalysis.

        Args:
        - api_key (str): OpenAI API key for authentication.

        Returns:
        - OpenAISentimentAnalysis: An instance of the OpenAISentimentAnalysis class.
        """
        if not cls._instance:
            cls._instance = super(OpenAISentimentAnalysis, cls).__new__(cls)
            # Initialize the OpenAI client
            cls._instance.client = OpenAI(api_key=api_key)
        return cls._instance

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the provided text using OpenAI GPT-3.5 Turbo.

        Args:
        - text (str): Text to analyze.

        Returns:
        - str: Sentiment analysis result.
        """
        prompt = f"Sentiment analysis of the following text: '{text}'"
        response = self.client.completions.create(
            model='gpt-3.5-turbo-instruct',
            prompt=prompt,
            max_tokens=10,
            temperature=0
        )
        # Extract sentiment from the response
        sentiment = response.choices[0].text.strip()
        return sentiment


# Example usage
if __name__ == "__main__":
    # Add your OpenAI API key here
    api_key = "your_openai_api_key"

    # Create an instance of the OpenAISentimentAnalysis class
    sentiment_analysis = OpenAISentimentAnalysis(api_key)

    # Example text for sentiment analysis
    text_example = "girls are fighting for feminism but for not correct reasons"

    # Analyze sentiment using the singleton instance
    sentiment_result = sentiment_analysis.analyze_sentiment(text_example)

    # Use the sentiment as needed
    if sentiment_result == "Positive":
        print("😊")
    elif sentiment_result == "Negative":
        print("😔")
    else:
        print("😐")
