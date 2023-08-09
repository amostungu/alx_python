#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


import requests
"""Importing requests for fetching data"""


url = "https://alu-intranet.hbtn.io/status"
"""URL to fetch data from"""

response = requests.get(url)
"""Send a GET request to the URL"""

if response.status_code == 200:
    if response.text == "OK":
        # Display the text content of the response
        print("Body response:")
        print("\t- type: str")
        print("\t- content:", response.text)
    else:
        # Display an error message if the response content is unexpected
        print("Unexpected response content:", response.text)
else:
    # Display an error message if the status code is not 200
    print(f"Error: {response.status_code}")
