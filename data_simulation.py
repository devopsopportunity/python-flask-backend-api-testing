# data_simulation.py - Simulated data for prize database
# This module provides simulated data for a prize database, including catalogs and prizes.

# Authors: Edoardo Sabatini - Data Worker and ChatGPT 3.5 Python Programmer
# Date: May 22, 2024

class PrizeDetails:
    """Represents a prize."""
    def __init__(self, id, title, description, image):
        self.id = id
        self.title = title
        self.description = description
        self.image = image

class Catalog:
    """Represents a catalog of prizes."""
    def __init__(self):
        self.catalogs = {}
        self.offsets = {}  # Dictionary to store offsets for each catalog

    def add_prize(self, catalog_id, prize):
        """Add a prize to the specified catalog."""
        if catalog_id not in self.catalogs:
            self.catalogs[catalog_id] = []
            self.offsets[catalog_id] = (catalog_id - 1) * 10  # Calculate offset
        self.catalogs[catalog_id].append(prize)

    def get_catalog(self, catalog_id):
        """Retrieve the prizes for the specified catalog."""
        return self.catalogs.get(catalog_id, [])

    def print_catalogs(self, is_debug=False):
        """Print all catalogs and associated prizes."""
        if is_debug:
            for catalog_id, prizes in self.catalogs.items():
                print(f"Catalog {catalog_id}:")
                for prize in prizes:
                    print(f"  Prize ID: {prize.id}, Title: {prize.title}, Description: {prize.description}, Image: {prize.image}")
                    
    def create_catalog(self, catalog_id):
        """Create a new catalog."""
        if catalog_id in self.catalogs:
            return False  # Catalog already exists
        self.catalogs[catalog_id] = []
        self.offsets[catalog_id] = (catalog_id - 1) * 10  # Calculate offset
        return True

    def delete_catalog(self, catalog_id):
        """Delete a catalog."""
        if catalog_id not in self.catalogs:
            return False  # Catalog doesn't exist
        del self.catalogs[catalog_id]
        del self.offsets[catalog_id]
        return True

class Prize:
    """Represents prizes and provides methods for retrieving, creating, updating, and deleting prizes from the catalog."""
    def __init__(self):
        self.catalog = self.InitializeMockData(5, 10)  # Generate 5 catalogs with 10 prizes each
        is_debug = False  # True
        self.catalog.print_catalogs(is_debug)

    def get_prizes(self, catalog_id, filter=None, pagination=None):
        """Retrieve prizes from the specified catalog, applying filters and pagination if provided."""
        # Simulated database query
        prizes_data = self.catalog.get_catalog(catalog_id)
        if not prizes_data:
            return None
        
        # Apply filters if provided
        if filter:
            filter_id = None
            filter_description = None
            logical_operator = filter.get('logical_operator', 'OR')
            
            if 'id' in filter:
                filter_id = int(filter['id']) if filter['id'].isdigit() else None

            if 'description' in filter:
                filter_description = filter['description']

            if filter_id is not None or filter_description is not None:
                if logical_operator.upper() == 'AND':
                    if filter_id is not None and filter_description is not None:
                        prizes_data = [prize for prize in prizes_data if prize.id == filter_id and filter_description in prize.description]
                    elif filter_id is not None:
                        prizes_data = [prize for prize in prizes_data if prize.id == filter_id]
                    elif filter_description is not None:
                        prizes_data = [prize for prize in prizes_data if filter_description in prize.description]
                else:
                    if filter_id is not None and filter_description is not None:
                        prizes_data = [prize for prize in prizes_data if prize.id == filter_id or filter_description in prize.description]
                    elif filter_id is not None:
                        prizes_data = [prize for prize in prizes_data if prize.id == filter_id]
                    elif filter_description is not None:
                        prizes_data = [prize for prize in prizes_data if filter_description in prize.description]
            else:
                prizes_data = []
        
        # Apply pagination if provided
        if pagination:
            page = pagination.get('page', 1)
            per_page = pagination.get('per_page', len(prizes_data))
            start_index = (page - 1) * per_page
            end_index = start_index + per_page
            prizes_data = prizes_data[start_index:end_index]

        return prizes_data

    def InitializeMockData(self, num_catalogs, prizes_per_catalog):
        """Generate mock data and add it to the catalog."""
        catalog = Catalog()

        for catalog_id in range(1, num_catalogs + 1):
            for prize_id in range(1, prizes_per_catalog + 1):
                # Add offset to prize_id based on catalog
                adjusted_prize_id = prize_id + (catalog_id - 1) * prizes_per_catalog
                prize = PrizeDetails(
                    adjusted_prize_id,  # Use adjusted prize_id
                    f"Prize {adjusted_prize_id}",
                    f"Description of prize {adjusted_prize_id} in catalog {catalog_id}",
                    f"https://example.com/image{adjusted_prize_id}.png"
                )
                catalog.add_prize(catalog_id, prize)
        
        return catalog

    def create_prize(self, catalog_id, prize_data):
        """Create a new prize in the specified catalog."""
        catalog = self.catalog.get_catalog(catalog_id)
        if catalog is None:
            return None

        new_id = max(prize.id for prize in catalog) + 1 if catalog else 1
        new_prize = PrizeDetails(new_id, prize_data['title'], prize_data['description'], prize_data['image'])
        self.catalog.add_prize(catalog_id, new_prize)
        return new_prize

    def update_prize(self, catalog_id, prize_id, existing_prize):
        """Update an existing prize in the specified catalog."""
        catalog = self.catalog.get_catalog(catalog_id)
        if catalog is None:
            return None

        for prize in catalog:
            if prize.id == prize_id:
                prize.title = existing_prize.title
                prize.description = existing_prize.description
                prize.image = existing_prize.image
                return prize

        return None

    def delete_prize(self, catalog_id, prize_id):
        """Delete a prize from the specified catalog."""
        catalog = self.catalog.get_catalog(catalog_id)
        if catalog is None:
            return False

        for i, prize in enumerate(catalog):
            if prize.id == prize_id:
                del catalog[i]
                return True

        return False

    def get_prize(self, catalog_id, prize_id):
        """Get a specific prize from the specified catalog."""
        catalog = self.catalog.get_catalog(catalog_id)
        if catalog is None:
            return False

        for prize in catalog:
            if prize.id == prize_id:
                return prize

        return None

