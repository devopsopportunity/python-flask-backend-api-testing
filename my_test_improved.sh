#!/bin/bash
# my_test_improved.sh
# Enhanced script to perform curl commands to test the API endpoints.
# It includes various curl requests to retrieve prizes filtered by description and paginated.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

echo "Welcome to MyTest!"
echo "------------------"

BASE_URL='http://localhost:5000/api/catalogs'

# Function to perform curl request and validate response
perform_curl() {
  endpoint=$1
  expected_total=$2
  expected_len=$3

  response=$(curl -s -g "${BASE_URL}${endpoint}")
  actual_total=$(echo $response | jq '.total')
  actual_len=$(echo $response | jq '.prizes | length')

  if [ "$actual_total" == "$expected_total" ] && [ "$actual_len" == "$expected_len" ]; then
    echo "Test passed for ${endpoint}"
  else
    echo "Test failed for ${endpoint}"
    echo "Expected total: ${expected_total}, Actual total: ${actual_total}"
    echo "Expected length: ${expected_len}, Actual length: ${actual_len}"
  fi
}

# Test cases
perform_curl "/1/prizes" 10 10
perform_curl "/2/prizes?filter={\"description\":\"prize\"}&pagination={\"page\":1,\"per_page\":1}" 1 1
perform_curl "/3/prizes?filter={\"description\":\"prize\"}&pagination={\"page\":1,\"per_page\":4}" 4 4
perform_curl "/3/prizes?filter={\"description\":\"prize\"}&pagination={\"page\":2,\"per_page\":4}" 4 4
perform_curl "/3/prizes?filter={\"description\":\"prize\"}&pagination={\"page\":3,\"per_page\":4}" 2 2
perform_curl "/1/prizes?filter={\"description\":\"hello\"}&pagination={\"page\":1,\"per_page\":5}" 0 0
perform_curl "/1/prizes?filter={\"description\":\"script\"}&pagination={\"page\":1,\"per_page\":5}" 5 5
perform_curl "/1/prizes?filter={\"id\":\"1\"}&pagination={\"page\":1,\"per_page\":5}" 1 1
perform_curl "/1/prizes?filter={\"id\":\"2\",\"description\":\"script\"}&pagination={\"page\":1,\"per_page\":5}" 5 5
perform_curl "/1/prizes?filter={\"id\":\"2\",\"description\":\"hello\"}&pagination={\"page\":1,\"per_page\":5}" 1 1
perform_curl "/1/prizes?filter={\"id\":\"2\",\"description\":\"hello\",\"logical_operator\":\"AND\"}&pagination={\"page\":1,\"per_page\":5}" 0 0
perform_curl "/1/prizes?filter={\"id\":\"2\",\"description\":\"script\",\"logical_operator\":\"AND\"}&pagination={\"page\":1,\"per_page\":5}" 1 1
perform_curl "/1/prizes?filter={\"id\":\"2\",\"description\":\"hello\",\"logical_operator\":\"OR\"}&pagination={\"page\":1,\"per_page\":5}" 1 1

