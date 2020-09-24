# Fitbit Data Visualization
## About
Fitbit Data Visualization is a program that extracts data from the Fitbit API into Google Spreadsheets to create user-friendly, visually appealing charts. Now your stats can be easily shared with anyone you know!

Python is used to automate the data extraction from the Fitbit Web API. The result of this automation process are 4 CSV files with health information (steps taken, hours of sleep, resting heart rate, and calories burned) in chronological order by date. The Google Apps Script API utilizes javascript and is used to organize data into Google Spreadsheets.

## Built With
### Languages
- Python
- Javascript

### APIs
- Google Apps Script
- Fitbit Web

## To Do
- Merge the health information in 4 separate CSV files produced into 1 CSV file
- Add error checking for dates with missing stats (aka dates on which the fitbit was not worn or the data has not been uploaded)
- Add permissions functionality: The script can access the user's list of emails to share with in a Google doc or spreadsheet, instead of manually sharing to each email

# Contributors
- [Kenneth Nguyen](https://github.com/KennethNguyen) - Creator
- [Jennie Nguyen](https://github.com/jennie-n) - Creator