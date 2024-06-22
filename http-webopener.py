import requests
import time

# List of URLs to request
urls = [
 'http://000.00.000.000:port,
'http://000.00.000.000:port'
]
# Number of times to request each URL
num_requests = 5

# Function to send HTTP requests
def send_requests(url):
    for _ in range(num_requests):
        try:
            response = requests.get(url, timeout=10)
            print(f"Request to {url} - Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Request to {url} failed: {e}")
        time.sleep(1)  # Delay between requests to avoid rate limits or server overload

# Loop through each URL and send requests
for url in urls:
    send_requests(url)
