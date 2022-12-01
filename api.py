"""Petfinder API functions"""

import os
from dotenv import load_dotenv
import requests
from random import choice

load_dotenv()

PETFINDER_API_KEY = os.environ['PETFINDER_API_KEY']
PETFINDER_SECRET_KEY = os.environ['PETFINDER_SECRET_KEY']

OAUTH_URL = 'https://api.petfinder.com/v2/oauth2/token'
API_URL = 'https://api.petfinder.com/v2/animals?limit=100'

# payload = {'limit': '100'}
# params=payload

def update_auth_token_string():
    """Request new Oauth token from Petfinder."""
    data = {
        'grant_type': 'client_credentials',
        'client_id': PETFINDER_API_KEY,
        'client_secret': PETFINDER_SECRET_KEY,
    }
    response = requests.post(OAUTH_URL, data=data)

    # TODO: add status code validation
    decoded_response = response.json() # if r.status_code == 200 else error

    return f"{decoded_response['token_type']} {decoded_response['access_token']}"

def get_random_pet():
    """Get a random pet from Petfinder and return name, age, and photo URL."""
    token_string = update_auth_token_string()
    headers = {
        'authorization': token_string,
    }
    params = {
        'limit': 100,
    }
    response = requests.get(API_URL, headers=headers, params=params)

    decoded_response = response.json()

    pet_data = choice(decoded_response['animals'])

    pet = {
        'name': pet_data['name'],
        'age': pet_data['age'],
        'photo_url': pet_data['photos'][0]['small'] if pet_data['photos'] else None
    }

    return pet
