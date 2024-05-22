#!/bin/bash
# prize_test.sh
# This script performs curl commands to test the API endpoints related to prize operations.
# It includes requests to list all prizes in a catalog, create a new prize, update a prize, delete a prize, and retrieve details of a single prize.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

echo "Prize API Test Script"
echo "-----------------------"

# List all prizes in a catalog (Catalog ID 1)
echo "Listing all prizes in catalog with ID 1:"
echo "GET /api/catalogs/1/prizes"
curl -X GET 'http://localhost:5000/api/catalogs/1/prizes'
echo
echo "------------------------------------------------------"

# Create a new prize in a catalog (Catalog ID 1)
echo "Creating a new prize in catalog with ID 1:"
echo "POST /api/catalogs/1/prize"
curl -X POST 'http://localhost:5000/api/catalogs/1/prize' -H 'Content-Type: application/json' -d '{"title": "New Prize", "description": "Description of the new prize", "image": "new_image_url"}'
echo
echo "------------------------------------------------------"

# List all prizes in a catalog (Catalog ID 1)
echo "Listing all prizes in catalog with ID 1:"
echo "GET /api/catalogs/1/prizes"
curl -X GET 'http://localhost:5000/api/catalogs/1/prizes'
echo
echo "------------------------------------------------------"

# Get details of a single prize in a catalog (Catalog ID 1, Prize ID 11)
echo "Getting details of prize with ID 1 in catalog with ID 11:"
echo "GET /api/catalogs/1/prize/11"
curl -X GET 'http://localhost:5000/api/catalogs/1/prize/11'
echo
echo "------------------------------------------------------"

# Update details of a single prize in a catalog (Catalog ID 1, Prize ID 11)
echo "Updating details of prize with ID 11 in catalog with ID 1:"
echo "PUT /api/catalogs/1/prize/11"
curl -X PUT 'http://localhost:5000/api/catalogs/1/prize/11' -H 'Content-Type: application/json' -d '{"title": "Updated Prize Name"}'
echo
echo "------------------------------------------------------"

# Get details of a single prize in a catalog (Catalog ID 1, Prize ID 11)
echo "Getting details of prize with ID 1 in catalog with ID 11:"
echo "GET /api/catalogs/1/prize/11"
curl -X GET 'http://localhost:5000/api/catalogs/1/prize/11'
echo
echo "------------------------------------------------------"

# Delete a single prize in a catalog (Catalog ID 1, Prize ID 11)
echo "Deleting prize with ID 1 in catalog with ID 11:"
echo "DELETE /api/catalogs/1/prize/11"
curl -X DELETE 'http://localhost:5000/api/catalogs/1/prize/11'
echo
echo "------------------------------------------------------"

# List all prizes in a catalog after deletion
echo "Listing all prizes in catalog with ID 1 after deletion:"
echo "GET /api/catalogs/1/prizes"
curl -X GET 'http://localhost:5000/api/catalogs/1/prizes'
echo
echo "------------------------------------------------------"

echo "Prize API Test Script Completed"








