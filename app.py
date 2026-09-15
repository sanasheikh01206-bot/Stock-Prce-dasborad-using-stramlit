import pandas as pd
import streamlit as st
import datetime as dt
import yfinance as yf

st.markdown("# Stock Price Chart")

col1,col2 = st.columns(2)

with col1:
    start_date = st.date_input("Please enter start date",dt.date(2026,9,1))
with col2:
    end_date = st.date_input("Please enter end date",dt.date(2026,9,14))

ticker_symbol = st.text_input("Please Enter Stock Symbol","AAPL",key = "placeholder")



ticker_data = yf.Ticker(ticker_symbol)
ticker_df = ticker_data.history(start = start_date, end = end_date)

st.write(f"{ticker_symbol}'s EOD Prices")
st.dataframe(ticker_df)

st.write(f"Daily Closing Price Chart ")

st.line_chart(ticker_df.Close)