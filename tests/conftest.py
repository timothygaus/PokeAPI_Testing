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
    "bulbasaur",
    "charmander",
    "jigglypuff",
    "pikachu",
    "eevee",
    "jolteon",
    "skuntank",
])
def pokemon_name(request):
    return request.param

# Add a marker for performance tests to rerun failed tests up to 3 times with a delay of 2 seconds between retries
def pytest_collection_modifyitems(config, items):
    for item in items:
        if "performance" in item.keywords:
            item.add_marker(pytest.mark.flaky(reruns=3, rerun_delay=2, min_passes=1))