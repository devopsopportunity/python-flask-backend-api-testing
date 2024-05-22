# Welcome to Python Flask Backend API Testing!

This repository contains backend API code developed in Python using the Flask framework, along with comprehensive testing scripts to validate and verify API endpoints.

## Exercise Overview

### Goal

Assess your skills in REST API development using object-oriented concepts, exception handling, and good programming practices.

### Description

Implement a REST API in Python that lists prizes by catalog, meeting the following requirements:

#### Functionality

**List Prizes**:
- Receives the following parameters:
  - `catalog_id` (number): Catalog identifier (required).
  - `filter` (optional): Dictionary with the fields:
    - `id` (optional): Prize identifier.
    - `description` (optional): Prize description (substring search).
  - `pagination` (optional): Dictionary with the fields:
    - `page` (number): Page number to be returned (starts at 1).
    - `per_page` (number): Number of prizes per page.
- Returns a JSON object with:
  - `total` (number): Total number of prizes found.
  - `prizes` (list): List of objects with the prize data:
    - `id` (number): Prize identifier.
    - `title` (string): Prize title.
    - `description` (string): Prize description.
    - `image` (string): URL of the prize image.

### Requirements

1. **API Development**:
   - Create an API class that defines the API routes and methods.
   - Create a `list_prizes` method that receives the parameters and returns the list of prizes.
   - Validate input parameters and return error messages in case of errors.
   - Handle exceptions and return appropriate error messages.
   - Use the Flask module to create the REST API (optional but a plus).
   - Define the `/api/catalogs/<catalog_id>/prizes` route.

2. **Data Simulation**:
   - Create a `Prize` class that represents a prize.
   - Create a class that simulates the database query, mocking the data instead of connecting and executing a query.
   - Create a `get_prizes` method in that class, which returns a mock list of prizes.
   - The `get_prizes` method should receive the `catalog_id`, `filter`, and `pagination` parameters.
   - The `get_prizes` method should filter the list of prizes according to the filter and pagination parameters.

3. **Testing**:
   - Write unit tests for the `list_prizes` method using the pytest module (optional but a plus).
   - Test different input scenarios and parameter validation.
   - Test the API behavior with different filters and pagination.

4. **Code Versioning**:
   - Upload the code in a public git repository for evaluation.

5. **Documentation**:
   - Provide the necessary documentation to correctly use and test the API method.

### Examples

#### Example 1: List all prizes from catalog 1

**Input**:
```
GET /api/catalogs/1/prizes
```

**Output**:
```json
{
  "total": 10,
  "prizes": [
    {
      "id": 1,
      "title": "Prize 1",
      "description": "Description of prize 1",
      "image": "https://example.com/image1.png"
    },
    {
      "id": 2,
      "title": "Prize 2",
      "description": "Description of prize 2",
      "image": "https://example.com/image2.png"
    },
    ...
  ]
}
```

## Installation

1. Ensure you have Python 3 installed on your system.

2. Install the required dependencies:
   ```sh
   pip install flask pytest
   ```

## Project Structure

### Main Application

- **`app.py`**: Implements a Flask API for managing catalogs and prizes, handling CRUD operations.

### Data Simulation

- **`data_simulation.py`**: Provides simulated data for the prize database, including functionality for CRUD operations.

### Configuration and Fixtures

- **`conftest.py`**: Contains fixtures for API endpoint testing using Pytest. Includes various requests for retrieving prizes filtered by description and pagination.

### Shell Scripts for Testing

- **`catalog_test.sh`**: Executes curl commands to validate the API endpoints for catalog operations, covering CRUD scenarios.
- **`my_test.sh`**: Conducts API endpoint testing via curl commands, focusing on `list_prizes` functionality and other API features.
- **`my_test_improved.sh`**: Enhanced version of `my_test.sh` for thorough examination of the `list_prizes` functionality.
- **`prize_test.sh`**: Tests API endpoints related to prize operations using curl commands, involving CRUD testing.

### Pytest Test Scripts

- **`pytest_fixture_api.py`**: Contains Pytest test cases for prize API endpoints, verifying the `list_prizes` method using Pytest fixtures.
- **`pytest_fixture_catalog.py`**: Holds Pytest test cases for catalog API endpoints, utilizing Pytest fixtures for efficient testing setup and covering CRUD scenarios.
- **`pytest_fixture_single_prize.py`**: Contains Pytest test cases for single prize API endpoints, involving CRUD operations.
- **`pytest_mark_parametrize_api.py`**: Performs HTTP requests to test API endpoints, covering various use cases of the `list_prizes` functionality with parameterized testing using `@pytest.mark.parametrize`.
- **`test_api.py`**: Conducts HTTP requests to test API endpoints comprehensively covering the `list_prizes` method.

## Running the Tests

### Using Shell Scripts

1. Start the Flask application in a separate shell:
   ```sh
   python3 app.py
   ```

2. Execute the relevant test scripts:

   - **Test Batch - `list_prizes`**:
     - `./my_test.sh`
     - `./my_test_improved.sh`

   - **Test Batch - `CRUD`**:
     - `./prize_test.sh`
     - `./catalog_test.sh`

### Using Pytest

1. Start the Flask application in a separate shell (for specific tests):
   ```sh
   python3 app.py
   ```

2. Run the tests:

   - **Test API Python REST `list_prizes`**:
     - With a running Flask application:
       ```sh
       pytest test_api.py
       ```
     - Without a running Flask application:
       ```sh
       pytest pytest_fixture_api.py
       pytest pytest_mark_parametrize_api.py
       ```

   - **Test API Python `CRUD`** (no need for a separate Flask application shell):
     ```sh
     pytest pytest_fixture_catalog.py
     pytest pytest_fixture_single_prize.py
     ```

By following these steps, you can set up and test the Flask API endpoints for managing catalogs and prizes effectively.
