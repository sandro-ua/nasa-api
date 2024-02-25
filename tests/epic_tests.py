# tests/test_nasa_api.py
import requests
import pytest

NASA_API_KEY = "x88Trcn4V9HNXxQkviO8bJ5Ubo2NhGQFQ9Ui9xGW"
NASA_API_URL = "https://api.nasa.gov"

# example
# https://api.nasa.gov/EPIC/api/natural/date/2019-05-30?api_key=DEMO_KEY
# documentation https://epic.gsfc.nasa.gov/about/api

def test_nasa_image():
    url = f"{NASA_API_URL}/EPIC/api/natural/date/2019-05-30?api_key={NASA_API_KEY}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    
    data = response.json()
    print("Response Data:", data)  # Print response data for debugging
    
    # Ensure 'image' key is present and has the expected value
    assert 'image' in data[0], "Image key not found in API response"
    image_value = data[0]['image']
    print("Image Value:", image_value)  # Print image value for debugging
    
    expected_image_value = "epic_1b_20190530011359"
    assert image_value == expected_image_value, f"Expected image value: {expected_image_value}, Actual image value: {image_value}"


def test_nasa_identifier():
    url = f"{NASA_API_URL}/EPIC/api/natural/date/2019-05-30?api_key={NASA_API_KEY}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    
    data = response.json()
    print("Response Data:", data)  # Print response data for debugging
    assert 'identifier' in data[0], "identifier not found in API response"

# Test that is expected to fail
def test_successful_data_retrieval():
    response = requests.get("https://epic.gsfc.nasa.gov/api/natural")
    assert response.status_code == 0 # Should be 200, expect failure here