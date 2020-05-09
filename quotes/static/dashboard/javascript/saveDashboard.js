

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


}