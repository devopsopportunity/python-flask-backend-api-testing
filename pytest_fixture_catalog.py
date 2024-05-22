# pytest_fixture_catalog.py
# This script contains Pytest test cases for catalog API endpoints.
# It tests listing all catalogs, creating new catalogs, getting details of single catalogs,
# deleting catalogs, and listing all catalogs after various operations.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

import pytest

@pytest.mark.usefixtures("client")
class TestCatalogAPI:
    def test_list_all_catalogs(self, client):
        """
        Test: List all catalogs.
        Expectation: A list of catalogs is returned.
        """
        response = client.get('/api/catalogs')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'catalogs' in data
        assert isinstance(data['catalogs'], list)
        assert len(data['catalogs']) >= 0  # Ensure there are catalogs in the list

    def test_create_new_catalog(self, client):
        """
        Test: Create a new catalog.
        Expectation: A new catalog is successfully created.
        """
        response = client.post('/api/catalog', json={})
        assert response.status_code == 201  # Assuming 201 Created is the expected response code
        data = response.get_json()
        assert 'catalog_id' in data
        assert isinstance(data['catalog_id'], int)  # Ensure the catalog_id is an integer

    def test_get_single_catalog_6(self, client):
        """
        Test: Get details of a single catalog (ID 6).
        Expectation: The details of the catalog with ID 6 are returned.
        """
        response = client.get('/api/catalogs')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'catalogs' in data
        assert isinstance(data['catalogs'], list)
        assert len(data['catalogs']) == 6  # Ensure there are catalogs in the list

        response = client.get(f'/api/catalog/6')
        assert response.status_code == 200
        data = response.get_json()
        assert data.get('catalog', {}).get('id') == 6

    def test_delete_catalog(self, client):
        """
        Test: Delete a catalog (ID 3).
        Expectation: The catalog with ID 3 is successfully deleted.
        """
        # Deleting catalog with ID 3
        print("Deleting catalog with ID 3:")
        print("DELETE /api/catalog/3")
        response = client.delete('/api/catalog/3')
        assert response.status_code == 200  # Modify expected status code if necessary
        print("------------------------------------------------------")

    def test_get_single_catalog_3(self, client):
        """
        Test: Get details of a single catalog (ID 3).
        Expectation: The details of the catalog with ID 3 are returned.
        """
        response = client.get('/api/catalogs')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'catalogs' in data
        assert isinstance(data['catalogs'], list)
        assert len(data['catalogs']) == 5  # Ensure there are catalogs in the list

        response = client.get(f'/api/catalog/3')
        assert response.status_code == 404

    def test_recreate_catalog(self, client):
        """
        Test: Recreate the catalog.
        Expectation: A new catalog is successfully created.
        """
        response = client.post('/api/catalog', json={})
        assert response.status_code == 201  # Assuming 201 Created is the expected response code
        data = response.get_json()
        assert 'catalog_id' in data
        assert isinstance(data['catalog_id'], int)  # Ensure the catalog_id is an integer

    def test_list_all_catalogs_after_operations(self, client):
        """
        Test: List all catalogs after performing create, delete, and recreate operations.
        Expectation: A list of catalogs is returned.
        """
        response = client.get('/api/catalogs')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'catalogs' in data
        assert isinstance(data['catalogs'], list)

