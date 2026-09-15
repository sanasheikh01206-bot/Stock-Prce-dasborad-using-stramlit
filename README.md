# Stock Price Dashboard 📈

An interactive financial web application built with Streamlit and Python. This dashboard fetches real-time and historical End-of-Day (EOD) market data for any publicly traded ticker using the `yfinance` API and visualizes closing price movements over customizable date ranges.

---

## Features

* **Custom Date Range Selection:** Choose specific start and end dates via interactive date pickers.
* **Ticker Search:** Query any valid market ticker symbol (e.g., `AAPL`, `MSFT`, `GOOG`).
* **Detailed Market Metrics:** View tabular End-of-Day (EOD) data, including Open, High, Low, Close, and Volume.
* **Interactive Data Visualization:** Track daily price fluctuations over time using clean line charts.

---

## Tech Stack

* **Language:** Python
* **Web Framework:** [Streamlit](https://streamlit.io/)
* **Market Data API:** [yfinance](https://pypi.org/project/yfinance/)
* **Data Manipulation:** [Pandas](https://pandas.pydata.org/)

---

## Project Structure

```text
├── app.py              # Main Streamlit application logic
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation

