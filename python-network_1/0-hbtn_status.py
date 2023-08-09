#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


import requests
"""Importing requests"""


url = "https://alu-intranet.hbtn.io/status"
"""URL to fetch data from"""

response = requests.get(url)
"""Send a GET request to the URL"""

if response.status_code == 200:
    """Check if the response status code is 200 (OK)"""
    data = response.json()
    """Parse the JSON content of the response"""

    print("Body response:")
    """Display the formatted response body"""
    print("\t- type:", type(data))
    """Display the type of the data (dictionary in this case)"""
    print("\t- content:", data)
    """Display the content of the response JSON data"""
else:
    """Display an error message if the status code is not 200"""
    print(f"Error: {response.status_code}")
