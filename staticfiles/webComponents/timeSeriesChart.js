class timeSeriesChart extends HTMLElement {
    constructor() {
        super();
       

        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = ``;
    

    }

    get types() {
        return this.getAttribute('types');
    }


    //attributeChangedCallback(name, oldVal, newVal) { // use this for intra day data. Update every time backend send new data.
      //  console.log(`Attribute: ${name} changed!`);
    //}




}
customElements.define('time-series-chart', timeSeriesChart);