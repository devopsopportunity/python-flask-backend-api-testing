# pytest_fixture_api.py
# This script contains Pytest test cases for prize API endpoints.
# It tests various requests to retrieve prizes filtered by description and paginated.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

import pytest

@pytest.mark.usefixtures("client")
class TestPrizeAPI:
    def test_retrieve_first_prize(self, client):
        """
        Test: Retrieve the first prize from catalog 1.
        Expectation: A list of prizes with a total of 10 prizes.
        """
        response = client.get('/api/catalogs/1/prizes')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 10
        assert len(data["prizes"]) == 10

    def test_prizes_filtered_by_description_pagination(self, client):
        """
        Test: Retrieve prizes from catalog 2 filtered by description 'prize' with pagination (1 result per page).
        Expectation: One prize in the result with the description containing 'prize'.
        """
        response = client.get('/api/catalogs/2/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":1}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 1
        assert len(data["prizes"]) == 1

    def test_prizes_filtered_by_description_pagination_4_results(self, client):
        """
        Test: Retrieve prizes from catalog 3 filtered by description 'prize' with pagination (up to 4 results per page).
        Expectation: Up to 4 prizes in the result with the description containing 'prize'.
        """
        response = client.get('/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":4}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 4
        assert len(data["prizes"]) <= 4

    def test_prizes_filtered_by_description_pagination_page_2(self, client):
        """
        Test: Retrieve prizes from catalog 3 filtered by description 'prize' with pagination (page 2, up to 4 results per page).
        Expectation: Up to 4 prizes in the result with the description containing 'prize'.
        """
        response = client.get('/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":2,"per_page":4}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 4
        assert len(data["prizes"]) <= 4

    def test_prizes_filtered_by_description_pagination_page_3(self, client):
        """
        Test: Retrieve prizes from catalog 3 filtered by description 'prize' with pagination (page 3, up to 4 results per page).
        Expectation: Up to 2 prizes in the result with the description containing 'prize'.
        """
        response = client.get('/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":3,"per_page":4}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 2
        assert len(data["prizes"]) <= 2

    def test_prizes_filtered_by_description_hello(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by description 'hello' with pagination (up to 5 results per page).
        Expectation: No prizes in the result with the description containing 'hello'.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"description":"hello"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 0
        assert len(data["prizes"]) == 0

    def test_prizes_filtered_by_description_script(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by description 'script' with pagination (up to 5 results per page).
        Expectation: Prizes in the result with the description containing 'script'.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"description":"script"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 5
        assert len(data["prizes"]) == 5

    def test_prizes_filtered_by_id_1(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '1' with pagination (up to 5 results per page).
        Expectation: One prize in the result with the ID '1'.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"1"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 1
        assert len(data["prizes"]) == 1

    def test_prizes_filtered_by_id_2_and_description_script(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '2' and description 'script' with pagination (up to 5 results per page).
        Expectation: Prizes in the result with the ID '2' and description containing 'script'.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"2","description":"script"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 5
        assert len(data["prizes"]) == 5

    def test_prizes_filtered_by_id_2_and_description_hello(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with pagination (up to 5 results per page).
        Expectation: One prize in the result with the ID '2' and description containing 'hello'.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"2","description":"hello"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 1
        assert len(data["prizes"]) == 1

    def test_prizes_filtered_by_id_2_and_description_hello_and(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with logical operator 'AND' and pagination (up to 5 results per page).
        Expectation: No prizes in the result with the ID '2' and description containing 'hello' using 'AND' logical operator.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"AND"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 0
        assert len(data["prizes"]) == 0

    def test_prizes_filtered_by_id_2_and_description_script_and(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '2' and description 'script' with logical operator 'AND' and pagination (up to 5 results per page).
        Expectation: One prize in the result with the ID '2' and description containing 'script' using 'AND' logical operator.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"2","description":"script","logical_operator":"AND"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 1
        assert len(data["prizes"]) == 1

    def test_prizes_filtered_by_id_2_and_description_hello_or(self, client):
        """
        Test: Retrieve prizes from catalog 1 filtered by ID '2' and description 'hello' with logical operator 'OR' and pagination (up to 5 results per page).
        Expectation: One prize in the result with the ID '2' and description containing 'hello' using 'OR' logical operator.
        """
        response = client.get('/api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"OR"}&pagination={"page":1,"per_page":5}')
        assert response.status_code == 200
        data = response.get_json()
        assert data["total"] == 1
        assert len(data["prizes"]) == 1

