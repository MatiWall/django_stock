async function list(url, wrapperId) {

    // Use sublevel dropdowns to show data

    var wrapper = document.getElementById(wrapperId);

    const response = await fetch(url);
    const data = await response.json();


    wrapper.innerHTML = '';

    for (var i in data) {
        listItem(wrapper, data[i]);
    }


}


function listItem(container, data ) {
    const id = data.id;
    const name = data.name;
    const selected = data.selected;


    var li = document.createElement('li');
    var checkbox = document.createElement('input');
    checkbox.type = "checkbox";
    checkbox.name =  id;
    checkbox.value = name;
    checkbox.id =  id;
    checkbox.checked = selected;
 
   

    var label = document.createElement('label');
    label.htmlFor = checkbox.id;
    label.appendChild(document.createTextNode(name));
    
    li.appendChild(checkbox)
    li.appendChild(label);
    
    container.appendChild(li);

}



$('#portfolio-filter-form').change(function(event){

  
});









