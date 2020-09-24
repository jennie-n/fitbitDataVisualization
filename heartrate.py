import requests
import csv
from pprint import pprint

# HEART RATE ON THIS DAY
def get_heartrate(user_id, access_token):
    heart_rate_request = requests.get('https://api.fitbit.com/1/user/' + user_id + '/activities/heart/date/2020-08-16/2020-08-31.json',
                                     headers={'Authorization': 'Bearer ' + access_token})
    # print(heart_rate_request.status_code)

    # pprint(heart_rate_request.json()['activities-heart'])
    data = heart_rate_request.json()['activities-heart']
    # d = data[0]
    # print(d['dateTime'])
    # print(d['value']['restingHeartRate'])

    # extract heart rate values to new csv file
    with open("./csv/heartrate.csv", "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            # print(line['value']['restingHeartRate'])
            writer.writerow([line['dateTime'], line['value']['restingHeartRate']])