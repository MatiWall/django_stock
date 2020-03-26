


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


/*
tickerInput.addEventListener("keyup",  (event) => {
    if (event.keyCode === 13) { // Ticker read when pressing enter
        event.preventDefault();
        var ticker = tickerInput.value;

    }

    console.log(ticker);

});
*/







