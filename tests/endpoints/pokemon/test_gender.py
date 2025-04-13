"""
Colleciton of tests for the Genders API endpoint
"""

from lib.helpers import make_request


def test_gender_name(base_url, gender_test_cases):
    """Test that the returned name is expected for the given id"""
    gender_id = gender_test_cases["id"]
    expected_gender_name = gender_test_cases["name"]
    response = make_request("GET", f"{base_url}gender/{gender_id}")
    assert response.status_code == 200
    assert (
        response.json()["name"] == expected_gender_name
    ), f"Expected gender name {expected_gender_name} but got {response.json()['name']}"


def test_gender_id(base_url, gender_test_cases):
    """Test that the returned id is expected for the given name"""
    gender_name = gender_test_cases["name"]
    expected_gender_id = gender_test_cases["id"]
    response = make_request("GET", f"{base_url}gender/{gender_name}")
    assert response.status_code == 200
    assert (
        response.json()["id"] == expected_gender_id
    ), f"Expected gender id {expected_gender_id} but got {response.json()['id']}"


def test_gender_invalid(base_url):
    """Test that the returned status code is 404 for invalid id"""
    response = make_request("GET", f"{base_url}gender/4")
    assert response.status_code == 404, f"Expected status code 404 but got {response.status_code}"


def test_gender_contains_pokemon(base_url, gender_test_cases):
    """Test that each gender contains at least one pokemon species"""
    gender_name = gender_test_cases["name"]
    response = make_request("GET", f"{base_url}gender/{gender_name}")
    assert response.status_code == 200
    assert len(response.json()["pokemon_species_details"]) > 0, (
        f"Expected length of pokemon species details to be greater than 0 "
        f"but got {len(response.json()['pokemon_species_details'])}"
    )


def test_gender_required_for_evolution(base_url, gender_test_cases):
    """
    Test that each gender contains an expected number of entries in the required_for_evolution list
    Female and Male should be > 0, Genderless should be 0
    """
    gender_name = gender_test_cases["name"]
    response = make_request("GET", f"{base_url}gender/{gender_name}")
    assert response.status_code == 200
    if gender_name == "genderless":
        assert len(response.json()["required_for_evolution"]) == 0, (
            f"Expected length of required_for_evolution to be 0 for {gender_name} "
            f"but got {len(response.json()['required_for_evolution'])}"
        )
    elif gender_name in ("female", "male"):
        assert len(response.json()["required_for_evolution"]) > 0, (
            f"Expected length of required_for_evolution to be greater than 0 for {gender_name} "
            f"but got {len(response.json()['required_for_evolution'])}"
        )
