// from data.js
var tableData = data;



// Select the table's body
var tableBody = d3.select("tbody");
var filter = 0;
sightings = data

data.forEach((instance) => {
	var tableRow = tableBody.append("tr");
	Object.entries(instance).forEach(([key, value]) => {
		var tableCell = tableBody.append("td");
		tableCell.text(value);
	}); });



// Filter button
var submitButton = d3.select("#filter-btn");

submitButton.on("click", function () {

	// Disable refreshing
	d3.event.preventDefault();

	// Allow only datetime as the input
	var dateTimeInput = d3.select("#datetime");

	// Collect the searched value
	var value = dateTimeInput.property("value");
    var filteredData = sightings.filter(ufoSearch => ufoSearch.datetime === value);
	buildTable(filteredData); });



// MAke the filter search operational
function buildTable(filter) {

	tableBody.html("");
	filter.forEach((instance) => {
		var tableRow = tableBody.append("tr");
		Object.entries(instance).forEach(([key, value]) => {
			var tableCell = tableBody.append("td");
			tableCell.text(value); }); }); }
