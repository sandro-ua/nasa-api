import requests
import constants as const


def test_nasa_image():
    url = f"{const.BASE_URL}/EPIC/api/natural/date/2019-05-30?api_key={const.API_KEY}"
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
    url = f"{const.BASE_URL}/EPIC/api/natural/date/2019-05-30?api_key={const.API_KEY}"
    response = requests.get(url)

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    
    data = response.json()
    print("Response Data:", data)  # Print response data for debugging
    assert 'identifier' in data[0], "identifier not found in API response"


def test_successful_data_retrieval():
    response = requests.get("https://epic.gsfc.nasa.gov/api/natural")
    assert response.status_code == 200 # Should be 200, expect failure here