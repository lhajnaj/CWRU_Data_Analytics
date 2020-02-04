d3.json("/player2").then(function (response) {
        var data = response;
        // console.log(data)
        var ages = data.map(d => d.age)
        var names = data.map(d => d.player)
        var teams = data.map(d => d.tm)
        // console.log(ages)
        var salary = data.map(d => d.salary_2019to2020)
      
        var height = data.map(d => d.height)
        var ppg = data.map(d => d.pts)
        // console.log(height)
        var position = data.map(d => d.position)
        
        var guards = data.filter(d => d.position.charAt(0) === "G")
        var forwards = data.filter(d => d.position.charAt(0) === "F")
        var centers = data.filter(d => d.position.charAt(0) === "C")
        console.log(forwards)

        var teamSet = new Set(teams);
        
        var positionsByTeam = [];
        teamSet.forEach(function sortTeam(teamName){
                
                
                var guardArray = guards.filter(d => d.tm === teamName);
                var guardSalary = guardArray.map(d => d.salary_2019to2020)
                
                guardsSalarySum = guardSalary.reduce(function(a, b) { return a + b; }, 0);
                
                
                var forwardArray = forwards.filter(d => d.tm === teamName);
                var forwardSalary = forwardArray.map(d => d.salary_2019to2020)
                
                forwardsSalarySum = forwardSalary.reduce(function(a, b) { return a + b; }, 0);
                
                
                var centerArray = centers.filter(d => d.tm === teamName);
                var centerSalary = centerArray.map(d => d.salary_2019to2020)
                
                centersSalarySum = centerSalary.reduce(function(a, b) { return a + b; }, 0);
                

                var teamAxis = {
                        name:teamName,
                        guardSalary:guardsSalarySum,
                        forwardSalary:forwardsSalarySum,
                        centerSalary:forwardsSalarySum

                };
                positionsByTeam.push(teamAxis)
                
                
        });
        console.log(positionsByTeam)
        positionsByTeam.splice(2,2)
        console.log(positionsByTeam)

        var myConfig = {
                type: "bar",
                plot: {
                        stacked: true,
                        stackType: "100%"
                },

                "title": {
                        "text": "Proportion of Team's Salary Spent by Position",
                        "font-color": "black",
                        "backgroundColor": "none",
                        "font-size": "22px",
                        "alpha": 1,
                        "adjust-layout":true,
                        "font-weight": "bold"
                    },

                'scale-x': {
                        label: { /* Scale Title */
                          text: "TEAMS",
                        },
                        labels: positionsByTeam.map(d=> d.name),
                        "items-overlap":true,
                        "max-items":30
                        
                      },

                scaleY: {
                        minValue: 0,
                        maxValue: 100
                },
                series: [
                        {
                                values: positionsByTeam.map(d=> d.guardSalary),
                                text: "Guards"
                        },
                        {
                                values: positionsByTeam.map(d=> d.forwardSalary),
                                text: "Forwards"
                        },
                        {
                                values: positionsByTeam.map(d=> d.centerSalary),
                                text: "Centers"
                        }
                        
                ],


                legend:{
                        borderRadius:"3px",
                        borderColor:"none",
                        backgroundColor:"none",
                        layout:"h",
                        verticalAlign:"bottom",
                        align:"center",
                        shadow:false,
                        marker:{
                          borderRadius:"2px",
                          borderColor:"none"
                        },
                       
                     },

                // tooltip:{
                //         borderRadius:"3px",
                //         borderColor:"#F4F2F2",
                //         borderWidth:2,
                //         width: 90,
                //         callout:true,
                //         height:50,
                //         fontSize: 12,
                //         shadow:false,
                //        text:positionsByTeam.map(d=> d.name),
                //         short: true,
                //         decimals:1,
                //         rules:[
                //            {
                //              rule:"%p === 0 && %i === 3 || %p === 1 && %i === 3",
                //              text: "%kt Projected: $%v in %t Sales",
                //              backgroundColor:"#7d7d7d"
                //            }  
                //         ]
                //      },
        };

        zingchart.render({
                id: 'chart_here',
                data: myConfig,
                height: "100%",
                width: "100%"
        });

});













        // var trace1 = [{
        //         x: ppg,
        //         y: salary,

        //         // type: "scatter",
        //         text: names,
        //         mode: "markers",
        //         marker: {
        //                 size: salary / 1000000,
        //                 // sizeref: .0000001,
        //                 // sizemode: 'area',
        //                 color: salary
        //         },
        //         hovertemplate: '<i>Player:</i> %{text}' +
        //                 '<br><b>PPG</b>: %{x:.2f} Point Per Game<br>' +
        //                 '<b>Salary</b>: $%{y:,}',
        //         hoverinfo: "hello",
        //         name: ""
        // }]
        // var layout = {
        //         title: 'Salary v. Points Per Game',
        //         showlegend: false,
        //         height: 600,
        //         // width: 800,
        //         hovermode: 'closest',
        //         xaxis: {
        //                 title: {
        //                         text: 'Points Per Game',
        //                         font: {
        //                                 family: 'Courier New, monospace',
        //                                 size: 18,
        //                                 color: '#7f7f7f'
        //                         }

        //                 }
        //         },
        //         yaxis: {
        //                 title: {
        //                         text: 'Salary',
        //                         font: {
        //                                 family: 'Courier New, monospace',
        //                                 size: 18,
        //                                 color: '#7f7f7f'
        //                         }

        //                 }
        //         }
        // };

        // Plotly.plot('chart here', trace1, layout);

