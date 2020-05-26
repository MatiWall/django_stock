

class myFieldset extends HTMLElement {
    constructor() {
        super();



        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `

        <style>
        
        
        legend {
            width: auto;
            margin-left: auto;
            margin-right: auto;
        }
        
        legend ~ input[type=radio] {
            position: absolute;
            left: -10000px;
          }
          
        
        label {
            border: solid;
            border-width: 1px;
            border-radius: 3px;
            border-color: lightgrey;
            background-color: white;
        }
          
        label:hover {
            cursor: pointer;
            background-color: lightgrey;
        }
        
        
        input[type=radio]:checked + label {
            background-color: rgba(200,200,200, 0.4);
          }
        
        </style>
        
        
        <fieldset id="dashboardComponentChoseType">
            <legend></legend>
           
        </fieldset>
        
        `;

        this._types = [];
        this._selected = "";



        this.changeEvent = new CustomEvent("change", {
            bubbles: true,
            cancelable: false,
            composed: true
          });

    }

    

    get selected() {
        return this._selected;
    }

   set selected(value) {
        this._selected = value
   }

   get types () {
       return this._types;
   }

   set types (values) {
       this._types = values;
       this._createList();
   }

    


 
    connectedCallback() {

      
        this.shadowRoot.getElementById('dashboardComponentChoseType').addEventListener('change', this._ifSelected)
        

      
    }


    disconnectedCallback() {
        this.shadowRoot.getElementById('dashboardComponentChoseType').removeEventListener('change', this._ifSelected);
    }


    _createList()  { 
        let type ;
        var list = `<legend> </legend>`
        for( var i = 0; i<this._types.length; i++) {
            type = this._types[i];
            list += `<input id="type_${type}" value="${type}" type="radio" name="type"></input>
                    <label for="type_${type}">${type}</label>`

        }

        this.shadowRoot.querySelector('fieldset').innerHTML = list; 
        this.shadowRoot.querySelector('legend').innerHTML = this.getAttribute('title');
        this.shadowRoot.querySelector('input').setAttribute('checked', "checked");


    }
    
    _ifSelected = (event) => {
        this._selected = event.target.value; 
        this.shadowRoot.querySelector('fieldset').setAttribute('selected',`${this._selected}`); 
        this.dispatchEvent(this.changeEvent);
    };

}
customElements.define('c-fieldset', myFieldset);