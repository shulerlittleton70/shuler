import requests
import logging

logger = logging.getLogger(__name__)

class FrontdoorClient:
    def __init__(self, public, secret, domain, env_name):
        """
        Initializes the FrontdoorClient.

        Args:
            public (str): Frontdoor Public key (keyAccess).
            secret (str): Frontdoor Secret key (keySecret).
            domain (str): Customer's domain (e.g., firstdata.com).
            env_name (str): Environment name (e.g., main, prod).
        """
        self.public = public
        self.secret = secret
        self.domain = domain
        self.env_name = env_name
        self.token = None
        self.environment_id = None

    def authenticate(self):
        """
        Authenticates with Frontdoor and retrieves both the OpenToken and Environment ID.

        Returns:
            dict: {
                "token": <apptio-opentoken>,
                "environment_id": <environment id>
            }

        Raises:
            Exception: If authentication or environment lookup fails.
        """
        self._get_token()
        self._get_environment_id()
        return {
            "token": self.token,
            "environment_id": self.environment_id
        }

    def _get_token(self):
        url = "https://frontdoor.apptio.com/service/apikeylogin"
        payload = {
            "keyAccess": self.public,
            "keySecret": self.secret
        }
        headers = {
            "Content-Type": "application/json"
        }

        logger.info("Starting Frontdoor authentication to get OpenToken...")

        try:
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            self.token = response.headers.get("apptio-opentoken")

            if not self.token:
                logger.error("Authentication succeeded but no OpenToken found in response headers.")
                raise Exception("No OpenToken found in response headers.")

            logger.info("Successfully retrieved OpenToken.")
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error during authentication: {http_err} - Response: {response.text}")
            raise
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request error during authentication: {req_err}")
            raise
        except Exception as err:
            logger.error(f"Unexpected error during authentication: {err}")
            raise

    def _get_environment_id(self):
        if not self.token:
            raise Exception("Cannot fetch environment ID without a valid OpenToken.")

        url = f"https://frontdoor.apptio.com/api/environment/{self.domain}/{self.env_name}"
        headers = {
            "Content-Type": "application/json",
            "apptio-opentoken": self.token
        }

        logger.info(f"Fetching environment ID for domain '{self.domain}' and environment '{self.env_name}'...")

        try:
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            data = response.json()
            self.environment_id = data.get("id")

            if not self.environment_id:
                logger.error("Environment lookup succeeded but no 'id' found in response JSON.")
                raise Exception("No environment ID ('id') found in response.")

            logger.info(f"Successfully retrieved environment ID: {self.environment_id}")
        except requests.exceptions.HTTPError as http_err:
            logger.error(f"HTTP error during environment lookup: {http_err} - Response: {response.text}")
            raise
        except requests.exceptions.RequestException as req_err:
            logger.error(f"Request error during environment lookup: {req_err}")
            raise
        except Exception as err:
            logger.error(f"Unexpected error during environment lookup: {err}")
            raise
