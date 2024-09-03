from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Get the API key from environment variables
API_KEY = os.getenv('MARKETSTACK_API_KEY')
BASE_URL = 'http://api.marketstack.com/v1/'

def get_stock_data(symbol, start_date=None, end_date=None):
    endpoint = f"{BASE_URL}eod"
    params = {
        'access_key': API_KEY,
        'symbols': symbol
    }
    if start_date:
        params['date_from'] = start_date
    if end_date:
        params['date_to'] = end_date

    try:
        response = requests.get(endpoint, params=params)
        response.raise_for_status()
        data = response.json()
        if 'error' in data:
            return None, data['error']
        return data['data'], None
    except requests.exceptions.RequestException as e:
        return None, str(e)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stock', methods=['POST'])
def stock():
    symbol = request.form.get('symbol')
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    stock_data, error = get_stock_data(symbol, start_date, end_date)
    return render_template('index.html', stock_data=stock_data, error=error)

if __name__ == '__main__':
    app.run(debug=True)
