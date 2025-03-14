import pytest
import requests

@pytest.mark.GET
def test_get_all(base_url, endpoint):
    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for GET {endpoint}"
    data = response.json()
    assert "results" in data, f"Expected 'results' key not found in response for GET {endpoint}"
    assert len(data["results"]) > 0, f"Expected non-empty 'results' for GET {endpoint}"

@pytest.mark.GET
@pytest.mark.parametrize("id", [1, 2, 3]) # Not going to go with large IDs here since we are testing many different endpoints
def test_get_by_id(base_url, endpoint, id):
    response = requests.get(f"{base_url}{endpoint}/{id}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for GET {endpoint}/1"
    data = response.json()
    assert "id" in data, f"Expected 'id' key not found in response for GET {endpoint}/{id}"
    assert data["id"] == id, f"Expected id to be {id} but got {data['id']} for GET {endpoint}/{id}"