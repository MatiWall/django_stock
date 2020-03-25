

class modalLayoutStandard extends HTMLElement {

    constructor() {
        super()

        this.attachShadow({ mode: 'open' });

        this.shadowRoot.innerHTML = `
            <p> This is a Test </p>

        `// Stops here
    }



}

customElements.define('modal-layout-standard', modalLayoutStandard);
