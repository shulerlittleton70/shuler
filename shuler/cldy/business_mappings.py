# shuler/cldy/business_mappings.py

import requests

def get_business_mappings(token, env):
    """
    Fetches all business mappings from the Cloudability API, using Frontdoor authentication.

    Args:
        token (str): The Frontdoor token retrieved via frontdoor_auth().
        env (str): The environment ID (apptio-current-environment).

    Returns:
        list: A list of business mapping dictionaries.

    Raises:
        Exception: If the API call fails or returns an error.
    """
    url = "https://api.cloudability.com/v3/business-mappings"
    headers = {
        "apptio-opentoken": token,
        "apptio-current-environment": env,
        "Accept": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises HTTPError if the response was unsuccessful
        business_mappings = response.json()
        return business_mappings
    except requests.exceptions.HTTPError as http_err:
        raise Exception(f"HTTP error occurred: {http_err} - Response: {response.text}")
    except requests.exceptions.RequestException as req_err:
        raise Exception(f"Request error occurred: {req_err}")
    except Exception as err:
        raise Exception(f"An unexpected error occurred: {err}")

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