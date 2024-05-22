# pytest_mark_parametrize_api.py
# This script performs HTTP requests to test the API endpoints.
# It includes various requests to retrieve prizes filtered by description and paginated.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

import pytest
import requests
import json

# Base URL for the API endpoints
BASE_URL = 'http://localhost:5000/api/catalogs'

def make_request(catalog_id, filters, pagination):
    """
    Helper function to make a GET request to the API endpoint.
    It constructs the URL, serializes the filters and pagination parameters,
    and sends the GET request.
    """
    url = f"{BASE_URL}/{catalog_id}/prizes"
    params = {
        "filter": json.dumps(filters),
        "pagination": json.dumps(pagination)
    }
    response = requests.get(url, params=params)
    return response

def assert_response(response, expected_total, expected_len):
    """
    Helper function to assert the response from the API.
    It checks if the response status code is 200 (OK),
    and then asserts the 'total' and the length of the 'prizes' list
    in the response data.
    """
    if response.status_code != 200:
        print(f"Error: Received status code {response.status_code}")
        print(f"Response content: {response.content}")
        print(f"Expected total: {expected_total}, Expected length: {expected_len}")
    assert response.status_code == 200
    data = response.json()
    assert data['total'] == expected_total
    assert len(data['prizes']) == expected_len

# Parametrized test cases
@pytest.mark.parametrize("catalog_id, filters, pagination, expected_total, expected_len", [
    # Test case 1: Retrieve all prizes from catalog 1
    (1, {}, {}, 10, 10),
    # Test case 2: Retrieve prizes from catalog 2 filtered by description 'prize' with pagination (1 result per page)
    (2, {"description": "prize"}, {"page": 1, "per_page": 1}, 1, 1),
    # Test cases 3-5: Retrieve prizes from catalog 3 filtered by description 'prize' with pagination (up to 4 results per page)
    (3, {"description": "prize"}, {"page": 1, "per_page": 4}, 4, 4),
    (3, {"description": "prize"}, {"page": 2, "per_page": 4}, 4, 4),
    (3, {"description": "prize"}, {"page": 3, "per_page": 4}, 2, 2),
    # Test case 6: Retrieve prizes from catalog 1 filtered by description 'hello' with pagination (up to 5 results per page)
    (1, {"description": "hello"}, {"page": 1, "per_page": 5}, 0, 0),
    # Test case 7: Retrieve prizes from catalog 1 filtered by description 'script' with pagination (up to 5 results per page)
    (1, {"description": "script"}, {"page": 1, "per_page": 5}, 5, 5),
    # Test case 8: Retrieve prizes from catalog 1 filtered by ID '1' with pagination (up to 5 results per page)
    (1, {"id": "1"}, {"page": 1, "per_page": 5}, 1, 1),
    # Test case 9: Retrieve prizes from catalog 1 filtered by ID '2' and description 'script' with pagination (up to 5 results per page)
    (1, {"id": "2", "description": "script"}, {"page": 1, "per_page": 5}, 5, 5),
    # Test case 10: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with pagination (up to 5 results per page)
    (1, {"id": "2", "description": "hello"}, {"page": 1, "per_page": 5}, 1, 1),
    # Test case 11: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with logical operator 'AND' and pagination (up to 5 results per page)
    (1, {"id": "2", "description": "hello", "logical_operator": "AND"}, {"page": 1, "per_page": 5}, 0, 0),
    # Test case 12: Retrieve prizes from catalog 1 filtered by ID '2' and description 'script' with logical operator 'AND' and pagination (up to 5 results per page)
    (1, {"id": "2", "description": "script", "logical_operator": "AND"}, {"page": 1, "per_page": 5}, 1, 1),
    # Test case 13: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with logical operator 'OR' and pagination (up to 5 results per page)
    (1, {"id": "2", "description": "hello", "logical_operator": "OR"}, {"page": 1, "per_page": 5}, 1, 1),
])
def test_api(catalog_id, filters, pagination, expected_total, expected_len):
    """
    Test function that calls the make_request and assert_response functions
    for the given test case parameters.
    """
    response = make_request(catalog_id, filters, pagination)
    assert_response(response, expected_total, expected_len)

