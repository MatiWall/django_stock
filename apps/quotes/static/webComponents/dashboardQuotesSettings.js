

var template = `
<template>



<template>


`// Template literal stops here




class QuotesSettings extends HTMLElement {
    constructor() {
        super();
       
        
        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = template;
        
    }

    get title() {
        return this.getAttribute('title');
    }

    connectedCallback() {

    }
    disconnectedCallback() {

    }

}
customElements.define('dash-quotes-settings',QuotesSettings);