var highchartsDataPoints = Highcharts.charts[0].series[1].points;

var extractedData = highchartsDataPoints.map(function(point) {
  return {
    x: point.date,
    y: point.y
  };
});

var jsonData = JSON.stringify(extractedData, null, 2);

var blob = new Blob([jsonData], { type: 'application/json' });

var blobUrl = URL.createObjectURL(blob);

var downloadLink = document.createElement('a');
downloadLink.href = blobUrl;
downloadLink.download = 'highcharts_data.txt';
downloadLink.textContent = 'Download Highcharts Data';

document.body.appendChild(downloadLink);

var highchartsChart = Highcharts.charts[0];

var extractedData = highchartsChart.series[0].data.map(function(point) {
  return {
    x: point.x,
    y: point.y
  };
});


var jsonData = JSON.stringify(extractedData, null, 2);

var blob = new Blob([jsonData], { type: 'application/json' });

var blobUrl = URL.createObjectURL(blob);

var downloadLink = document.createElement('a');
downloadLink.href = blobUrl;
downloadLink.download = 'highcharts_data.txt';
downloadLink.textContent = 'Download Highcharts Data';

document.body.appendChild(downloadLink);
