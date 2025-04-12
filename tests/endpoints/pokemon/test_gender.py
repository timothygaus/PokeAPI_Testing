"""
Colleciton of tests for the Genders API endpoint
"""

from lib.helpers import make_request


def test_gender_female(base_url):
    """Test that the returned name is female for id = 1"""
    response = make_request("GET", f"{base_url}gender/1")
    assert response.status_code == 200
    assert response.json()["name"] == "female", f"Expected gender name female but got {response.json()['name']}"


def test_gender_male(base_url):
    """Test that the returned name is male for id = 2"""
    response = make_request("GET", f"{base_url}gender/2")
    assert response.status_code == 200
    assert response.json()["name"] == "male", f"Expected gender name male but got {response.json()['name']}"


def test_gender_genderless(base_url):
    """Test that the returned name is genderless for id = 3"""
    response = make_request("GET", f"{base_url}gender/3")
    assert response.status_code == 200
    assert response.json()["name"] == "genderless", f"Expected gender name genderless but got {response.json()['name']}"


def test_gender_invalid(base_url):
    """Test that the returned status code is 404 for invalid id"""
    response = make_request("GET", f"{base_url}gender/4")
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
