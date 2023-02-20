# Invest-EX
Invest-EX is a Python program that predicts the next price of a specified cryptocurrency using the Coingecko API. It uses a moving average calculation to predict the next price.

# Features
Predicts the next price of a specified cryptocurrency using the Coingecko API.
Uses a moving average calculation to predict the next price.
User-friendly command-line interface.
Supports four different time periods: 1, 7, 30, or 365 days.

# Documentation
get_price_data(crypto, time)
Fetches price data for the specified cryptocurrency and time period.

crypto: The name of the cryptocurrency to fetch price data for.
time: The time period to fetch price data for. Must be one of the following: 1, 7, 30, or 365.
Returns a list of price data.

predict_price(prices, n)
Predicts the next price based on the moving average of the price data.

prices: A list of price data.
n: The number of prices to use in the moving average calculation.
Returns the predicted price
