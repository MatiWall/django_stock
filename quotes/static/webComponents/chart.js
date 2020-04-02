
class timeSeriesChart extends HTMLElement {

    constructor() {
        super();


        this.attachShadow({ mode: 'open' });


        this.shadowRoot.innerHTML =  `

        <style>

            div {
                width : 80%;
                height : 80%;
            }

        </style>
        
        
        <div id="chartContainer"> </div>`;

        this._data = [];
        this._config = {};
        this._layout = {};

    }



    get data(){
        return this._data;
    }

    set data(values){
        this._data = values;
    }


    get config() {
        return this._config;
    }

    set config(values) {
        this._config = values
    }


    get layout() {
        return this._layout;
    }

    set layout(values) {
        this._layout = values;
    }




    connectedCallback() {

        Plotly.newPlot(this.shadowRoot.getElementById('chartContainer'), this._data, this._layout, this._config);
       
    }




}

customElements.define('plotly-chart', timeSeriesChart);