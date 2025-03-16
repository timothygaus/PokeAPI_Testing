# PokeAPI Automated Testing

## Overview

This test suite provides automated testing for the PokeAPI, located at [PokeAPI](https://pokeapi.co/). PokeAPI is a free RESTful API service that allows users to interact with a database containing information related to Pokemon. The purpose of this test suite is to test the various capabilities of the PokeAPI. This test suite primarily uses the `pytest` library of Python and other plugins of pytest, including `pytest-html` for reporting and `pytest-xdist` to improve test performance by running tests in parallel.

### Features

These are the main features of this test suite:

- Automated testing of the PokeAPI using `pytest`
- Basic API functionality (Smoke tests for key endpoints)
- Negative and edge case testing
- Performance testing (Including response time and throughput)
- Data validation testing

### Reports

The latest test reports can be found at [Test Report](https://timothygaus.github.io/PokeAPI_Testing/report.html)

## Installation

To run these tests locally:

1. Clone this repo with `git clone https://github.com/timothygaus/PokeAPI_Testing.git`
2. Run `.\setup.bat` in your command line
3. Run `.\run_tests` in your command line

This will execute all tests contained in the test suite and generate a `report.html` file that can be opened with your internet browser.

## Future Improvements

These are features that I plan on adding in the future:

- Expand edge case test coverage
- Expand data validation coverage
- Research and implement mocks for API responses

## Contact

- Author: Timothy Gaus
- GitHub: [timothygaus](https://github.com/timothygaus)
