

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



    fetch('/dashboard/saveDashboard/', {
        method : 'PUT',
        credentials : 'same-origin',
        headers: {
            "X-CSRFToken": Cookies.get("csrftoken"),
            "Accept": "application/json",
            'X-Requested-With': 'XMLHttpRequest'
        },
        body: JSON.stringify(itemData),
    }).then( (res)=> {console.log(res)})
    .catch( (res)=> {console.log(res)})


}

function loadGridstackData() {
    
    fetch('/dashboard/loadDashboard/').then( (res) => res.json()).then(data => console.log(data))
    .catch( (res)=> {console.log('catch')})
    
    /*
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/dashboard/loadDashboard/');
    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log(xhr.responseText);
        }
        else {
            console.log('request failed' + xhr.status);
        }
    }
    xhr.send();
    */
    console.log('Load button pressed');
}