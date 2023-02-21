# InvestEX

Invest-EX is a Python program that predicts the next price of a specified cryptocurrency using the Coingecko API. It uses a moving average calculation to predict the next price.
## Installation 

Clone the repository:
```
git clone https://github.com/grey-sz/Invest-EX.git
```
Change into the project directory:
```
cd Invest-EX
```
Install the required packages:
```
pip install -r requirements.txt
```
Start the server:
```
python app.py
```
The app should now be running on http://localhost:5000.


## API Reference

#### Example Request

```bash
  GET http://localhost:5000/get_price_data?crypto=bitcoin&time=30
```
#### Example Response

```json
  {
  "prices": [
    40214.82529032752,
    38866.16977770458,
    39108.25893500827,
    //...
  ]
}
```

| Parameter | Required     | Description                |
| :-------- | :------- | :------------------------- |
| `crypto` | `Yes` |   `The ID of the cryptocurrency (e.g. "bitcoin")` |
| `time` | `Yes` |   `The number of days of historical data to use in the prediction (e.g. 30, 60, 90)` |
| `days` | `No` |   `The number of days in the future to predict the price (default is 7)` |

#### Example Request

``` bash
GET http://localhost:5000/predict_price?crypto=bitcoin&time=30&days=7
```
#### Example Request
``` json
{
  "predicted_price": 52333.157479312136
}
```
