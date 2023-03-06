import requests
import json
from datetime import datetime

def log_request(method, endpoint, timestamp):
    
    # Discord webook
    
    url = 'https://discord.com/api/webhooks/1082218762159280228/5kfJFa47vmNIatwlCjS84hVXlQ9UGx9osqVO0NvqU3fpS0d-bKWglvDGcWvHXt83AGEo'

    headers = {
        'Content-Type': 'application/json'
    }

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"{current_time}: {method} request to {endpoint} at {timestamp}"

    payload = {
        'content': message
    }

    response = requests.post(url, headers=headers, data=json.dumps(payload))

    if response.status_code != 204:
        print(f"Error sending log message: {response.text}")
