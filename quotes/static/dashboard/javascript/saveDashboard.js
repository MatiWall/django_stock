
// File -> Save AS

function dashboardSaveAs() {
    



}








//---------------

function saveGridstackData() {
    
    const charts = Highcharts.charts; // list of all High
    ItemchartUserOptions = {};
    charts.forEach(function (chart, index) {
        userOptions = chart.userOptions;

        //console.log(chart.renderTo.id)
        ItemchartUserOptions[chart.renderTo.id] = userOptions;

    })
  


    
    var itemData = [];
    const dashboardCanvas = document.getElementById('dashboardCanvasGridStack');
    const items = dashboardCanvas.querySelectorAll('.grid-stack-item');


    items.forEach(  function( item, index) {
           // console.log(item.getElementsByClassName('dashboardComponentContainer')[0].id);
           
            const chartContainerId = item.getElementsByClassName('dashboardComponentContainer')[0].id;
            itemData.push({ 
                'gridId' : index,
                'x' : item.getAttribute('data-gs-x'),
                'y' : item.getAttribute('data-gs-y'),
                'width' : item.getAttribute('data-gs-width'),
                'height' : item.getAttribute('data-gs-height'),
                'userOptions' : ItemchartUserOptions[chartContainerId],
                
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
    
    fetch('/dashboard/loadDashboard/').then( (res) => res.json())
    .then(data => {console.log(data);})
    .catch( (res)=> {console.log('catch')})
    
  
    



   fetch('/dashboard/loadDashboard/', {
    method : 'POST',
    credentials : 'same-origin',
    headers: {
        "X-CSRFToken": Cookies.get("csrftoken"),
        "Accept": "application/json",
        'X-Requested-With': 'XMLHttpRequest'
    },
    body: JSON.stringify('Name Test7'),
    }).then( (res)=> res.json())
    .then( (data) => {
        console.log(data.positions[0].userOptions);
        grid.removeAll();
        data.positions.forEach( function(node) {
            grid.addWidget(`
            <div class="grid-stack-item dashboardComponents" data-gs-disable-drag="true">
                <div class="grid-stack-item-content">
                    <div class="widgetButton">
                        <button class="deleteButton" onclick="grid.removeWidget(this.parentNode.parentNode.parentNode)"> &times; </button>
                        <button class="editButton button buttonNeutral"> Edit </button> </br>
                    </div>
                    
                </div>
            </div>`, node);
        })
        grid.commit();
    })
    .catch( (res)=> {console.log(res)})


  
}



