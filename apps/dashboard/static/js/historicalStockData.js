class historicalStockData {

    constructor(data) {
        this.ticker = data.ticker;
        this.container = data.container;
        this.range = data.hasOwnProperty('range') ? data.range : undefined;
        this.url = data.url;

    }


    getData() {

        fetch(this.url, {
            method: 'POST',
            credentials: 'same-origin',
            headers: {
                "X-CSRFToken": Cookies.get("csrftoken"),
                "Accept": "application/json",
                'X-Requested-With': 'XMLHttpRequest'
            },
            body: JSON.stringify({ 'fetchData': 'test' }),
        }).then((res) => res.json())
            .then((data) => {
                
                let chart = this.plotData(data);
                this.addComponent(chart)

            })
            .catch((err) => console.log(err))


    }



    plotOptions(data) {
        // Collect plot options

        let opt = {}
        opt = this.pushObject(this.axisOptions(), opt);
        opt = this.pushObject(this.seriesOptions(data), opt);
        opt = this.pushObject(this.responsiveOptions(), opt);
        opt = this.pushObject(this.tooltipOptions(), opt);

        return opt


    }

    plotData(data) {

        const id = 'dbc' + Math.random().toString(36).substr(2, 9); "dbc = dashboardComponent"

        let divContainer = document.createElement('div');
        divContainer.setAttribute("class", 'dashboardComponentContainer');
        divContainer.setAttribute("id", id);

        let chart = Highcharts.stockChart(divContainer, this.plotOptions(data))

        return divContainer

    }

    addComponent(chart) {

        var dataInputId = Math.random().toString(36).substr(2, 9); // Generate a unigue id (maybe overkill)


        var dashboardComponent = `
        <div class="grid-stack-item" data-gs-disable-drag="true">
            <div id=${dataInputId} class="grid-stack-item-content">
                <div class="widgetButton">
                    <button class="deleteButton" onclick="grid.removeWidget(this.parentNode.parentNode.parentNode)"> &times; </button>
                    <button class="editButton button buttonNeutral"> Edit </button> </br>
                </div>
                
            </div>
        </div>`;


        grid.addWidget(dashboardComponent, { width: 4, height: 5 });
        document.getElementById(dataInputId).appendChild(chart);
    }




    axisOptions() {

        let axisOpt = {
            yAxis: [{
                labels: {
                    align: 'left'
                },
                height: '80%',
                resize: {
                    enabled: true
                }
            }, {
                labels: {
                    align: 'left'
                },
                top: '80%',
                height: '20%',
                offset: 0
            }]
        }

        return axisOpt
    }

    seriesOptions(data) {
        let seriesOpt = {
            series: [{
                type: 'ohlc',
                id: 'aapl-ohlc',
                name: 'AAPL Stock Price',
                data: data.ohlc,
            }, {type: 'column',
            id: 'aapl-volume',
            name: 'AAPL Volume',
            data: data.volume,
            yAxis: 1}
        ]
        }

        return seriesOpt
    }

    responsiveOptions() {
        let responsiveOpt = {
            responsive: {
                rules: [{
                    condition: {
                        maxWidth: 800
                    },
                    chartOptions: {
                        rangeSelector: {
                            inputEnabled: false
                        }
                    }
                }]
            }
        }

        return responsiveOpt
    }

    tooltipOptions() {
        let tooltipOpt = {
            tooltip: {
                shape: 'square',
                headerShape: 'callout',
                borderWidth: 0,
                shadow: false,
                positioner: function (width, height, point) {
                    var chart = this.chart,
                        position;

                    if (point.isHeader) {
                        position = {
                            x: Math.max(
                                // Left side limit
                                chart.plotLeft,
                                Math.min(
                                    point.plotX + chart.plotLeft - width / 2,
                                    // Right side limit
                                    chart.chartWidth - width - chart.marginRight
                                )
                            ),
                            y: point.plotY
                        };
                    } else {
                        position = {
                            x: point.series.chart.plotLeft,
                            y: point.series.yAxis.top - chart.plotTop
                        };
                    }

                    return position;
                }
            }
        }

        return tooltipOpt
    }


    pushObject(object, container){
        
        for (let [key, value] of Object.entries(object)) {
           
            container[key]=value
            
          }

          return container

        }



}



grid.on('gsresizestop', function(event, element) { // Resize highchart charts when widget is resized.
    
    let chartComponent = element.querySelector('.dashboardComponentContainer');
   
    let chart = Highcharts.charts[chartComponent.getAttribute('data-highcharts-chart')];

    //console.log(chart);

    chart.setSize(element.offsetWidth-20, element.scrollHeight-5, true);
  });




