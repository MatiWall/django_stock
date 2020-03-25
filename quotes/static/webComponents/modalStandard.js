
/*
    This is a standard modal "<modal-standard>" with a button
*/


class modal extends HTMLElement {
    constructor() {
        super();
        this._modalVisible = false;
        this._modal;
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = `
        <style>
            /* The Modal (background) */
            .modal {
                display: none; 
                position: fixed; 
                z-index: 1; 
                padding-top: 100px; 
                left: 0;
                top: 0;
                width: 100%; 
                height: 100%; 
                overflow: auto; 
                background-color: rgba(0,0,0,0.4); 
            }
            /* Modal Content */
            .modal-content {
                position: relative;
                background-color: white;
                margin: auto;
                padding: 0;
                border: 1px solid #888;
                border-radius: 10px;
                width: 80%;
                height: 70%;
                box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2),0 6px 20px 0 rgba(0,0,0,0.19);
                
            }
            
            /* The Close Button */
            .close {
                color: black;
                float: right;
                font-size: 28px;
                font-weight: bold;
                cursor: pointer;
            }

            .close:hover,
            .close:focus {
            color: rgb(255,255,255);
            text-decoration: none;
            }

            .modal-header {
            padding: 2px 16px;
            background-color: lightgrey;
            color: white;
            height: 10%;
            border-bottom: solid black 2px;
            }
            .modal-body {
                padding: 2px 16px; 
                margin: 20px 2px;
                max-height : 90%;
            }

        

        </style>
        <button class="buttonNeutral buttonSizeWide">Add Component</button>
        <div class="modal">
            <div class="modal-content">
                <div class="modal-header">
                    <span class="close">&times;</span>
                    <h1 style="text-align : center;"></h1>
                </div>
                <div class="modal-body">
                
                <slot></slot>
                
                </div>
            </div>
        </div>
        `
    }

    get title() {
        return this.getAttribute('title');
    }

    connectedCallback() {
        this._modal = this.shadowRoot.querySelector(".modal");
        this.shadowRoot.querySelector("button").addEventListener('click', this._showModal.bind(this));
        this.shadowRoot.querySelector(".close").addEventListener('click', this._hideModal.bind(this));
        this.shadowRoot.querySelector("h1").append(this.title);
    }
    disconnectedCallback() {
        this.shadowRoot.querySelector("button").removeEventListener('click', this._showModal);
        this.shadowRoot.querySelector(".close").removeEventListener('click', this._hideModal);
    }
    _showModal() {
        this._modalVisible = true;
        this._modal.style.display = 'block';
    }
    _hideModal() {
        this._modalVisible = false;
        this._modal.style.display = 'none';
    }
}
customElements.define('modal-standard',modal);