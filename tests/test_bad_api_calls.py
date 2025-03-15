import pytest
import requests

@pytest.mark.GET
def test_invalid_get_requests(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}/invalid")
    assert response.status_code in [400, 404], f"Expected 400 or 404 for GET {endpoint}/invalid but got {response.status_code}"

def test_post_request(base_url, endpoint):
    response = requests.post(f"{base_url}{endpoint}")
    assert response.status_code in [404, 405], f"Expected 404 or 405 for POST request to {endpoint} but got {response.status_code}"

def test_put_request(base_url, endpoint):
    response = requests.put(f"{base_url}{endpoint}")
    assert response.status_code in [404, 405], f"Expected 404 or 405 for PUT request to {endpoint} but got {response.status_code}"