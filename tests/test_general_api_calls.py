"""
Collection of general API tests for various endpoints
that don't neatly fit into the other categories
"""

import pytest
from lib.helpers import make_request


def test_get_all(base_url, endpoint):
    """Test that the GET request to the endpoint returns a 200 status code and non-empty results"""
    response = make_request("GET", f"{base_url}{endpoint}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for GET {endpoint}"
    data = response.json()
    assert "results" in data, f"Expected 'results' key not found in response for GET {endpoint}"
    assert len(data["results"]) > 0, f"Expected non-empty 'results' for GET {endpoint}"


@pytest.mark.parametrize(
    "pokemon_id", [1, 2, 3]
)  # Not going to go with large IDs here since we are testing many different endpoints
def test_get_by_id(base_url, endpoint, pokemon_id):
    """
    Test that the GET request to the endpoint with a specific ID
    returns a 200 status code and the correct ID in the response
    """
    response = make_request("GET", f"{base_url}{endpoint}/{pokemon_id}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for GET {endpoint}/{pokemon_id}"
    data = response.json()
    assert "id" in data, f"Expected 'id' key not found in response for GET {endpoint}/{pokemon_id}"
    assert (
        data["id"] == pokemon_id
    ), f"Expected id to be {pokemon_id} but got {data['id']} for GET {endpoint}/{pokemon_id}"
