
$(document).ready(function() {

    
    var value = JSON.parse(document.getElementById('quotes').textContent);

    console.log(typeof value);

    function createTable() {
        
        /*
        var body = document.getElementById('addStockTable');
        var tbl = document.createElement('table');
        var tbdy = document.createElement('tbody');

        tbl.classList.add("table table-striped table-bordered table-hover");

        var tr, td;
        tr = document.createElement('tr');
        for(var i = 1; i<3; i++){
            td = document.createElement('td');
            td.appendChild(document.createTextNode('test'));
            tr.appendChild(td);
        }
        tbdy.appendChild(tr);
        tbl.appendChild(tbdy);
        body.appendChild(tbl);
        */
       var table_body = '<table border="1">';
       for(var i=0;i<3;i++){
         table_body+='<tr>';
         for(var j=0;j<3;j++){
             table_body +='<td>';
             table_body +='Table data';
             table_body +='</td>';
         }
         table_body+='</tr>';
       }
         table_body+='</table>';
        $('#addStockTable').html(table_body);



    }

    createTable();

});




