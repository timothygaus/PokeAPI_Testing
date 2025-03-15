import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://pokeapi.co/api/v2/"

@pytest.fixture(scope="session", params=[
    "pokemon",
    "ability",
    "item",
    "move",
    "type",
    "berry",
    "evolution-chain",
])
def endpoint(request):
    return request.param

@pytest.fixture(scope="session", params=[
    {"id": 1, "name": "bulbasaur"},
    {"id": 4, "name": "charmander"},
    {"id": 39, "name": "jigglypuff"},
    {"id": 25, "name": "pikachu"},
    {"id": 133, "name": "eevee"},
    {"id": 135, "name": "jolteon"},
    {"id": 435, "name": "skuntank"},
])
def pokemon_test_cases(request):
    return request.param

# Add a marker for performance tests to rerun failed tests up to 3 times with a delay of 2 seconds between retries
def pytest_collection_modifyitems(config, items):
    for item in items:
        if "performance" in item.keywords:
            item.add_marker(pytest.mark.flaky(reruns=3, rerun_delay=2, min_passes=1))