import requests
import csv
from pprint import pprint

# CALORIES BURNED FROM A SPECIFIC TIME PERIOD
def get_calories(user_id, access_token):
    calories = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/tracker/calories/date/2020-08-16/2020-08-31.json',
                            headers={'Authorization': 'Bearer ' + access_token})
    if (calories.status_code == 401):
        print('Error')
    else:
        print('Success')
        # pprint(calories.json()) # print out the json response of the fetched data
        # pprint(calories.json()['activities-tracker-calories']) # print out more specific part of the response
        data = calories.json()['activities-tracker-calories']

        # extract calories values to new csv file
        with open("./csv/calories.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in data:
                # print(line['value'])
                writer.writerow(line.values())