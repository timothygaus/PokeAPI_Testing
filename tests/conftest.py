"""
Fixtures for pytest
"""

import pytest

from lib.test_data import ENDPOINTS, POKEMON_TEST_CASES, EVOLUTION_CHAIN_TEST_CASES


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the API"""
    return "https://pokeapi.co/api/v2/"


@pytest.fixture(scope="session", params=ENDPOINTS)
def endpoint(request):
    """Endpoints for the API"""
    return request.param


@pytest.fixture(scope="session", params=POKEMON_TEST_CASES)
def pokemon_test_cases(request):
    """Test cases for Pokemon"""
    return request.param


@pytest.fixture(scope="session", params=EVOLUTION_CHAIN_TEST_CASES)
def evolution_chain_test_cases(request):
    """Test cases for Evolution Chains"""
    return request.param


# Add a marker for performance tests to rerun failed tests up to 3 times with a delay of 2 seconds between retries
def pytest_collection_modifyitems(items):
    """Automatically rerun failed performance tests"""
    for item in items:
        if "performance" in item.keywords:
            item.add_marker(pytest.mark.flaky(reruns=3, rerun_delay=2, min_passes=1))
