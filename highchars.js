//Assuming you have obtained the data points from Highcharts as an array
var highchartsDataPoints = Highcharts.charts[0].series[1].points;

// Extract the relevant data from the points array
var extractedData = highchartsDataPoints.map(function(point) {
  return {
    x: point.date,
    y: point.y
  };
});

// Convert the extracted data array to a JSON string
var jsonData = JSON.stringify(extractedData, null, 2); // Adding null, 2 for pretty formatting

// Create a Blob containing the JSON data
var blob = new Blob([jsonData], { type: 'application/json' });

// Create a URL for the Blob
var blobUrl = URL.createObjectURL(blob);

// Create a link element for downloading the file
var downloadLink = document.createElement('a');
downloadLink.href = blobUrl;
downloadLink.download = 'highcharts_data.txt';
downloadLink.textContent = 'Download Highcharts Data';

// Append the link to the page
document.body.appendChild(downloadLink);

// Assuming you have a reference to your Highcharts chart
var highchartsChart = Highcharts.charts[0]; // Adjust the index as needed

//////////////

// Extract the relevant data from the chart series
var extractedData = highchartsChart.series[0].data.map(function(point) {
  return {
    x: point.x,
    y: point.y
  };
});

// Convert the extracted data array to a JSON string
var jsonData = JSON.stringify(extractedData, null, 2); // Adding null, 2 for pretty formatting

// Create a Blob containing the JSON data
var blob = new Blob([jsonData], { type: 'application/json' });

// Create a URL for the Blob
var blobUrl = URL.createObjectURL(blob);

// Create a link element for downloading the file
var downloadLink = document.createElement('a');
downloadLink.href = blobUrl;
downloadLink.download = 'highcharts_data.txt';
downloadLink.textContent = 'Download Highcharts Data';

// Append the link to the page
document.body.appendChild(downloadLink);
