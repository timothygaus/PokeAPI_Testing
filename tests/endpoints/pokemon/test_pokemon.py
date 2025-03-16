"""
Collection of tests for the Pokemon API endpoint
"""

import pytest

from lib.helpers import make_request


@pytest.mark.GET
def test_pokemon_name(base_url, pokemon_test_cases):
    """Test that the returned pokemon name matches the expected name for the given input name"""
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert response.json()["name"] == pokemon_name, f"Expected name {pokemon_name} but got {response.json()['name']}"


@pytest.mark.GET
def test_pokemon_base_experience(base_url, pokemon_test_cases):
    """Test that the returned base experience is populated correctly (greater than 0 and not None)"""
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "base_experience" in response.json()
    assert (
        response.json()["base_experience"] > 0 and response.json()["base_experience"] is not None
    ), f"Base experience for {pokemon_name} should be greater than 0"


@pytest.mark.GET
def test_pokemon_height(base_url, pokemon_test_cases):
    """Test that the returned height is populated correctly (greater than 0 and not None)"""
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "height" in response.json()
    assert (
        response.json()["height"] > 0 and response.json()["height"] is not None
    ), f"Height for {pokemon_name} should be greater than 0"


@pytest.mark.GET
def test_pokemon_name_has_expected_id(base_url, pokemon_test_cases):
    """Test that the name of the returned pokemon matches the expected name for the given input ID"""
    pokemon_id = pokemon_test_cases["id"]
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_id}")
    assert response.status_code == 200
    assert (
        response.json()["name"] == pokemon_name
    ), f"Expected name {pokemon_name} but got {response.json()['name']} for ID {pokemon_id}"


@pytest.mark.GET
def test_pokemon_id_has_expected_name(base_url, pokemon_test_cases):
    """Test that the ID of the returned pokemon matches the expected ID for the given input name"""
    pokemon_id = pokemon_test_cases["id"]
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_id}")
    assert response.status_code == 200
    assert (
        response.json()["id"] == pokemon_id
    ), f"Expected ID {pokemon_id} but got {response.json()['id']} for name {pokemon_name}"

def test_pokemon_data_has_valid_types(base_url, pokemon_test_cases):
    """Test that various fields within pokemon contain the correct data types"""
    pokemon_name = pokemon_test_cases["name"]
    response = make_request("GET", f"{base_url}pokemon/{pokemon_name}")
    assert response.status_code == 200
    id_response = response.json()["id"] # Expect integer
    name_response = response.json()["name"] # Expect string
    abilities_response = response.json()["abilities"] # Expect a list of PokemonAbility
    types_response = response.json()["types"] # Expect a list of PokemonType
    assert isinstance(id_response, int), f"Expected 'id' to be int, but got {type(id_response)}"
    assert isinstance(name_response, str), f"Expected 'name' to be string, but got {type(name_response)}"
    assert isinstance(abilities_response, list), f"Expected 'abilities' to be list, but got {type(abilities_response)}"
    assert isinstance(types_response, list), f"Expected 'types' to be list, but got {type(abilities_response)}"
    # Check that lists are not empty
    assert len(abilities_response) > 0, f"Expected at least one entry in 'abilities' list, but list was empty"
    assert len(types_response) > 0, f"Expected at least one entry in 'types', list, but list was empty"
