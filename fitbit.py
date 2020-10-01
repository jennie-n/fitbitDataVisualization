import requests
import time
import oauth2 as oauth2
from pprint import pprint
import json
import csv
from dotenv import load_dotenv

load_dotenv()
import os

from steps import get_steps, get_steps_today
from heartrate import get_heartrate
from sleep import get_sleep
from calories import get_calories

access_token = os.getenv('ACCESS_TOKEN')
auth = os.getenv('AUTH')
refresh_token = os.getenv('REFRESH_TOKEN')
user_id = os.getenv('USER_ID')

# -------------------------------------------------------------------------------------------------------------------------------

# Get user profile data
# activity_request1 = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers={'Authorization': 'Bearer ' + access_token})
# print(activity_request1)

# get_steps(user_id, access_token)

# get_heartrate(user_id, access_token)

# get_sleep(user_id, access_token)

# get_calories(user_id, access_token)

# -------------------------------------------------------------------------------------------------------------------------------

def create_refresh_token():
    a = open('test',  'r+')
    lines = a.readlines() # read all the lines from the file into an array
    offset = 0 # used to keep track of the offset for overwriting new .env values

    for line in lines:
        value = line.find('=') # .find() will return first index of the symbol, otherwise -1 if not in string
        a.seek(offset + value + 1) # set the file's current pointer to where we will start overwritting a new value
        a.write('\'New Token\'')
        # TODO: the value of write should be the new access token / refresh token. possibly truncate new .env file for
        # those two variables alone since much more sensitive or change range in this loop
        offset = offset + len(line) # add the length of the current line to the offset

    a.close()