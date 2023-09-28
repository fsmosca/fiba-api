"""Get world cup 2023 championship game results

You need to install requests with "pip install requests."
"""

import requests

# Define the endpoint.
url = "https://apifiba.fly.dev/worldcup/2023/championship"

# Make a request to the endpoint.
response = requests.get(url)

# Print results if request is successful otherwise print the status code.
if response.status_code == 200:
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
