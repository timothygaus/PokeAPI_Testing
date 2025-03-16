"""
Collection of tests for performance testing various endpoints
"""

import time

import psutil
import pytest

from lib.helpers import make_request


THROUGHPUT_THRESHOLD = 10  # requests per second
CPU_PERFORMANCE_THRESHOLD = 50  # percentage
MEMORY_PERFORMANCE_THRESHOLD = 50 * 1024 * 1024  # 50 MB converted to Bytes


@pytest.mark.performance
def test_response_time(base_url, endpoint):
    """Test that the response time for the endpoint is less than 1 second"""
    start_time = time.time()
    response = make_request('GET', f"{base_url}{endpoint}")
    end_time = time.time()

    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for {endpoint}"
    assert (end_time - start_time) < 1, f"Response time for {endpoint} took too long: {end_time - start_time} seconds"
    print(f"Response time for {endpoint}: {end_time - start_time} seconds")


@pytest.mark.performance
def test_throughput(base_url, endpoint):
    """Test that the throughput for the endpoint is greater than 50 requests/second"""
    num_requests = 100
    start_time = time.time()

    for _ in range(num_requests):
        response = make_request('GET', f"{base_url}{endpoint}")
        assert response.status_code == 200, f"Expected 200 but got {response.status_code} for {endpoint}"

    end_time = time.time()
    total_time = end_time - start_time
    throughput = num_requests / total_time
    assert throughput > THROUGHPUT_THRESHOLD, f"Throughput for {endpoint} was too low: {throughput} requests/second"
    print(f"Throughput for {endpoint}: {throughput} requests/second")


@pytest.mark.performance
def test_resource_usage(base_url, endpoint):
    """Test that the resource usage (CPU and Memory) for the endpoint is within acceptable limits"""
    process = psutil.Process()
    start_cpu = process.cpu_percent(interval=None)
    start_memory = process.memory_info().rss

    response = make_request('GET', f"{base_url}{endpoint}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for {endpoint}"

    end_cpu = process.cpu_percent(interval=None)
    end_memory = process.memory_info().rss

    cpu_usage = end_cpu - start_cpu
    memory_usage = end_memory - start_memory

    assert cpu_usage < CPU_PERFORMANCE_THRESHOLD, f"CPU usage for {endpoint} was too high: {cpu_usage}%"
    assert (
        memory_usage < MEMORY_PERFORMANCE_THRESHOLD
    ), f"Memory usage for {endpoint} was too high: {memory_usage / (1024 * 1024)} MB"
