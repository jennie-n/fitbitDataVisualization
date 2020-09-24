import requests
import csv
from pprint import pprint

# HEART RATE ON THIS DAY
def get_heartrate(user_id, access_token):
    heart_rate_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/heart/date/2020-09-01/1d/1min/time/09:00/22:00.json',
                                     headers={'Authorization': 'Bearer ' + access_token})
    # print(heart_rate_request.status_code)

    # pprint(heart_rate_request.json()['activities-heart-intraday']['dataset'])
    data = heart_rate_request.json()['activities-heart-intraday']['dataset']

    # extract heart rate values to new csv file
    with open("./csv/heartrate.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            # print(line['value'])
            writer.writerow(line.values())