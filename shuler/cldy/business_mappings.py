# shuler/cldy/business_mappings.py

import requests

from shuler.auth import FrontdoorClient
import requests
import logging

logger = logging.getLogger(__name__)

def get_business_mappings(client: FrontdoorClient):
    """
    Fetches all business mappings using the authenticated FrontdoorClient.

    Args:
        client (FrontdoorClient): An authenticated FrontdoorClient instance.

    Returns:
        list: A list of business mapping dictionaries.

    Raises:
        Exception: If the request fails or if authentication is missing.
    """
    if not client.token or not client.environment_id:
        raise Exception("Client is not authenticated. Please call client.authenticate() first.")

    url = "https://api.cloudability.com/v3/business-mappings"
    headers = {
        "apptio-opentoken": client.token,
        "apptio-current-environment": client.environment_id,
        "Accept": "application/json"
    }

    logger.info("Fetching business mappings...")

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        logger.info("Successfully retrieved business mappings.")
        return data
    except requests.exceptions.HTTPError as http_err:
        logger.error(f"HTTP error while fetching business mappings: {http_err} - Response: {response.text}")
        raise
    except requests.exceptions.RequestException as req_err:
        logger.error(f"Request error while fetching business mappings: {req_err}")
        raise
    except Exception as err:
        logger.error(f"Unexpected error while fetching business mappings: {err}")
        raise


def get_business_mapping_index(client: FrontdoorClient):
    """
    Calls the Cloudability business mappings endpoint and:
    1️⃣ Prints a readable summary of all business mappings (excluding 'statements').
    2️⃣ Returns a list of cleaned mappings (dicts) for future programmatic use.

    Each returned dict includes:
    - name
    - index
    - kind
    - defaultValue
    - numberFormat
    - updatedAt
    """
    response = client.session.get(f"{client.base_url}/v3/business-mappings")
    response.raise_for_status()

    data = response.json()
    mappings = data.get('result', [])

    if not mappings:
        print("No business mappings found.")
        return []

    cleaned_mappings = []

    print("\nBusiness Mapping Index Summary:\n")
    for mapping in mappings:
        summary = {
            'name': mapping.get('name'),
            'index': mapping.get('index'),
            'kind': mapping.get('kind'),
            'defaultValue': mapping.get('defaultValue'),
            'numberFormat': mapping.get('numberFormat'),
            'updatedAt': mapping.get('updatedAt')
        }
        cleaned_mappings.append(summary)

        # Print each mapping in a clean format
        print(f"Name        : {summary['name']}")
        print(f"Index       : {summary['index']}")
        print(f"Kind        : {summary['kind']}")
        print(f"DefaultVal  : {summary['defaultValue']}")
        print(f"NumberFormat: {summary['numberFormat']}")
        print(f"UpdatedAt   : {summary['updatedAt']}")
        print("-" * 40)

    return cleaned_mappings



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