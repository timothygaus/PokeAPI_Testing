class PokeAPISchema:
    
    POKEMON_SCHEMA = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string"},
            "height": {"type": "integer"},
            "weight": {"type": "integer"},
    },
    "required": ["id", "name", "height", "weight"]
}