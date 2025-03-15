import pytest
import requests

@pytest.mark.GET
def test_pokemon_name(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert response.json()["name"] == pokemon_name, f"Expected name {pokemon_name} but got {response.json()['name']}"

@pytest.mark.GET
def test_pokemon_base_experience(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "base_experience" in response.json()
    assert response.json()["base_experience"] > 0 and response.json()["base_experience"] is not None, f"Base experience for {pokemon_name} should be greater than 0"

@pytest.mark.GET
def test_pokemon_height(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert "height" in response.json()
    assert response.json()["height"] > 0 and response.json()["height"] is not None, f"Height for {pokemon_name} should be greater than 0"