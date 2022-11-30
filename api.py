"""Petfinder API functions"""

import os
from dotenv import load_dotenv
import requests

load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

OAUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'
API_URL = 'https://api.petfinder.com/v2/animals?limit=100'

# payload = {'limit': '100'}
# params=payload

def update_auth_token():
    """Request new Oauth token from Petfinder."""
    data = {
        'grant_type': 'client_credentials',
        'client_id': PETFINDER_API_KEY,
        'client_secret': PETFINDER_SECRET_KEY,
    }
    response = requests.post(OAUTH_URL, data=data)

    # TODO: add status code validation
    decoded_response = response.json() # if r.status_code == 200 else error

    oauth_token = decoded_response['access_token']

    return oauth_token

