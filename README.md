# HTTP Requester Script

This Python script performs HTTP GET requests to multiple URLs. It can be used for testing or monitoring purposes where you need to repeatedly query HTTP endpoints.

## Prerequisites

- Python 3.x installed on your system. If not installed, download and install Python from [python.org](https://www.python.org/downloads/).

## Installation

1. Clone the repository or download the `http_requester.py` script.

    ```bash
    git clone https://github.com/electrokido321/http-requester.git
    ```

2. Navigate to the directory containing the script.

    ```bash
    cd http-requester
    ```

3. Install the required Python packages using pip.

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Open the `http_requester.py` script in a text editor.

2. Modify the `urls` list to include the HTTP URLs you want to request.

    ```python
    urls = [
        'http://example.com',
        'http://another-example.com',
        # You can add yours but i have an list already implemented
    ]
    ```

3. Adjust the `num_requests` variable to specify how many times to request each URL.

    ```python
    num_requests = 5  # Number of requests per URL
    ```

4. Run the script.

    ```bash
    python http_requester.py
    ```

5. The script will start sending HTTP GET requests to each URL specified in the `urls` list.

## Customization

- **Timeout**: You can adjust the timeout for each request by modifying the `timeout` parameter in the `requests.get()` call within the `send_requests()` function.

    ```python
    response = requests.get(url, timeout=10)
    ```

- **Delay Between Requests**: To avoid overwhelming the server, the script includes a 1-second delay (`time.sleep(1)`) between requests. You can adjust this delay if needed.

    ```python
    time.sleep(1)  # Delay between requests in seconds
    ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or create a pull request in the GitHub repository.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
