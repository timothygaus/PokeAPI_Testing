import pytest
import requests
from jsonschema import validate
from lib.pokeapi_json_schema import PokeAPISchema

@pytest.mark.parametrize("pokemon_name", ["pikachu", "gengar", "skuntank"])
def test_pokemon_name(pokemon_name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
    assert response.status_code == 200
    assert response.json()["name"] == pokemon_name

def test_invalid_pokemon_name():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/invalid_name")
    assert response.status_code == 404

def test_invalid_endpoint():
    response = requests.get("https://pokeapi.co/api/v2/invalid_endpoint")
    assert response.status_code == 404

def test_incorrect_http_method():
    response = requests.post("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 404

def test_response_headers():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

def test_response_content():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 200
    assert response.headers['Content-Type'].startswith("application/json")

def test_json_schema():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 200
    validate(response.json(), PokeAPISchema.POKEMON_SCHEMA)
