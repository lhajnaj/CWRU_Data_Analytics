// from table_data.js
// var tableData = data;

// get table references

// {"pk":0,"rk":1.0,"player":"Stephen Curry","tm":"GSW","salary_2019to2020":40231758,"salary_2020to2021":"$43,006,362 ","salary_2021to2022":"$45,780,966 ","salary_2022to2023":null,"salary_2023to2024":null,"salary_2024to2025":null,"signed_using":"Bird Rights","guaranteed":"$129,019,086 ","year_start":2010,"position":"G","height":6.25,"weight":190.0,"birth_date":574300800000,"college":"Davidson College","age":31,"gp":69,"w":52,"l":17,"min":33.8,"pts":27.3,"fgm":9.2,"fga":19.4,"fg_prc":47.2,"three_pnt_m":5.1,"three_pnt_a":11.7,"three_pnt_prc":43.7,"ftm":3.8,"fta":4.2,"ft_prc":91.6,"oreb":0.7,"dreb":4.7,"reb":5.3,"ast":5.2,"tov":2.8,"stl":1.3,"blk":0.4,"plusminus":10.0},

var data

function buildTable(data) {
    
    // First: clear any existing data
    var tbody = d3.select("tbody");
    tbody.html("");
    
    // Next, Loop through each object in the data
    // append a row and cells for each value in the row
    data.forEach((dataRow) => {
        // append row to table body
        var row = tbody.append("tr");
        
        // loop through each field in the dataRow and add
        // each value as a table cell (td)
        Object.values(dataRow).forEach((val) => {
            var cell = row.append("td");
            cell.text(val);
            }
            );
    });
};

function handleClick() {
    
    // grab the player name value from the filter
    var name = d3.select("#name").property("value");
    let filteredData = window.data;
    
    // check to see if a date was entered and filter the 
    // data using that date
    if (name) {
        // apply `filter` to the table data to only keep the
        // rows where the `name` value matches the filter value
        filteredData = filteredData.filter(d => d.player === name);
    }

    // rebuild the table using filtered data
    buildTable(filteredData);
    
}

// Attach an event to listen for the form button
// window.data is available to anyone who wants it and can grab it from wherever 
d3.selectAll("#filter-btn").on("click", handleClick);

// build the table when the page loads

        d3.json("/player2").then (function(data){
            
            window.data = data.map(function(d){return {"rk":d.rk, "player":d.player, "tm":d.tm, "salary_2019to2020":d.salary_2019to2020, "height":d.height, "age":d.age, "gp":d.gp, "min":d.min,"pts":d.pts,"fgm":d.fgm,"fga":d.fgm,"fg_prc":d.fg_prc,"three_pnt_m":d.three_pnt_m,"three_pnt_a":d.three_pnt_a,"three_pnt_prc":d.three_pnt_prc,"ftm":d.ftm,"fta":d.fta,"ft_prc":d.fta,"oreb":d.oreb,"dreb":d.dreb,"reb":d.reb,"ast":d.ast,"tov":d.tov,"stl":d.stl,"blk":d.blk,"plusminus":d.plusminus}});

            buildTable(window.data);
        });