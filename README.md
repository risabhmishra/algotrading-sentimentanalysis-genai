# AlgoTrading with Sentiment Analysis and Backtesting using GenAI

This project provides a framework for sentiment analysis on stock market data and conducting backtesting using Backtrader. It includes functions for downloading stock data from Yahoo Finance, preprocessing sentiment data, and running backtests with customizable strategies.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Configuration](#configuration)
  - [Run Backtest](#run-backtest)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to provide a streamlined workflow for analyzing stock market sentiment and backtesting trading strategies. It leverages [Backtrader](https://www.backtrader.com/) for backtesting and [yfinance](https://pypi.org/project/yfinance/) for downloading stock data.

## Features

- Download stock data from Yahoo Finance.
- Preprocess sentiment data and merge it with stock data.
- Run backtests with customizable strategies using Backtrader.
- Analyze backtest results with various performance metrics.

## Requirements

- Python 3.6+
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/stock-sentiment-backtesting.git
   cd stock-sentiment-backtesting
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Configuration

Edit the configuration parameters in `main.py` to customize the stock, date range, and other settings for your analysis.

```python
STOCK_TICKER = 'AAPL'
START_DATE = '2022-03-21'
END_DATE = '2022-12-31'
SENTIMENT_DATA_PATH = 'data/stock_sentiment_data.csv'
```

### Run Backtest

Execute the main script to run the backtest:

```bash
python main.py
```

The backtest results, including performance metrics, will be displayed in the console.

## Project Structure

```
algotrading-sentimentanalysis-genai/
├── alpaca/
│   └── client.py
├── data/
│   └── stock_sentiment_data.csv
│   └── ...
├── llms/
│   └── llama_llm.py
│   └── openai_llm.py
├── processor/
│   └── stock_data_processor.py
├── runner/
│   └── backtest_runner.py
├── sentiment_analysis/
│   └── sentiment_analysis_pipeline.py
├── strategies/
│   └── technical_only_strategy/
│   └── technical_with_sentiment_strategy/
├── output/
│   └── ...
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
└── venv/
    └── ...
```

# Getting Client Secrets and Configurations

## 1. Alpaca REST Client

### Requirements:
- Python 3.7 or later
- [Alpaca account](https://alpaca.markets/)
- API key ID and secret (available in your Alpaca account dashboard)

### Configuration:

1. Install the Alpaca Python library:

   ```bash
   pip install alpaca-trade-api
   ```

2. Use the API key in your code:

   ```python
   from alpaca_trade_api import REST

   alpaca_api_key = "YOUR_API_KEY"
   alpaca_secret_key = "YOUR_SECRET_KEY"

   rest_client = REST(alpaca_api_key, alpaca_secret_key)
   ```

## 2. OpenAI LLM Client

### Requirements:
- Python 3.6 or later
- [OpenAI account](https://beta.openai.com/signup)
- API key (available in your OpenAI account dashboard)

### Installation:

1. Install the official OpenAI library:

   ```bash
   pip install openai
   ```

2. Set your API key as an environment variable:

   ```bash
   export OPENAI_API_KEY="YOUR_API_KEY"
   ```

   Alternatively, provide it directly in your code:

   ```python
   import openai

   openai.api_key = "YOUR_API_KEY"
   ```

## 3. Llama LLM Client

### Requirements:
- Python 3.7 or later
- [Hugging Face account](https://huggingface.co/join) with an access token
- Token with access to the desired Llama model

### Installation:

1. Install necessary libraries:

   ```bash
   pip install transformers
   ```

2. Set your Hugging Face token as an environment variable:

   ```bash
   export HF_ACCESS_TOKEN="YOUR_TOKEN"
   ```

## Important:
Use caution when handling API keys and tokens. Avoid exposing them in public repositories or sharing them without proper security measures.

## Adding to README:
Feel free to include this information in your README for comprehensive setup instructions.

- **main.py:** 
  Contains the main script for running backtests and strategy definition.

- **data:** 
  Directory for storing data files, including stock and sentiment data.

- **output:** 
  Directory for saving backtest results and plots.

- **llms:** 
  Contains OpenAI and Llama clients for sentiment analysis.

- **processor:** 
  Contains stock data processor for preprocessing stock news and sentiment data.

- **runner:** 
  Contains backtest runner class for backtesting using cerebro and backtrader.

- **sentiment_analysis:** 
  Contains transformer pipeline for sentiment analysis on news data.

- **strategies:** 
  Contains code for technical only strategy and technical with sentiment analysis strategy.

- **.gitignore:** 
  Specifies files and directories to be ignored by version control.

- **README.md:** 
  Project documentation.

- **requirements.txt:** 
  List of Python dependencies.


## Contributing

Contributions are welcome! Please follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

