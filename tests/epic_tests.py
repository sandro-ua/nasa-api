# tests/test_nasa_api.py
import requests
import pytest

NASA_API_KEY = "x88Trcn4V9HNXxQkviO8bJ5Ubo2NhGQFQ9Ui9xGW"
NASA_API_URL = "https://api.nasa.gov"

# example
# https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=DEMO_KEY 

def test_nasa_image():
    url = f"{NASA_API_URL}/EPIC/api/natural/date/2019-05-30?api_key={NASA_API_KEY}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    
    data = response.json()
    assert 'image' in data, "image not found in API response"


def test_nasa_identifier():
    url = f"{NASA_API_URL}/EPIC/api/natural/date/2019-05-30?api_key={NASA_API_KEY}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    
    data = response.json()
    print(data)
    assert 'identifier' in data, "identifier not found in API response"