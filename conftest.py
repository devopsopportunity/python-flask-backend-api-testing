# conftest.py
# This script provides fixtures for testing the API endpoints by performing HTTP requests.
# It includes various requests to retrieve prizes filtered by description and paginated.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

import pytest
from app import app

@pytest.fixture
def client():
    """Fixture to provide a test client for making HTTP requests."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        with app.app_context():
            yield client

