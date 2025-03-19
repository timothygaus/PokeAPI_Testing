"""
Collection of tests for the Evolution Chain endpoint within Evolution
"""

from lib.helpers import make_request


def test_species_by_id(base_url, evolution_chain_test_cases):
    """Tests that the expected species is returned for a given id"""
    evolution_chain_id = evolution_chain_test_cases["id"]
    evolution_chain_species_name = evolution_chain_test_cases["species_name"]
    response = make_request("GET", f"{base_url}/evolution-chain/{evolution_chain_id}")
    assert response.status_code == 200
    response_species_name = response.json()["chain"]["species"]["name"]
    assert response_species_name == evolution_chain_species_name, (
        f"Expected evolution chain species name for evolution chain id {evolution_chain_id} "
        f"to be {evolution_chain_species_name}, but got {response_species_name}"
    )
