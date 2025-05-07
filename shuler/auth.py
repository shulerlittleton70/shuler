# shuler/auth.py

import requests

def frontdoor_auth(client_id, client_secret, domain, env_id):
    """
    Authenticate against Apptio Frontdoor and return an access token.

    Args:
        client_id (str): Your Frontdoor client ID.
        client_secret (str): Your Frontdoor client secret.
        domain (str): The domain (e.g., 'company.com').
        env_id (str): The environment ID (Apptio environment).

    Returns:
        str: Bearer token for use in subsequent API calls.

    Raises:
        HTTPError: If the authentication request fails.
    """

    url = f"https://{domain}/frontdoor/v1/token"
    data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
        "environment_id": env_id,
    }
    response = requests.post(url, data=data)
    response.raise_for_status()
    token = response.json().get("access_token")
    return token