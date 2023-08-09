#!/usr/bin/python3
"""Python script that fetches https://alu-intranet.hbtn.io/status"""


import requests
"""Importing requests for fetching data"""


url = "https://alu-intranet.hbtn.io/status"
"""URL to fetch data from"""

response = requests.get(url)
"""Send a GET request to the URL"""

if response.status_code == 200:
    try:
        # Try to parse the JSON content of the response
        data = response.json()
        # Display the formatted response body
        print("Body response:")
        print("\t- type:", type(data))     # Display the type of the data (dictionary in this case)
        print("\t- content:", data)        # Display the content of the response JSON data
    except Exception as e:
        # If JSON parsing fails, display the raw content of the response
        print("Failed to parse JSON. Raw content:")
        print(response.text)
else:
    # Display an error message if the status code is not 200
    print(f"Error: {response.status_code}")
