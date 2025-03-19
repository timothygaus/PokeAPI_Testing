"""
Various lists and dictionaries used for testing purposes
"""

ENDPOINTS = ["pokemon", "ability", "item", "move", "type", "berry", "evolution-chain"]

POKEMON_TEST_CASES = [
    {"id": 1, "name": "bulbasaur"},
    {"id": 4, "name": "charmander"},
    {"id": 39, "name": "jigglypuff"},
    {"id": 25, "name": "pikachu"},
    {"id": 133, "name": "eevee"},
    {"id": 135, "name": "jolteon"},
    {"id": 435, "name": "skuntank"},
]

EVOLUTION_CHAIN_TEST_CASES = [
    {"id": 1, "species_name": "bulbasaur", "is_baby": False},
    {"id": 5, "species_name": "weedle", "is_baby": False},
    {"id": 10, "species_name": "pichu", "is_baby": True},
]
