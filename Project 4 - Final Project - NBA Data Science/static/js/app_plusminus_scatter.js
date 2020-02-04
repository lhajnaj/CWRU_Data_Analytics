d3.json("/player2").then(function (response) {
        var data = response;
        // console.log(data)
        var ages = data.map(d => d.age)
        var names = data.map(d => d.player)
        var teams = data.map(d => d.tm)
        // console.log(ages)
        var salary = data.map(d => d.salary_2019to2020)
        var height = data.map(d => d.height)
        var plusMinus = data.map(d => d.plusminus)
        // console.log(height)

        var trace1 = [{
                x: plusMinus,
                y: salary,

                // type: "scatter",
                text: names,
                mode: "markers",
                marker: {
                        size: salary / 1000000,
                        // sizeref: .0000001,
                        // sizemode: 'area',
                        color: salary
                },
                hovertemplate: '<i>Player:</i> %{text}' +
                        '<br><b>Plus/Minus</b>: %{x:.2f} impact on Team Score<br>' +
                        '<b>Salary</b>: $%{y:,}',
                hoverinfo: "hello",
                name: ""
        }]
        var layout = {
                title: 'Salary v. Plus/Minus of Each Player',
                showlegend: false,
                height: 600,
                // width: 800,
                hovermode: 'closest',
                xaxis: {
                        title: {
                                text: 'Plus/Minus',
                                font: {
                                        family: 'Courier New, monospace',
                                        size: 18,
                                        color: '#7f7f7f'
                                }

                        }
                },
                yaxis: {
                        title: {
                                text: 'Salary',
                                font: {
                                        family: 'Courier New, monospace',
                                        size: 18,
                                        color: '#7f7f7f'
                                }

                        }
                }
        };

        Plotly.plot('chart here', trace1, layout);
});
