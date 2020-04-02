



// Type options for dashboard component
var typesFieldset = document.getElementById("dashboardTypeFieldset");
typesFieldset.types = ['Quote', 'Historical', 'Intra Day', 'OHCL', 'Largest Trades', 'Previous Days Price', 'Volume by Venue', 'Company Profiles'];

typesFieldset.addEventListener('change', (e) => { // chart type change
    setTimeout(() => {
        console.log('heys');
        //loadSettings();
    }, 1000);

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

        console.log('testtt');

        // Options to picklist


        console.log(picklist.items);
    }
}





fetch("getData/", {
    method: 'POST',
    headers: {
        "X-CSRFToken": Cookies.get('csrftoken'),
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest'
    },
    body: JSON.stringify({ 'This': 'is', 'past': 'data' }),

}).then(function (response) {
    console.log(response);
    return response.json();
}).then(function (data) {
    console.log("Data is ok", data);
}).catch(function (ex) {
    console.log("parsing failed", ex);
});











