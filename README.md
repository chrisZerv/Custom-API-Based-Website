# Stock Market Data Web Application

This project is a simple web application built with Flask that retrieves and displays stock market data using the Marketstack API. Users can input stock symbols, select a date range, and view the corresponding stock data in a user-friendly interface.

## Features

- Fetch and display stock market data for multiple symbols.
- Select a date range to retrieve historical data.
- Error handling for invalid symbols or network issues.
- Responsive and visually appealing interface using Bootstrap.
- Loading indicator to improve user experience.

## Demo

![screenshot]()

## Technologies Used

- Python
- Flask
- Marketstack API
- Bootstrap (for styling)
- HTML/CSS

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.
- An API key from [Marketstack](https://marketstack.com/).

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Create a `.env` file in the root directory and add your Marketstack API key:
    ```plaintext
    MARKETSTACK_API_KEY=your_marketstack_api_key
    ```

5. Run the Flask application:
    ```bash
    python app.py
    ```

6. Open your browser and go to `http://localhost:5000` to view the application.

### Usage

- Enter one or multiple stock symbols (comma-separated) into the input field.
- Optionally, select a start and end date to filter the results.
- Click "Get Data" to retrieve and display the stock market data.

### Deployment

To deploy this application, follow the instructions for your chosen hosting platform. Ensure that you set the necessary environment variables (like `MARKETSTACK_API_KEY`) directly on the server.

### Contributing

If you would like to contribute to this project, please fork the repository and create a pull request with your changes.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Acknowledgements

- [Marketstack API](https://marketstack.com/) for providing the stock market data.
- [Flask](https://flask.palletsprojects.com/) for the web framework.
- [Bootstrap](https://getbootstrap.com/) for the responsive design framework.

