#!/bin/bash
# my_test.sh
# This script performs curl commands to test the API endpoints.
# It includes various curl requests to retrieve prizes filtered by description and paginated.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

echo "Welcome to MyTest!"
echo "------------------"

# Executing the first curl to retrieve the first prize
echo "Executing the first curl to retrieve the first prize:"
echo "GET /api/catalogs/1/prizes"
curl 'http://localhost:5000/api/catalogs/1/prizes'
echo
echo "------------------------------------------------------"

# Executing curls to retrieve prizes filtered by description and paginated

# Curl to retrieve prizes filtered by description "prize" and paginated
echo "Executing the second curl to retrieve prizes filtered by description 'prize' and paginated:"
echo "Expected: Pagination with 'prize' in description, 1 result"
echo 'GET /api/catalogs/2/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":1}'
curl -g 'http://localhost:5000/api/catalogs/2/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":1}'
echo

# Curl to retrieve prizes filtered by description "prize" and paginated
echo "Executing the third curl to retrieve prizes filtered by description 'prize' and paginated:"
echo "Expected: Pagination with 'prize' in description, up to 4 results"
echo 'GET /api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":4}'
curl -g 'http://localhost:5000/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":1,"per_page":4}'
echo

# Curl to retrieve prizes filtered by description "prize" and paginated
echo "Executing the fourth curl to retrieve prizes filtered by description 'prize' and paginated:"
echo "Expected: Pagination with 'prize' in description, up to 4 results (page 2)"
echo 'GET /api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":2,"per_page":4}'
curl -g 'http://localhost:5000/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":2,"per_page":4}'
echo

# Curl to retrieve prizes filtered by description "prize" and paginated
echo "Executing the fifth curl to retrieve prizes filtered by description 'prize' and paginated:"
echo "Expected: Pagination with 'prize' in description, up to 4 results (page 3)"
echo 'GET /api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":3,"per_page":4}'
curl -g 'http://localhost:5000/api/catalogs/3/prizes?filter={"description":"prize"}&pagination={"page":3,"per_page":4}'
echo

# Curl to retrieve prizes filtered by description "hello" and paginated
echo "Executing the sixth curl to retrieve prizes filtered by description 'hello' and paginated:"
echo "Expected: Pagination with 'hello' in description, no results"
echo 'GET /api/catalogs/1/prizes?filter={"description":"hello"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"description":"hello"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by description "script" and paginated
echo "Executing the seventh curl to retrieve prizes filtered by description 'script' and paginated:"
echo "Expected: Pagination with 'script' in description"
echo 'GET /api/catalogs/1/prizes?filter={"description":"script"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"description":"script"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "1" and paginated
echo "Executing the eighth curl to retrieve prizes filtered by ID '1' and paginated:"
echo "Expected: Pagination with ID '1'"
echo 'GET /api/catalogs/1/prizes?filter={"id":"1"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"1"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "2" and description "script"
echo "Executing the ninth curl to retrieve prizes filtered by ID '2' and description 'script':"
echo "Expected: Pagination with ID '2' and 'script' in description"
echo 'GET /api/catalogs/1/prizes?filter={"id":"2","description":"script"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"2","description":"script"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "2" and description "hello"
echo "Executing the tenth curl to retrieve prizes filtered by ID '2' and description 'hello':"
echo "Expected: Pagination with ID '2' and 'hello' in description"
echo 'GET /api/catalogs/1/prizes?filter={"id":"2","description":"hello"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"2","description":"hello"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "2" and description "hello" with logical operator AND
echo "Executing the eleventh curl to retrieve prizes filtered by ID '2' and description 'hello' with logical operator 'AND':"
echo "Expected: Pagination with ID '2' and 'hello' in description, using logical operator 'AND'"
echo 'GET /api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"AND"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"AND"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "2" and description "script" with logical operator AND
echo "Executing the twelfth curl to retrieve prizes filtered by ID '2' and description 'script' with logical operator 'AND':"
echo "Expected: Pagination with ID '2' and 'script' in description, using logical operator 'AND'"
echo 'GET /api/catalogs/1/prizes?filter={"id":"2","description":"script","logical_operator":"AND"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"2","description":"script","logical_operator":"AND"}&pagination={"page":1,"per_page":5}'
echo

# Curl to retrieve prizes filtered by ID "2" and description "hello" with logical operator OR
echo "Executing the thirteenth curl to retrieve prizes filtered by ID '2' and description 'hello' with logical operator 'OR':"
echo "Expected: Pagination with ID '2' and 'hello' in description, using logical operator 'OR'"
echo 'GET /api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"OR"}&pagination={"page":1,"per_page":5}'
curl -g 'http://localhost:5000/api/catalogs/1/prizes?filter={"id":"2","description":"hello","logical_operator":"OR"}&pagination={"page":1,"per_page":5}'
echo

