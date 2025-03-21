"""
Collection of tests for invalid API calls to various endpoints,
including invalid GET, POST, and PUT requests
"""

from lib.helpers import make_request


def test_invalid_get_requests(base_url, endpoint):
    """Test that invalid GET requests return appropriate error codes (400 or 404)"""
    response = make_request('GET', f"{base_url}{endpoint}/invalid")
    assert response.status_code in [
        400,
        404,
    ], f"Expected 400 or 404 for GET {endpoint}/invalid but got {response.status_code}"


def test_post_request(base_url, endpoint):
    """Test that POST requests to the endpoint return appropriate error codes (404 or 405)"""
    response = make_request('POST', f"{base_url}{endpoint}/invalid")
    assert response.status_code in [
        404,
        405,
    ], f"Expected 404 or 405 for POST request to {endpoint} but got {response.status_code}"


def test_put_request(base_url, endpoint):
    """Test that PUT requests to the endpoint return appropriate error codes (404 or 405)"""
    response = make_request('PUT', f"{base_url}{endpoint}/invalid")
    assert response.status_code in [
        404,
        405,
    ], f"Expected 404 or 405 for PUT request to {endpoint} but got {response.status_code}"
