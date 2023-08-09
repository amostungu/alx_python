#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


import requests
"""Importing requests"""

# URL to fetch data from
url = "https://alu-intranet.hbtn.io/status"

# Send a GET request to the URL
response = requests.get(url)

# Check if the response status code is 200 (OK)
if response.status_code == 200:
    # Parse the JSON content of the response
    data = response.json()

    # Display the formatted response body
    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
else:
    # Display an error message if the status code is not 200
    print(f"Error: {response.status_code}")
