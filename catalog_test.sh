#!/bin/bash
# catalog_test.sh
# This script performs curl commands to test the API endpoints related to catalog operations.
# It includes requests to list all catalogs, create a new catalog, update a catalog, delete a catalog, and recreate a catalog.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

echo "Catalog API Test Script"
echo "-----------------------"

# List all catalogs
echo "Listing all catalogs:"
echo "GET /api/catalogs"
curl -X GET 'http://localhost:5000/api/catalogs'
echo
echo "------------------------------------------------------"

# Create a new catalog
echo "Creating a new catalog:"
echo "POST /api/catalog"
curl -X POST 'http://localhost:5000/api/catalog' -H 'Content-Type: application/json' -d '{}'
echo
echo "------------------------------------------------------"

# List all catalogs
echo "Listing all catalogs:"
echo "GET /api/catalogs"
curl -X GET 'http://localhost:5000/api/catalogs'
echo
echo "------------------------------------------------------"

# Get details of a single catalog (ID 6)
echo "Getting details of catalog with ID 6:"
echo "GET /api/catalog/6"
curl -X GET 'http://localhost:5000/api/catalog/6'
echo
echo "------------------------------------------------------"

# Delete a catalog (ID 3)
echo "Deleting catalog with ID 3:"
echo "DELETE /api/catalog/3"
curl -X DELETE 'http://localhost:5000/api/catalog/3'
echo
echo "------------------------------------------------------"

# List all catalogs
echo "Listing all catalogs:"
echo "GET /api/catalogs"
curl -X GET 'http://localhost:5000/api/catalogs'
echo
echo "------------------------------------------------------"

# Recreate the catalog with ID 3
echo "Recreating catalog with ID 3:"
echo "POST /api/catalog"
curl -X POST 'http://localhost:5000/api/catalog' -H 'Content-Type: application/json' -d '{}'
echo
echo "------------------------------------------------------"

# List all catalogs
echo "Listing all catalogs:"
echo "GET /api/catalogs"
curl -X GET 'http://localhost:5000/api/catalogs'
echo
echo "------------------------------------------------------"

echo "Catalog API Test Script Completed"

