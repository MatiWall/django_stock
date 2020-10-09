async function postForm(url, formId, method = 'post') {
    
    let formData = getFormData(formId);
    

    let res = await ajaxRequest (url, method =  method,  data = formData)
   
    return res;

}



function getFormData(formId) {
    const form = document.getElementById(formId);

 

    let formData = {};
    for(var i=0; i<form.length; i++) {
    
        formData[form[i].name] = form[i].value;
    }
  
    
    return formData;

}




function ajaxRequest (url, method = 'get',  data = null){

    var input = {};

    input.method = method.toLowerCase();

    if(input.method !== 'get'){
        input.headers =  {
            "X-CSRFToken": Cookies.get("csrftoken"),
            "Accept": "application/json",
        "Content-Type": "application/json"};
       
        input.credentials =  "same-origin";

        input.body = JSON.stringify(data);
    }


   
    
    return fetch(url, input);
}


