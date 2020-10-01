import requests
import csv
from pprint import pprint

# SLEEP FROM A SPECIFIC TIME PERIOD
def get_sleep(user_id, access_token):
    sleep = requests.get('https://api.fitbit.com/1.2/user/' + user_id + '/sleep/date/2020-08-16/2020-08-31.json', headers={'Authorization': 'Bearer ' + access_token})
    #pprint(sleep.json()['sleep'][0]['duration'])
    if (sleep.status_code != 200):
        print('Error fetching sleep request. Need a new access token')
    else:
        sleep_object = sleep.json()['sleep']
        sleep_length = len(sleep_object)

        actual_minutes_asleep = 0
        sleep_schedule = []
        current_day_index = -1

        for i in range(0, sleep_length):
            # print("Date: " + str(sleep_object[i]['dateOfSleep']) + " | Slept for: " + str(sleep_object[i]['minutesAsleep']) + " minutes")
            date = sleep_object[i]['dateOfSleep']
            actual_minutes_asleep = actual_minutes_asleep + sleep_object[i]['minutesAsleep']
            if i == 0:
                sleep_schedule.append({date: round(actual_minutes_asleep / 60, 2)})
                current_day_index = current_day_index + 1
            elif sleep_object[i]['dateOfSleep'] == sleep_object[(i-1)]['dateOfSleep']:
                sleep_schedule[current_day_index][date] = round(actual_minutes_asleep / 60, 2)
            else:
                actual_minutes_asleep = sleep_object[i]['minutesAsleep']
                sleep_schedule.append({date: round(actual_minutes_asleep / 60, 2)})
                current_day_index = current_day_index + 1

        sleep_schedule.reverse()

        # extract sleep values to new csv file
        with open("./csv/sleep.csv", "w", newline='') as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            for line in sleep_schedule:
                writer.writerow([list(line.keys())[0], list(line.values())[0]])