# app.py
# This script implements a Flask API for managing catalogs and prizes.
# It provides endpoints for listing, creating, updating, and deleting catalogs and prizes.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

from flask import Flask, jsonify, request
import json
from data_simulation import Prize  # Importing Prize from data_simulation.py

app = Flask(__name__)
app.json.sort_keys = False

prize = Prize()

def validate_params(params):
    try:
        return json.loads(params) if params else {}
    except json.JSONDecodeError:
        return None

@app.route("/api/catalogs/<catalog_id>/prizes", methods=["GET"])
def list_prizes(catalog_id):
    # Validate catalog_id
    if not catalog_id.isdigit() or int(catalog_id) < 1 or int(catalog_id) > 5:
        return jsonify({"error": "Catalog ID should be an integer between 1 and 5."}), 400
    
    catalog_id = int(catalog_id)  # Convert to integer after validation
    
    filter_param = request.args.get("filter")
    pagination_param = request.args.get("pagination")
    
    filter_dict = validate_params(filter_param)
    pagination_dict = validate_params(pagination_param)
    
    # Validate pagination parameters
    if pagination_dict:
        page = pagination_dict.get('page')
        per_page = pagination_dict.get('per_page')
        if not str(page).isdigit() or not str(per_page).isdigit() or int(page) < 1 or int(per_page) < 1 or int(per_page) > 10:
            return jsonify({"error": "Invalid pagination format. Page and per_page should be positive integers with per_page no greater than 10."}), 400
    
    if filter_dict:
        # Validate filter parameters
        if 'id' in filter_dict and (not str(filter_dict['id']).isdigit() or int(filter_dict['id']) < 1):
            return jsonify({"error": "Filter ID should be a positive integer."}), 400
        
        if 'description' in filter_dict and len(filter_dict['description']) > 80:
            return jsonify({"error": "Filter description should not exceed 80 characters."}), 400
        
        if 'logical_operator' in filter_dict and filter_dict['logical_operator'].upper() not in ['AND', 'OR']:
            return jsonify({"error": "Invalid logical operator. Use 'AND' or 'OR'."}), 400
    
    if filter_dict is None or pagination_dict is None:
        return jsonify({"error": "Invalid filter or pagination format."}), 400
    
    prizes = prize.get_prizes(catalog_id, filter_dict, pagination_dict)
    
    if prizes is None:
        return jsonify({"error": f"Catalog {catalog_id} not found. The catalog ID should be an integer between 1 and 5."}), 404
    
    prizes_list = [prize.__dict__ for prize in prizes]
    total_prizes = len(prizes_list)
    
    response = {
        "total": total_prizes,
        "prizes": prizes_list
    }
    
    return jsonify(response)

@app.route("/api/catalogs/<catalog_id>/prize/<prize_id>", methods=["GET"])
def get_prize(catalog_id, prize_id):
    # Check if both the catalog ID and the prize ID are valid integers
    if not catalog_id.isdigit() or not prize_id.isdigit():
        return jsonify({"error": "Both catalog ID and prize ID should be integers."}), 400
    
    catalog_id = int(catalog_id)
    prize_id = int(prize_id)

    prizes = prize.get_prizes(catalog_id)
    if prizes is None:
        return jsonify({"error": f"Catalog {catalog_id} not found."}), 404

    prize_item = next((p for p in prizes if p.id == prize_id), None)
    if prize_item is None:
        return jsonify({"error": f"Prize with ID {prize_id} not found in catalog {catalog_id}."}), 404

    return jsonify(prize_item.__dict__), 200

# Update the details of a specific prize in a catalog
@app.route("/api/catalogs/<catalog_id>/prize/<prize_id>", methods=["PUT"])
def update_prize(catalog_id, prize_id):
    # Check if both the catalog ID and the prize ID are valid integers
    if not catalog_id.isdigit() or not prize_id.isdigit():
        return jsonify({"error": "Both catalog ID and prize ID should be integers."}), 400
    
    catalog_id = int(catalog_id)
    prize_id = int(prize_id)

    # Retrieve the prize data from JSON request
    data = request.json
    
    # Check if valid data is provided for prize update
    if not data:
        return jsonify({"error": "No data provided for update."}), 400

    # Get the existing prize details
    existing_prize = prize.get_prize(catalog_id, prize_id)
    if existing_prize is None:
        return jsonify({"error": f"Prize with ID {prize_id} not found in catalog {catalog_id}."}), 404

    # Update only the attributes provided in the JSON request
    for key, value in data.items():
        setattr(existing_prize, key, value)

    # Save the updated prize
    updated_prize = prize.update_prize(catalog_id, prize_id, existing_prize)

    # Return the updated prize details
    return jsonify(updated_prize.__dict__), 200

