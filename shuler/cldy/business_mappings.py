# shuler/cldy/business_mappings.py

def get_business_mappings(token):
    """
    Retrieve all business mappings.

    Args:
        token (str): Bearer token for authentication.

    Returns:
        dict: Full list of business mappings.
    """
    pass


def get_business_mapping_index(token):
    """
    Retrieve all business mappings but only return their names and indexes.

    Args:
        token (str): Bearer token for authentication.

    Returns:
        list of dict: Each dict contains 'name' and 'index' of a business mapping.
    """
    pass


def get_business_mapping(token, index):
    """
    Retrieve a specific business mapping by index.

    Args:
        token (str): Bearer token for authentication.
        index (str): Index of the business mapping.

    Returns:
        dict: Business mapping details.
    """
    pass


def update_business_mapping(token, index, payload):
    """
    Update a specific business mapping.

    Args:
        token (str): Bearer token for authentication.
        index (str): Index of the business mapping.
        payload (dict): The updated business mapping payload.

    Returns:
        dict: API response confirming the update.
    """
    pass


def create_business_mapping(token, payload):
    """
    Create a new business mapping.

    Args:
        token (str): Bearer token for authentication.
        payload (dict): The new business mapping payload.

    Returns:
        dict: API response confirming the creation.
    """
    pass


def delete_business_mapping(token, index):
    """
    Delete a specific business mapping by index.

    Args:
        token (str): Bearer token for authentication.
        index (str): Index of the business mapping to delete.

    Returns:
        dict: API response confirming the deletion.
    """
    pass