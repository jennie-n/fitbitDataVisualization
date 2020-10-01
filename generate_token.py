import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
from dotenv import load_dotenv

load_dotenv()
import os

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
AUTH = os.getenv('AUTH')
USER_ID = os.getenv('USER_ID')

def get_new_refresh_token():
    headers = {'Authorization': f'Basic {AUTH}', 'Content-Type': 'application/x-www-form-urlencoded'}
    params = { 'grant_type': 'refresh_token', 'refresh_token': REFRESH_TOKEN }
    new_token_object = requests.post('https://api.fitbit.com/oauth2/token', headers=headers, params=params)
    # print(f'New Token: {new_token_object}')
    # print('JSON ACCESS TOKEN: ' + new_token_object.json()['access_token'])
    # print('JSON REFRESH TOKEN: ' + new_token_object.json()['refresh_token'])
    new_access_token = new_token_object.json()['access_token']
    new_refresh_token = new_token_object.json()['refresh_token']
    return [new_access_token, new_refresh_token]

def overwrite_tokens(new_tokens):
    a = open('.env', 'r+')
    lines = a.readlines() # read all the lines from the file into an array
    offset = 0 # used to keep track of the offset for overwriting new .env values

    # for loop to change ONLY the access token and refresh token values in the .env file
    for x in range(2):
        value = lines[x].find('=') # .find() will return first index of the symbol, otherwise -1 if not in string
        a.seek(offset + value + 1) # set the file's current pointer to where we will start overwritting a new value
        a.write(f'\'{new_tokens[x]}\'')
        offset = offset + len(lines[x]) # add the length of the current line to the offset

    a.close()

new_tokens = get_new_refresh_token()
overwrite_tokens(new_tokens)
