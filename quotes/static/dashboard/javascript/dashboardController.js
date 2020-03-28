


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


var list = document.querySelector("dual-picklist");
list.items = ['1', '2', '3', '4', '5', '6'];
console.log(list.chosenItems);









