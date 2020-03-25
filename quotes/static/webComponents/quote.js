

const button = `
        <button></button>
    ` // Stops here

const template = `

` // Stops here 

class quote extends HTMLElement {
    constructor() {
        super();

        this._quoteSettings = false;
        this._quote;
       

        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = button;

  
        
    }

    connectedCallback() {
        this.shadowRoot.querySelector("button").addEventListener('click', this._showSettings.bind(this));
        this.shadowRoot.querySelector("button").append(this.getAttribute("title"));
         
    }

    disconnectedCallback() {
        this.shadowRoot.querySelector("button").removeEventListener('click', this._showSettings);
    }

    _showSettings() {
        this._settingsVisible = true;
    }
    _hideModal() {
        this._modalSe = false;

    }

}
customElements.define('stock-quote', quote);