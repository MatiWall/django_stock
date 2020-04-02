


  
$(document).ready(function() {
    var data = JSON.parse(document.getElementById('quotes').textContent);
        
     
    var keys = Object.keys(data);
    var type_values = Object.values(data);

    var types = Object.keys(type_values);
    var values = type_values[types[0]]

    createQuoteTable(keys, types, values, '#addStockTable');
    
    createChoiseList(['latestPrice', 'previousClose', 'marketCap'], "#addTickerTable");
    
});




function createQuoteTable(keys, types, values, divId) {
    
    

    var items = ['latestPrice', 'previousClose', 'marketCap'];


    var table_body = '<table class="tableDark">';

    
    
    table_body += '<thead class="theadDark"> <tr>'
    for(var i = 0; i< items.length; i++){
     table_body += '<th>' +items[i]+'</th>'
    }
    table_body += '<tr/> </thead> <tbody class="tbodyLight">'

    var key;
    for(var i=0;i< keys.length;i++){
     key = keys[i];
      table_body+='<tr>';
      for(var j=0;j<3;j++){

         
          table_body +='<td>';
          table_body +=values[items[j]];
          table_body +='</td>';
      }
      table_body+='</tr>';
    }
      table_body+='</tbody> </table>';
     $(divId).html(table_body);



 }


 function createChoiseList(items, containerId) {

    var table_body = '<table>';

    for(var i = 0; i< 5; i++){
     table_body += '<tr> <td><input type="checkbox" /></td> <td>' +i
     +'</td></tr>'
    }
    table_body+='</table>';
    $(containerId).html(table_body);


}

