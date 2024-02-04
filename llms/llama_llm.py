from langchain import HuggingFacePipeline, PromptTemplate, LLMChain
from transformers import AutoTokenizer
import transformers
import torch


class SentimentAnalysisWithLLM:
    """
    A class for sentiment analysis of stock market news using a Hugging Face language model.

    Attributes:
    - model (str): Hugging Face model name or path.
    - token (str): Token used for tokenization.
    - max_length (int): Maximum length of the generated text.
    - temperature (float): Sampling temperature for text generation.
    - top_k (int): Top-k sampling for text generation.
    - num_return_sequences (int): Number of sequences to generate.
    - eos_token_id (int): End of sequence token id.
    - device (str): Device on which the model will run.
    """

    def __init__(self, model, token, max_length=1000, temperature=0, top_k=10,
                 num_return_sequences=1, eos_token_id=None, device='mps'):
        """
        Initializes the SentimentAnalysisWithLLM object.

        Args:
        - model (str): Hugging Face model name or path.
        - token (str): Token used for tokenization.
        - max_length (int): Maximum length of the generated text.
        - temperature (float): Sampling temperature for text generation.
        - top_k (int): Top-k sampling for text generation.
        - num_return_sequences (int): Number of sequences to generate.
        - eos_token_id (int): End of sequence token id.
        - device (str): Device on which the model will run.
        """
        self.model = model
        self.token = token
        self.max_length = max_length
        self.temperature = temperature
        self.top_k = top_k
        self.num_return_sequences = num_return_sequences
        self.eos_token_id = eos_token_id
        self.device = device

        tokenizer = AutoTokenizer.from_pretrained(model, token=token)

        pipeline = transformers.pipeline(
            "text-generation",
            model=model,
            tokenizer=tokenizer,
            torch_dtype=torch.bfloat16,
            trust_remote_code=True,
            device_map="auto",
            max_length=max_length,
            do_sample=True,
            top_k=top_k,
            num_return_sequences=num_return_sequences,
            eos_token_id=eos_token_id,
            token=token,
            device=device
        )

        llm = HuggingFacePipeline(pipeline=pipeline, model_kwargs={'temperature': temperature})

        template = """Analyse the sentiment of the following stock market news:\n\n```{text}```\n\nSentiment:"""
        prompt = PromptTemplate(template=template, input_variables=["text"])

        self.llm_chain = LLMChain(prompt=prompt, llm=llm)

    def analyze_sentiment(self, text):
        """
        Analyzes the sentiment of the provided stock market news text.

        Args:
        - text (str): Stock market news text to analyze.

        Returns:
        - dict: A dictionary containing the sentiment analysis results.
        """
        return self.llm_chain.run(text)


# Example Usage:
model_name = "meta-llama/Llama-2-7b-chat-hf"
token = ""
sentiment_analyzer = SentimentAnalysisWithLLM(model_name, token)

stock_news_text = """Some Stock market news data of a particular stock fetched using alpaca apis"""

sentiment_result = sentiment_analyzer.analyze_sentiment(stock_news_text)
print(sentiment_result)
