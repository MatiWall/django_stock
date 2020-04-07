
// Toggle Button 

var grid = GridStack.init();

function addComponent() {

    var dataInputId = Math.random().toString(36).substr(2, 9); // Generate a unigue id (maybe overkill)

    dashboardComponent = `
            <div class="grid-stack-item dashboardComponents" data-gs-disable-drag="true">
                <div id=${dataInputId} class="grid-stack-item-content">
                    <button class="deleteButton" onclick="grid.removeWidget(this.parentNode.parentNode)"> &times; </button>
                    <button class="editButton"> Edit </button>
                </div>
            </div>`;


    grid.addWidget(dashboardComponent, { width: 4, height: 5 });
    var chart = document.createElement('highchart-timeseries');
    document.getElementById(dataInputId).appendChild(chart);


}





document.getElementById('edit_tgl').addEventListener('click', (e) => {
    let dashboardCanvas = document.getElementById('dashboardCanvasGridStack'); 

    if (e.target.checked) {

        grid.movable('.grid-stack-item', false);
        grid.resizable('.grid-stack-item', false);
        updateWidgetVisibility(dashboardCanvas, 'hidden'); 

    } else {

        grid.movable('.grid-stack-item', true);
        grid.resizable('.grid-stack-item', true);
        updateWidgetVisibility(dashboardCanvas, 'visible');

    }

})

function updateWidgetVisibility(canvas, visibility) {
    let deleteButtonNodes = canvas.querySelectorAll('.deleteButton');
    let editButtonNodes = canvas.querySelectorAll('.editButton');

    for(var i = 0; i<deleteButtonNodes.length; i++) {
        deleteButtonNodes[i].style.visibility = visibility;
        editButtonNodes[i].style.visibility = visibility;
    }

    

}


// Add/Edit Dashboard Widget

const endPointsIEX = { 'Quote': 'quote', 'Historical': 'chart', 'Intra Day Prices': 'intraday-prices', 'OHCL': 'ohcl', 'Largest Trades': 'largest-trades', 'Previous Days Price': 'previous', 'Volume by Venue': 'volume-by-venue', 'Company Profiles': 'company' };


// Type options for dashboard component
var typesFieldset = document.getElementById("dashboardTypeFieldset");
typesFieldset.types = Object.keys(endPointsIEX);
typesFieldset.addEventListener('change', (e) => { // chart type change

    loadSettings();

});



// Ticker Input


let tickerInput = document.getElementById('dashboardComponentTickers');
tickerInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        console.log('Enter Was Pressed');

        loadSettings();


    }
})






function loadSettings() {
    const type = typesFieldset.selected;
    console.log(type);

    var panel = document.getElementById("dashboardSettings");

    if (type === 'Quote') {
        let picklist = document.createElement("dual-picklist");
        picklist.setAttribute('title', 'Choose Values');
        panel.appendChild(picklist);
        picklist.items = ['1', '2', '3', '4', '5', '6', '7'];

        console.log(picklist.items);
    } else if (type === 'Historical') {
        var textnode = document.createTextNode("Nothing here yet")
        panel.appendChild(textnode);
    }
}







function getIEXData(ticker, type, isSandbox = true) {

    var baseURL;
    var token;
    var endpointPath;



    const requestBaseIifoOptions = {
        'standard': { 'baseURL': 'https://cloud.iexapis.com/stable/', 'token': 'pk_1fabca50feb84a8a960fda5d63eeab29' },
        'sandbox': { 'baseURL': 'https://sandbox.iexapis.com/stable/', 'token': 'Tpk_1d9ebd084c5149d79631fa7cbf811a8e' }
    }


    const requestBaseInfo = !isSandbox ? requestBaseIifoOptions.standard : requestBaseIifoOptions.sandbox;
    console.log(requestBaseInfo);

    if (ticker.indexOf(',') === -1 && type.indexOf(',') === -1) {// Setting URL for batch or single stock request
        endpointPath = 'stock/' + ticker + '/' + type + '?token=';

    } else {
        endpointPath = 'stock/market/batch?symbols=' + ticker + ',&types=' + type + '&token=';
    }


    const url = requestBaseInfo.baseURL + endpointPath + requestBaseInfo.token;
    console.log(url);
    fetch(url).then((response) => {
        errorHandeling(response)
        return response.json();
    })
        .then((stockData) => {
            //console.log(data);
            console.log(stockData);
        });



}

function errorHandeling(response) {
    if (response.status.toString()[0] !== '2') {

        alert('Error: ' + response.status + ' - ' + response.statusText);
        console.log(response);
    }


}



getIEXData('aapl', 'chart,quote');






