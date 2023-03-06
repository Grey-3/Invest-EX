from datetime import datetime
from flask import Flask, request, jsonify
from api_logging import log_request
import requests

app = Flask(__name__)

@app.route('/get_price_data', methods=['GET'])
def get_price_data():
    crypto = request.args.get('crypto')
    time = request.args.get('time')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_request(request.method, request.url, timestamp)

    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days={time}"
    
    response = requests.get(url)
    
    data = response.json()
    
    if 'prices' in data:
        prices = [p[1] for p in data['prices']]
    else:
        error = f"Error: could not retrieve price data for {crypto} with time {time}"
        return jsonify(error=error), 404
    
    return jsonify(prices=prices), 200

@app.route('/predict_price', methods=['GET'])
def predict_price():
    crypto = request.args.get('crypto')
    time = request.args.get('time')
    days = int(request.args.get('days', '7'))
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_request(request.method, request.url, timestamp)
    
    url = f"https://api.coingecko.com/api/v3/coins/{crypto}/market_chart?vs_currency=usd&days={time}"
    
    response = requests.get(url)
    
    data = response.json()
    
    if 'prices' in data:
        prices = [p[1] for p in data['prices']]
    else:
        error = f"Error: could not retrieve price data for {crypto} with time {time}"
        return jsonify(error=error), 404
    
    if len(prices) >= days:
        moving_average = sum(prices[-days:]) / days
        next_price = moving_average * 2 - prices[-days]
        return jsonify(predicted_price=next_price), 200
    else:
        error = f"Error: not enough data available to make prediction for {crypto} with time {time}"
        return jsonify(error=error), 404

if __name__ == '__main__':
    app.run(debug=True)
