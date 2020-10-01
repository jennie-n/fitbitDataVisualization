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

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
AUTH = os.getenv('AUTH')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
USER_ID = os.getenv('USER_ID')

# -------------------------------------------------------------------------------------------------------------------------------

# Get user profile data
# activity_request1 = requests.get('https://api.fitbit.com/1/user/-/profile.json', headers={'Authorization': 'Bearer ' + ACCESS_TOKEN})
# print(activity_request1)

get_steps(USER_ID, ACCESS_TOKEN)

get_heartrate(USER_ID, ACCESS_TOKEN)

get_sleep(USER_ID, ACCESS_TOKEN)

get_calories(USER_ID, ACCESS_TOKEN)