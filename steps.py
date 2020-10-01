import requests
import csv
from pprint import pprint

# STEPS FOR TODAY'S DATE, IF APPLICABLE
def get_steps_today(user_id, access_token):
    # STEPS ON THIS DAY
    activity_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/steps/date/2020-09-12/2020-09-12.json', 
                                    headers={'Authorization': 'Bearer ' + access_token})
    # print(activity_request.status_code)
    # pprint(activity_request.json()) # print out the json response of the fetched data
    # pprint(activity_request.json()['activities-steps']) # print out more specific part of the response

# STEPS FROM A SPECIFIC TIME PERIOD
def get_steps(user_id, access_token):
    steps = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/steps/date/2020-08-16/2020-08-31.json', headers={'Authorization': 'Bearer ' + access_token})
    if (steps.status_code != 200):
        print('Error fetching steps request. Need a new access token')
    else:
        # pprint(steps.json())
        # pprint(steps.json()['activities-steps'])
        data = steps.json()['activities-steps']

        # extract steps values to new csv file
        with open("./csv/steps.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in data:
                # print(line['value'])
                writer.writerow(line.values())