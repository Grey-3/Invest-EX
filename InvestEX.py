import requests

def get_price_data(crypto, time):
    # Set the Coingecko API endpoint
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days={time}"
    
    # Make a request to the Coingecko API
    response = requests.get(url)
    
    # Print the response JSON
    print(response.json())
    
    # Parse the response JSON
    data = response.json()
    
    # Extract the price data
    if 'prices' in data:
        prices = [p[1] for p in data['prices']]
    else:
        print(f"Error: could not retrieve price data for {crypto} with time {time}")
        prices = []
    
    return prices

def predict_price(prices, n):
    # Calculate the moving average of the price data
    moving_average = sum(prices[-n:]) / n
    
    # Predict the next price based on the moving average
    next_price = moving_average * 2 - prices[-n]
    
    return next_price

if __name__ == "__main__":
    # Prompt the user to enter the required inputs
    crypto = input("Enter the name of the cryptocurrency: ")
    time = input("Enter the time period to fetch data for (1, 7, 30, or 365 days): ")

    # Fetch price data for the specified cryptocurrency and time period
    prices = get_price_data(crypto, time)

    # Check if price data is available
    if len(prices) > 0:
        # Predict the next price based on the moving average
        next_price = predict_price(prices, 7)

        # Print the predicted price
        print(f"The predicted price of {crypto} in the next {time} days is ${next_price:.2f}")
