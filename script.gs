// written by Jennie and Kenneth Nguyen in 2020 :)

// Opening the master sheet manually because this script is standalone
// (not directly attached to a Google spreadsheet)
const spreadSheetID = "1KHqDeSCkyEEZRY4ujwnaGFXOLODLa7unNC2K9v3vZEs";
const sheet = SpreadsheetApp.openById(spreadSheetID);

const headerFormat = {
  "headerRow":1,
  "nextRowColor":"#ffffff",
  "date": {"columnWidth":100, "colNum":1, "name":"Date"},
  "steps": {"columnWidth":115, "colNum":2, "name":"Steps", "reverse":1},
  "sleep": {"columnWidth":100, "colNum":3, "name":"Sleep"},
  "heartrate": {"columnWidth":125, "colNum":4, "name":"Resting Heart Rate"},
  "calories": {"columnWidth":107, "colNum":5, "name":"Calories Burned"},
  "dataStartingRow":2,
  "firstCol":1,
  "lastCol":5
}

// HELPER FUNCTIONS --------------------------------------------------------------------------------------------

// Obtains data from a CSV file in
function getCSVFromGoogleDrive(file) { // add headerFormat as input parameter later
  var file = DriveApp.getFilesByName(file).next();
  var csvData = Utilities.parseCsv(file.getBlob().getDataAsString());
  // Logger.log(csvData); // for testing purposes
  return csvData;
}

// Prints data to columns in spreadsheet
function addData(csvData, column) {
  for(i=headerFormat["dataStartingRow"]; i<csvData.length+headerFormat["dataStartingRow"]; i++){
    sheet.getActiveSheet().getRange(i,column).setValue(csvData[i-headerFormat["dataStartingRow"]][1]);
  }
}

// IMPORTANT FUNCTIONS ------------------------------------------------------------------------------------------

// Updates data on an already made spreadsheet
// This is the function you most likely need to run.
function updateGoogleSpreadsheet(){
  const stepsFile = "steps.csv";
  const sleepFile = "sleep.csv";
  const heartrateFile = "heartrate.csv";
  const caloriesFile = "calories.csv";

  addData( getCSVFromGoogleDrive(stepsFile), headerFormat["steps"]["colNum"] );
  addData( getCSVFromGoogleDrive(sleepFile), headerFormat["sleep"]["colNum"] );
  addData( getCSVFromGoogleDrive(heartrateFile), headerFormat["heartrate"]["colNum"] );
  addData( getCSVFromGoogleDrive(caloriesFile), headerFormat["calories"]["colNum"] );
}

// Creates a new Google spreadsheet with data
function createGoogleSpreadsheet(){

}