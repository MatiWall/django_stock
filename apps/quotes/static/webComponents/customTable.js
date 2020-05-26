

var template = `

    <table>

    </table>

`// Stops here 



class myTable extends HTMLElement {

    constructor() {
        super()

        
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = template;

    }

    connectedCallback() {
        
    }



}

customElements.define('c-table', myTable);