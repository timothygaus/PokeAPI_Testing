import pytest
import requests


@pytest.mark.GET
def test_pokemon_name(pokemon_test_cases):
    # Test that the returned name matches the expected name for the given input name
    pokemon_name = pokemon_test_cases["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert response.json()["name"] == pokemon_name, f"Expected name {pokemon_name} but got {response.json()['name']}"


@pytest.mark.GET
def test_pokemon_base_experience(pokemon_test_cases):
    # Test that the returned base experience is populated correctly (greater than 0 and not None)
    pokemon_name = pokemon_test_cases["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "base_experience" in response.json()
    assert (
        response.json()["base_experience"] > 0 and response.json()["base_experience"] is not None
    ), f"Base experience for {pokemon_name} should be greater than 0"


@pytest.mark.GET
def test_pokemon_height(pokemon_test_cases):
    # Test that the returned height is populated correctly (greater than 0 and not None)
    pokemon_name = pokemon_test_cases["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "height" in response.json()
    assert (
        response.json()["height"] > 0 and response.json()["height"] is not None
    ), f"Height for {pokemon_name} should be greater than 0"


@pytest.mark.GET
def test_pokemon_name_has_expected_id(pokemon_test_cases):
    # Test that the name of the returned pokemon matches the expected name for the given input ID
    pokemon_id = pokemon_test_cases["id"]
    pokemon_name = pokemon_test_cases["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}")
    assert response.status_code == 200
    assert (
        response.json()["name"] == pokemon_name
    ), f"Expected name {pokemon_name} but got {response.json()['name']} for ID {pokemon_id}"


@pytest.mark.GET
def test_pokemon_id_has_expected_name(pokemon_test_cases):
    # Test that the ID of the returned pokemon matches the expected ID for the given input name
    pokemon_id = pokemon_test_cases["id"]
    pokemon_name = pokemon_test_cases["name"]
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert (
        response.json()["id"] == pokemon_id
    ), f"Expected ID {pokemon_id} but got {response.json()['id']} for name {pokemon_name}"
