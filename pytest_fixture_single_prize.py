# pytest_fixture_single_prize.py
# This script contains Pytest test cases for single prize API endpoints.
# It tests listing all prizes in a catalog, creating a new prize, updating a prize,
# deleting a prize, and retrieving details of a single prize.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

import pytest

@pytest.mark.usefixtures("client")
class TestSinglePrizeAPI:
    def test_list_all_prizes(self, client):
        """
        Test: List all prizes in catalog with ID 1.
        Expectation: A list of prizes is returned.
        """
        response = client.get('/api/catalogs/1/prizes')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'prizes' in data
        assert isinstance(data['prizes'], list)

    def test_create_new_prize(self, client):
        """
        Test: Create a new prize in catalog with ID 1.
        Expectation: The new prize is successfully created.
        """
        new_prize = {
            "title": "New Prize",
            "description": "Description of the new prize",
            "image": "new_image_url"
        }
        response = client.post('/api/catalogs/1/prize', json=new_prize)
        assert response.status_code == 201
        data = response.get_json()
        assert 'id' in data  # Assuming the response includes the ID of the newly created prize

    def test_verify_new_prize(self, client):
        """
        Test: Get details of a single prize (ID 11).
        Expectation: The details of the prize with ID 11 are returned.
        """
        response = client.get('/api/catalogs/1/prizes')

        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'prizes' in data
        assert isinstance(data['prizes'], list)
        assert len(data['prizes']) == 11  # Ensure there are prizes in the list

    def test_get_single_prize_details(self, client):
        """
        Test: Get details of a single prize with ID 11 in catalog with ID 1.
        Expectation: The prize details are returned.
        """
        response = client.get('/api/catalogs/1/prize/11')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'id' in data and data['id'] == 11

    def test_update_single_prize(self, client):
        """
        Test: Update details of a single prize with ID 11 in catalog with ID 1.
        Expectation: The prize details are successfully updated.
        """
        updated_prize = {
            "title": "Updated Prize Name"
        }
        response = client.put('/api/catalogs/1/prize/11', json=updated_prize)
        assert response.status_code == 200
        data = response.get_json()
        assert data['title'] == "Updated Prize Name"

    def test_delete_single_prize(self, client):
        """
        Test: Delete a single prize with ID 11 in catalog with ID 1.
        Expectation: The prize is successfully deleted.
        """
        response = client.delete('/api/catalogs/1/prize/11')
        assert response.status_code == 200  # Assuming 200 for successful deletion

    def test_verify_deletion_single_prize_11(self, client):
        """
        Test: Get details of a single prize with ID 11 in catalog with ID 1.
        Expectation: The prize details are returned.
        """
        response = client.get('/api/catalogs/1/prize/11')
        assert response.status_code == 404

    def test_verify_deletion_single_prize_11_other_way(self, client):
        """
        Test: Get details of a single prize with ID 11 in catalog with ID 1.
        Expectation: The prize details are returned.
        """
        response = client.get('/api/catalogs/1/prizes')

        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'prizes' in data
        assert isinstance(data['prizes'], list)
        assert len(data['prizes']) < 11  # Ensure there are prizes in the list

    def test_list_all_prizes_after_deletion(self, client):
        """
        Test: List all prizes in catalog with ID 1 after deletion.
        Expectation: The list of prizes does not include the deleted prize.
        """
        response = client.get('/api/catalogs/1/prizes')
        assert response.status_code == 200
        data = response.get_json()
        assert isinstance(data, dict)
        assert 'prizes' in data
        assert isinstance(data['prizes'], list)
        assert not any(prize['id'] == 11 for prize in data['prizes'])  # Ensure the deleted prize is not in the list

