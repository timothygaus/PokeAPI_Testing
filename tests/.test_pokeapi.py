import pytest
import requests
from jsonschema import validate
from lib.pokeapi_json_schema import PokeAPISchema

# TODO: Going to eventually remove this

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