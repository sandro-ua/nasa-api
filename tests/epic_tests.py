import HTTPConnection as http
import logger as log


def test_nasa_image_response_code():
    # url = f"{const.BASE_URL}/EPIC/api/natural/date/2019-05-30?api_key={const.API_KEY}"
    http_c = http.HTTPConnection()
    response = http_c.send_request(method="GET", param="natural", sub_param="date", value="2019-05-30")
    assert response.status_code == 200, f"Request failed with status code {response.status_code}"


def test_nasa_image_key():
    http_c = http.HTTPConnection()
    response = http_c.send_request(method="GET", param="natural", sub_param="date", value="2019-05-30")

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"
    data = response.json()
    log.logger.info(f"Response Data: {data}")

    # Ensure 'image' key is present and has the expected value
    assert 'image' in data[0], "Image key not found in API response"
    image_value = data[0]['image']
    log.logger.info(f"Image Value:: {image_value}")

    expected_image_value = "epic_1b_20190530011359"
    assert image_value == expected_image_value, f"Expected image value: {expected_image_value}, Actual image value: {image_value}"


def test_nasa_identifier():
    http_c = http.HTTPConnection()
    response = http_c.send_request(method="GET", param="natural", sub_param="date", value="2019-05-30")

    assert response.status_code == 200, f"Request failed with status code {response.status_code}"

    data = response.json()
    log.logger.info(f"Response Data: {data}")
    assert 'identifier' in data[0], "identifier not found in API response"
