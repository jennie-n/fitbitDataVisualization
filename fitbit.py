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