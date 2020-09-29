// written by Jennie and Kenneth Nguyen in 2020 :)

// Opening the master sheet manually because this script is standalone
// (not directly attached to a Google spreadsheet)
const spreadSheetID = "1KHqDeSCkyEEZRY4ujwnaGFXOLODLa7unNC2K9v3vZEs";
const sheet = SpreadsheetApp.openById(spreadSheetID);

const headerFormat = {
  "headerRow":1,
  "nextRowColor":"#ffffff",
  "date": {"columnWidth":100, "colNum":1, "name":"Date"},
  "steps": {"columnWidth":115, "colNum":2, "name":"Steps Taken"},
  "sleep": {"columnWidth":100, "colNum":3, "name":"Hours of Sleep"},
  "heartrate": {"columnWidth":125, "colNum":4, "name":"Resting Heart Rate"},
  "calories": {"columnWidth":107, "colNum":5, "name":"Calories Burned"},
  "dataStartingRow":2,
  "firstCol":1,
  "lastCol":5
}

// HELPER FUNCTIONS --------------------------------------------------------------------------------------------

// Prints dates to spreadsheet
function addDates(csvData, column){
  for(i=headerFormat["dataStartingRow"]; i<csvData.length+headerFormat["dataStartingRow"]; i++){
    sheet.getActiveSheet().getRange(i,column).setValue(csvData[i-headerFormat["dataStartingRow"]][0]);
    Logger.log(csvData[i-headerFormat["dataStartingRow"]][0]);
  }
}

// Obtains health data from a CSV file in 
function getCSVFromGoogleDrive(file) { // add headerFormat as input parameter later
  var file = DriveApp.getFilesByName(file).next();
  var csvData = Utilities.parseCsv(file.getBlob().getDataAsString());
  // Logger.log(csvData); // for testing purposes
  return csvData;
}

// Prints health data to columns in spreadsheet
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
  
  addDates(getCSVFromGoogleDrive(stepsFile), headerFormat["date"]["colNum"]);
  
  addData( getCSVFromGoogleDrive(stepsFile), headerFormat["steps"]["colNum"] );
  addData( getCSVFromGoogleDrive(sleepFile), headerFormat["sleep"]["colNum"] );
  addData( getCSVFromGoogleDrive(heartrateFile), headerFormat["heartrate"]["colNum"] );
  addData( getCSVFromGoogleDrive(caloriesFile), headerFormat["calories"]["colNum"] );
  makeCumulativeChart();
}

// Creates a new Google spreadsheet with data
function createGoogleSpreadsheet(){
  
}

// Produces a chart with all health data information in spreadsheet
function makeCumulativeChart() {
  var headerRow = sheet.getRange("B1:E1").getValues();
  Logger.log(headerRow); // for testing purposes
  var cumulativeChart = sheet.getActiveSheet().newChart().asLineChart()
  .addRange(sheet.getRange("A1:E17"))
  .setTitle('Health Information by Date')
  .setXAxisTitle('Date')
  .setPosition(3, 7, 0, 0)
  .setOption('series', 
     {0:{labelInLegend:headerRow[0][0]},
      1:{labelInLegend:headerRow[0][1]},
      2:{labelInLegend:headerRow[0][2]},
      3:{labelInLegend:headerRow[0][3]}})
  .build();

   sheet.getActiveSheet().insertChart(cumulativeChart);
}

// Produces "Steps Taken vs. Hours of Sleep" chart
function makeStepsSleepChart() {
  var stepsSleepChart = sheet.getActiveSheet().newChart().asScatterChart()
  .addRange(sheet.getRange("C1:C17"))
  .addRange(sheet.getRange("B1:B17"))
  .setTitle('Steps Taken vs. Hours of Sleep')
  .setXAxisTitle('Hours of Sleep')
  .setOption('vAxes.0.title', 'Steps Taken') // set y axis
  .setPosition(22, 7, 0, 0)
  .setOption("trendlines", {0: {type: "linear"}})
  .build();

   sheet.getActiveSheet().insertChart(stepsSleepChart);
}