var table = document.querySelector('.data-table');
var rows = table.querySelectorAll('.data-table-row');
var scrapedData = [];

rows.forEach(function(row) {
    var rowData = {};
    var cells = row.querySelectorAll('.data-table-row-cell');

    cells.forEach(function(cell) {
        var dataType = cell.getAttribute('data-type');
        var cellValue = cell.textContent.trim();

        if (dataType === 'name') {
            var full = cell.querySelector('[data-type="full"]').textContent.trim();
            var abbreviation = cell.querySelector('[data-type="abbreviation"]').textContent.trim();
            rowData['Name'] = full;
            rowData['Abbreviation'] = abbreviation;
        } else {
            rowData[dataType] = cellValue;
        }
    });

    scrapedData.push(rowData);
});

console.log(scrapedData);
