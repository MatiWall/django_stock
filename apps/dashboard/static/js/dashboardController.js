







// add component




let editModeButton = document.getElementById('edit_tgl');
editModeButton.checked = false;

editModeButton.addEventListener('click', (e) => {
    let dashboardContainer = document.getElementById('dashboardCanvas'); 
    
    if (e.target.checked) {

        grid.movable('.grid-stack-item', true);
        grid.resizable('.grid-stack-item', true);
        updateDashboardVisibility(dashboardContainer, 'block'); 

    } else {

        grid.movable('.grid-stack-item', false);
        grid.resizable('.grid-stack-item', false);
        updateDashboardVisibility(dashboardContainer, 'none');

    }

})


function updateDashboardVisibility(dashboardContainer, visibility) {
    let widgetButtonNodes = dashboardContainer.querySelectorAll('.widgetButton');

    for(var i = 0; i<widgetButtonNodes.length; i++) {
        widgetButtonNodes[i].style.display = visibility;

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
    panel.innerHTML = ''; // Remove childNodes
    console.log(panel.hasChildNodes());
    if (type === 'Quote') {
        let picklist = document.createElement("dual-picklist");
        picklist.setAttribute('title', 'Choose Values');
        panel.appendChild(picklist);
        picklist.items = ['1', '2', '3', '4', '5', '6', '7'];

        console.log(picklist.items);
    } else if (type === 'Historical') {
        
    }
}














