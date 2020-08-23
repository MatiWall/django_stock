
let highchartInitTimeSeries = (series) => {


Highcharts.chart('categoryAggregatedAmount', {
    chart: {
        type: 'spline'
      },
    title: {
        text: 'Aggregated amount'
    },
    xAxis: {
        type: 'datetime',
    },
    yAxis: {
        title: {
            text: 'dkk'
        }
    },
    
    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },
    
    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
        }
    },
    
    series: series,
    
    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }
    
    });
}




let highchartInitPieChart = (data) => {
    Highcharts.chart('categoriesPercentSummary', {
        chart: {
            plotBackgroundColor: null,
            plotBorderWidth: null,
            plotShadow: false,
            type: 'pie'
        },
        title: {
            text: 'tesssst'
        },
        accessibility: {
            point: {
                valueSuffix: '%'
            }
        },
        plotOptions: {
            pie: {
                allowPointSelect: true,
                cursor: 'pointer',
                dataLabels: {
                    enabled: true,
                    distance: -50,
                    filter: {
                        property: 'percentage',
                        operator: '>',
                        value: 4
                    }
                }
            }
        },
        series: [{
            name: 'Share',
            data: data
        }]
    });
} 