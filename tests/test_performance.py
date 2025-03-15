import time
from concurrent.futures import ThreadPoolExecutor

import psutil
import pytest
import requests

# Collection of tests for performance testing various endpoints

@pytest.mark.GET
@pytest.mark.performance
def test_response_time(base_url, endpoint):
    start_time = time.time()
    response = requests.get(f"{base_url}{endpoint}")
    end_time = time.time()
    
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for {endpoint}"
    assert (end_time - start_time) < 1, f"Response time for {endpoint} took too long: {end_time - start_time} seconds"
    print(f"Response time for {endpoint}: {end_time - start_time} seconds")

@pytest.mark.GET
@pytest.mark.performance
def test_throughput(base_url, endpoint):
    num_requests = 100
    start_time = time.time()

    def send_request():
        response = requests.get(f"{base_url}{endpoint}")
        return response.status_code

    with ThreadPoolExecutor(max_workers=num_requests) as executor:
        futures = [executor.submit(send_request) for _ in range(num_requests)]
        results = [future.result() for future in futures]

    end_time = time.time()
    total_time = end_time - start_time
    throughput = num_requests / total_time
    assert throughput > 50, f"Throughput for {endpoint} was too low: {throughput} requests/second"

@pytest.mark.GET
@pytest.mark.performance
def test_resource_usage(base_url, endpoint):
    process = psutil.Process()
    start_cpu = process.cpu_percent(interval=None)
    start_memory = process.memory_info().rss

    response = requests.get(f"{base_url}{endpoint}")
    assert response.status_code == 200, f"Expected 200 but got {response.status_code} for {endpoint}"

    end_cpu = process.cpu_percent(interval=None)
    end_memory = process.memory_info().rss

    cpu_usage = end_cpu - start_cpu
    memory_usage = end_memory - start_memory

    assert cpu_usage < 50, f"CPU usage for {endpoint} was too high: {cpu_usage}%"
    assert memory_usage < 50 * 1024 * 1024, f"Memory usage for {endpoint} was too high: {memory_usage / (1024 * 1024)} MB"