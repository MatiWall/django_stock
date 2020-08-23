



function createSeries(data) {
    let series = [];

    let keys = Object.keys(data);
    keys.forEach( key => {
        series.push({name : key, data : data[key]});
    });
    return series;
}