# Create a new prize within a catalog
@app.route("/api/catalogs/<catalog_id>/prize", methods=["POST"])
def create_prize(catalog_id):
    # Check if the catalog ID is a valid integer
    if not catalog_id.isdigit() or int(catalog_id) < 1 or int(catalog_id) > 5:
        return jsonify({"error": "Catalog ID should be a valid integer between 1 and 5."}), 400
    
    catalog_id = int(catalog_id)

    # Retrieve the data for the new prize from the JSON request
    data = request.json
    
    # Check if valid data is provided for creating the prize
    if not data:
        return jsonify({"error": "No data provided for creating prize."}), 400
    
    new_prize = prize.create_prize(catalog_id, data)
    if new_prize is None:
        return jsonify({"error": f"Catalog {catalog_id} not found."}), 404

    return jsonify(new_prize.__dict__), 201

# Delete a specific prize within a catalog
@app.route("/api/catalogs/<catalog_id>/prize/<prize_id>", methods=["DELETE"])
def delete_prize(catalog_id, prize_id):
    # Check if both the catalog ID and the prize ID are valid integers
    if not catalog_id.isdigit() or not prize_id.isdigit():
        return jsonify({"error": "Both catalog ID and prize ID should be integers."}), 400
    
    catalog_id = int(catalog_id)
    prize_id = int(prize_id)

    success = prize.delete_prize(catalog_id, prize_id)
    if not success:
        return jsonify({"error": f"Prize with ID {prize_id} not found in catalog {catalog_id}."}), 404

    return jsonify({"message": f"Prize with ID {prize_id} in catalog with ID {catalog_id} deleted successfully."}), 200

# List all catalogs
@app.route("/api/catalogs", methods=["GET"])
def list_catalogs():
    catalogs = prize.catalog.catalogs
    catalog_list = [{"id": id, "name": f"Catalog {id}"} for id in catalogs]
    
    return jsonify({"catalogs": catalog_list}), 200

# Get details of a single catalog
@app.route("/api/catalog/<catalog_id>", methods=["GET"])
def get_catalog(catalog_id):
    try:
        catalog_id = int(catalog_id)
    except ValueError:
        return jsonify({"error": "Catalog ID should be a valid integer."}), 400

    if catalog_id not in prize.catalog.catalogs:
        return jsonify({"error": "Catalog not found."}), 404
    
    catalog_details = {
        "id": catalog_id,
        "name": f"Catalog {catalog_id}"
    }
    return jsonify({"catalog": catalog_details}), 200
    
# Delete a catalog
@app.route("/api/catalog/<catalog_id>", methods=["DELETE"])
def delete_catalog(catalog_id):
    # Check if the catalog ID is a valid integer
    if not catalog_id.isdigit() or int(catalog_id) < 1 or int(catalog_id) > 5:
        return jsonify({"error": "Catalog ID should be a valid integer between 1 and 5."}), 400
    
    catalog_id = int(catalog_id)

    success = prize.catalog.delete_catalog(catalog_id)
    if not success:
        return jsonify({"error": f"Catalog {catalog_id} not found."}), 404

    return jsonify({"message": f"Catalog with ID {catalog_id} deleted successfully."}), 200

# Create a new catalog with the first available ID
@app.route("/api/catalog", methods=["POST"])
def create_catalog():
    # Retrieve the data for the new catalog from the JSON request
    data = request.json

    # Determine the first available catalog ID
    existing_ids = set(prize.catalog.catalogs.keys())
    available_id = 1
    while available_id in existing_ids:
        available_id += 1

    success = prize.catalog.create_catalog(available_id)
    if not success:
        return jsonify({"error": f"Failed to create catalog with ID {available_id}."}), 500

    return jsonify({"message": f"Catalog with ID {available_id} created successfully.", "catalog_id": available_id}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)

