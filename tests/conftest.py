"""
Fixtures for pytest
"""

import pytest

from lib.test_data import ENDPOINTS, GENDERS, POKEMON_TEST_CASES, GROWTH_RATES


@pytest.fixture(scope="session")
def base_url():
    """Base URL for the API"""
    return "https://pokeapi.co/api/v2/"


@pytest.fixture(scope="session", params=ENDPOINTS)
def endpoint(request):
    """Endpoint for the API"""
    return request.param


@pytest.fixture(scope="session", params=POKEMON_TEST_CASES)
def pokemon_test_cases(request):
    """Test cases for Pokemon"""
    return request.param


@pytest.fixture(scope="session", params=GROWTH_RATES)
def growth_rate_test_cases(request):
    """Test cases for Growth Rate"""
    return request.param


@pytest.fixture(scope="session", params=GENDERS)
def gender_test_cases(request):
    """Test cases for Gender"""
    return request.param


# Add a marker for performance tests to rerun failed tests up to 3 times with a delay of 2 seconds between retries
def pytest_collection_modifyitems(items):
    """Automatically rerun failed performance tests"""
    for item in items:
        if "performance" in item.keywords:
            item.add_marker(pytest.mark.flaky(reruns=3, rerun_delay=2, min_passes=1))
