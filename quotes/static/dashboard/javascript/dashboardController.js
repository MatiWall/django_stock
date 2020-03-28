


//var tickerInput = document.getElementById("dashboardComponentTickers");


let buttons = document.querySelectorAll('input');
buttons.forEach((btn) => {

    if (btn.id == dashboardComponentTickers) {
        btn.addEventListener("keyup", (event) => {
            if (event.keyCode === 13) { // Ticker read when pressing enter
                event.preventDefault();
                var ticker = tickerInput.value;
                alert(event.target);
            }
        })

    } else {
        btn.addEventListener("onclick", (event) => {
            alert(event.target);


        })
    }
});


// Type options for dashboard component
var typesFieldset = document.getElementById("dashboardTypeFieldset");
 typesFieldset.types = ['Quote', 'Chart1', 'Chart2', 'osv'];

    // Keep track of which option is chosen 
 //var typeSettingFill = document.getElementById('dashboardComponentType');
 //typeSettingFill.innerHTML = '<p>This is a trest</p>';



// Options to picklist
var list = document.getElementById("settingsDualPicklist");
list.items = ['1', '2', '3', '4', '5', '6'];
console.log(list.chosenItems);













