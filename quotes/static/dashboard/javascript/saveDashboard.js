

function saveGridstackData() {
    var itemData = [];

    const dashboardCanvas = document.getElementById('dashboardCanvasGridStack');

    const items = dashboardCanvas.querySelectorAll('.grid-stack-item');

    items.forEach(  function( item, index) {

            itemData.push({ 
                'gridId' : index,
                'x' : item.getAttribute('data-gs-x'),
                'y' : item.getAttribute('data-gs-y'),
                'width' : item.getAttribute('data-gs-width'),
                'height' : item.getAttribute('data-gs-height')
                
            });
        }
    )


    console.log(itemData);
    console.log(Date.now());

    fetch('/dashboard/saveDashboard/', {
        method : 'put',
        credentials : 'same-origin',
        headers: {
            "X-CSRFToken": Cookies.get("csrftoken"),
            "Accept": "application/json",
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify({a:1, b:2})
    }).then( (res)=> {console.log(res)})
    .catch( (res)=> {console.log(res)})


}

function loadGridstackData() {
    console.log('Load button pressed');
}