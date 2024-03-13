import pytest
import HTTPConnection as http


@pytest.fixture(scope="module")
def http_c():
    """
    Fixture to create an instance of HTTPConnection before tests.
    """
    return http.HTTPConnection()


@pytest.mark.parametrize("param, expected_status_code", [("natural", 200)])
def test_nasa_epic_natural_response_code(http_c, param, expected_status_code):
    response = http_c.send_request(method="GET", param=param)
    assert response.status_code == expected_status_code


def test_nasa_epic_natural_color_metadata(http_c):
    response = http_c.send_request(method="GET", param="natural")
    # Verify that the response contains the expected data structure (e.g., image name, date, caption)
    data = response.json()
    assert "image" in data[0]
    assert "date" in data[0]
    assert "caption" in data[0]


def test_nasa_epic_enhanced_color_metadata(http_c):
    response = http_c.send_request(method="GET", param="enhanced")
    # Verify that the response contains the expected data structure (e.g., image name, date, caption)
    data = response.json()
    assert "image" in data[0]
    assert "date" in data[0]
    assert "caption" in data[0]


@pytest.mark.parametrize("invalid_param", [
    ("invalid_endpoint", "date", "2015/10/31"),  # Invalid endpoint URL
    ("natural", "", "2015/10/31"),  # Missing date parameter
    ("enhanced", "", "2015/10/31"),  # Missing required parameter
])
def test_error_handling(http_c, invalid_param):
    # Send a request with invalid parameters
    param, sub_param, value = invalid_param
    response = http_c.send_request(method="GET", param=param, sub_param=sub_param, value=value)

    # Verify that it returns an appropriate error status code
    assert response.status_code == 404, f"Expected status code 404 for {param}/{sub_param}/{value}, but received {response.status_code}"
