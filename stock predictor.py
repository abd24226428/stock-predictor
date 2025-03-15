import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Streamlit app title
st.title('📊 Apple vs Google Stock Performance & Product Launch Impact')

# Define ticker symbols
google_ticker = 'GOOGL'
apple_ticker = 'AAPL'

# Fetch historical stock data for the past year
start_date = "2024-01-01"
end_date = "2025-01-01"
google_data = yf.download(google_ticker, start=start_date, end=end_date)
apple_data = yf.download(apple_ticker, start=start_date, end=end_date)

# Convert index to datetime format
google_data.index = pd.to_datetime(google_data.index)
apple_data.index = pd.to_datetime(apple_data.index)

# 📌 Define major product launches for both companies
product_launches = {
    # Apple Product Launches
    "2024-09-10": ("iPhone 16", "red"),
    "2024-10-20": ("MacBook Pro M3", "blue"),
    "2024-11-05": ("iPad Pro M3", "green"),
    "2024-12-01": ("Apple Watch Series 10", "purple"),
    
    # Google Product Launches
    "2024-10-10": ("Pixel 9", "red"),
    "2024-05-14": ("Gemini 2 AI", "blue"),
    "2024-06-15": ("Nest Hub Max 2", "green"),
    "2024-08-20": ("Pixel Fold 2", "purple"),
}

# Convert product launch dates to datetime
product_launches = {pd.to_datetime(date): (product, color) for date, (product, color) in product_launches.items()}

# 📊 Plot stock performance of Google & Apple
st.subheader('📈 Stock Price Comparison: Google vs Apple')

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(google_data.index, google_data['Adj Close'], label='Google (GOOGL)', color='blue')
ax.plot(apple_data.index, apple_data['Adj Close'], label='Apple (AAPL)', color='red')

# Highlight product launches
for date, (product, color) in product_launches.items():
    if date in google_data.index or date in apple_data.index:
        ax.axvline(x=date, color=color, linestyle='--', alpha=0.7)
        ax.text(date, max(apple_data['Adj Close'].max(), google_data['Adj Close'].max()) * 0.9, 
                product, rotation=90, fontsize=9, color=color)

# Set labels
ax.set_xlabel('Date')
ax.set_ylabel('Adjusted Close Price (USD)')
ax.set_title('Google vs Apple Stock Performance (With Product Launches)')
ax.legend()

# Display the plot
st.pyplot(fig)

# 📊 Display raw stock data
st.subheader('🗂 Stock Data')
tab1, tab2 = st.tabs(["Google (GOOGL)", "Apple (AAPL)"])

with tab1:
    st.write(google_data.tail())

with tab2:
    st.write(apple_data.tail())