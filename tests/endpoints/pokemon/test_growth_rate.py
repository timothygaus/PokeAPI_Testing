"""
Collection of tests for the Growth Rate API endpoint
"""

from lib.helpers import make_request


def test_growth_rate_names(base_url, growth_rate_test_cases):
    """Test that the growth rate names are as expected"""
    growth_rate_id = growth_rate_test_cases["id"]
    expected_name = growth_rate_test_cases["name"]
    response = make_request("GET", f"{base_url}growth-rate/{growth_rate_id}")
    assert response.status_code == 200
    assert (
        response.json()["name"] == expected_name
    ), f"Expected growth rate name {expected_name} but got {response.json()['name']}"


def test_growth_rate_ids(base_url, growth_rate_test_cases):
    """Test that the growth rate IDs are as expected"""
    growth_rate_name = growth_rate_test_cases["name"]
    expected_id = growth_rate_test_cases["id"]
    response = make_request("GET", f"{base_url}growth-rate/{growth_rate_name}")
    assert response.status_code == 200
    assert (
        response.json()["id"] == expected_id
    ), f"Expected growth rate ID {expected_id} but got {response.json()['id']}"


def test_number_of_levels(base_url, growth_rate_test_cases):
    """Test that the levels list is equal to 100 for all growth rates"""  # All pokemon can be level 100
    growth_rate_id = growth_rate_test_cases["id"]
    response = make_request("GET", f"{base_url}growth-rate/{growth_rate_id}")
    assert response.status_code == 200
    assert (
        len(response.json()["levels"]) == 100
    ), f"Expected 100 levels but got {len(response.json()['levels'])} for growth rate ID {growth_rate_id}"


def test_at_least_one_pokemon_species_per_growth_rate(base_url, growth_rate_test_cases):
    """Test that there is at least one pokemon species for each growth rate"""
    growth_rate_id = growth_rate_test_cases["id"]
    response = make_request("GET", f"{base_url}growth-rate/{growth_rate_id}")
    assert response.status_code == 200
    assert len(response.json()["pokemon_species"]) > 0, (
        f"Expected at least one pokemon species but got {len(response.json()['pokemon_species'])} "
        f"for growth rate ID {growth_rate_id}"
    )


# TODO: Consider adding the actual formula to the growth rate test cases to test that the formula is correct
# Counterpoint: Have growth rate formulas ever changed?
# Regardless, it may still be valid to check that the API contains the most up to date information,
# or to flag the test if it is incorrectly failing and needs updating
def test_growth_rate_formula(base_url, growth_rate_test_cases):
    """Test that the growth rate formula is not None"""
    growth_rate_id = growth_rate_test_cases["id"]
    response = make_request("GET", f"{base_url}growth-rate/{growth_rate_id}")
    assert response.status_code == 200
    assert (
        response.json()["formula"] is not None
    ), f"Expected a formula but got None for growth rate ID {growth_rate_id}"


def test_invalid_growth_rate_id(base_url):
    """Test that the returned status code is 404 for invalid growth rate ID"""
    response = make_request("GET", f"{base_url}growth-rate/999")
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


def test_invalid_growth_rate_name(base_url):
    """Test that the returned status code is 404 for invalid growth rate name"""
    response = make_request("GET", f"{base_url}growth-rate/invalid_name")
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"
