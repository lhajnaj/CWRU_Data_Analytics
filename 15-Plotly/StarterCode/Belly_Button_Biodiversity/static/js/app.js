function buildMetadata(sample) {

  // To complete the function that builds the metadata panel, start by using d3.json to pull a sample with the metadata:
  var metaDataRoute = `/metadata/${sample}`;

    // Use d3 to select the panel with id of `#sample-metadata`
    d3.json(metaDataRoute).then(function(sample){
      var sampleMetaData = d3.select(`#sample-metadata`);

    // Use `.html("") to clear any existing metadata
    sampleMetaData.html("");

    // Use `Object.entries` to add each key and value pair to the panel to append
    // tags for each key-value in the metadata.
      Object.entries(sample).forEach(function([key,value]){
        var row = sampleMetaData.append("h6"); row.text(`${key}:${value}`)})});
} 


function buildCharts(sample) {

  // Use d3.json to fetch the sample data for the plots
 var plotSampleData = `/samples/${sample}`;

 // Build a Bubble Chart using the sample data
 d3.json(plotSampleData).then(function(data){
   var x_axis = data.otu_ids;
   var y_axis = data.sample_values;
   var sizes = data.sample_values;
   var colors = data.otu_ids;
   var texts = data.otu_labels;
   var bubbleChart = {
     x: x_axis,
     y: y_axis,
     text: texts,
     mode: `markers`,
     marker: {size: sizes, color: colors}
   };
   
   var dataForGraphics = [bubbleChart];
   var layout = {
     title: "Belly Button Bacteria",
     xaxis: {title: "OTU IDs"}
   };

   Plotly.newPlot("bubble", dataForGraphics, layout);


   // Build a Pie Chart
   d3.json(plotSampleData).then(function(dataForGraphics){
     var value = dataForGraphics.sample_values.slice(0,10);
     var label = dataForGraphics.otu_ids.slice(0,10);
     var display = dataForGraphics.otu_labels.slice(0,10);
     var pie_chart = [{
       values: value,
       labels: label,
       hovertext: display,
       type: "pie"
     }];

     var layout = {height: 400, width: 700};

     Plotly.newPlot('pie',pie_chart,layout);});});
}


function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json("/names").then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}

function optionChanged(newSample) {
  // Fetch new data each time a new sample is selected
  buildCharts(newSample);
  buildMetadata(newSample);
}

// Initialize the dashboard
init();
