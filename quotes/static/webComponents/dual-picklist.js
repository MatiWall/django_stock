
/*
Note to self: det driller med dine attributes når du forsøget at flytte fra avalible listen til chosen
*/


var template = `

<style>
    :root {
        --buttonWidth: 3rem;
        --buttonHeight: 3rem;
        --columnHeaderFontColor: rgba(80, 80, 80, 1);
    }


    .dualPicklistAvalibleHeader {
        font-size: 13px;
        color: var(--columnHeaderFontColor);
        grid-area: avalible-header;
    }

    .dualPicklistAddRemoveHeader {
        grid-area: add-remove-header;
    }

    .dualPicklistChosenHeader {
        font-size: 13px;
        color: var(--columnHeaderFontColor);
        grid-area: chosen-header;
    }

    .dualPicklistReorder {
        grid-area: reorder-header;
    }


    .dualPicklistAavalible {
        grid-area: avalible;
    }

    .dualPicklistAddRemove {
        grid-area: add-remove;
    }

    .dualPicklistChosen {
        grid-area: chosen;
    }

    .dualPicklistReorder {
        grid-area: reorder;
    }

    .dualPickListContainer {
        display: grid;
        grid-template-areas: 'avalible-header add-remove-header chosen-header reorder-header'
            'avalible add-remove chosen reorder';
        grid-gap: 10px;
        grid-template-columns: minmax(6em, 4fr) 1fr minmax(6em, 4fr) 1fr;


    }

    .buttonPicklistPosition {
        margin: 0px 0px 5px 0px;
        align-content: center;
    }

    .dualPicklistOptions {
        border: 1px solid #dddbda;
        border-radius: .25rem;
        padding: .25rem 0;
        height: 15rem;
        background-color: #fff;
        overflow: auto;

    }



    .picklistItem {
        all: unset;
        cursor: pointer;
    }

    .picklistItem:hover {
        background-color: lightgrey;
    }

    .selectedPicklistItem {
        border: solid;
    }




    /* Arrow buttons*/


    arrow {
        border: solid black;
        border-width: 0 3px 3px 0;
        display: inline-block;
        padding: 3px;
    }

    .right {
        transform: rotate(-45deg);
        -webkit-transform: rotate(-45deg);
    }

    .left {
        transform: rotate(135deg);
        -webkit-transform: rotate(135deg);
    }

    .up {
        transform: rotate(-135deg);
        -webkit-transform: rotate(-135deg);
    }

    .down {
        transform: rotate(45deg);
        -webkit-transform: rotate(45deg);
    }
</style>

<div class="container">
    <h3 class="textHeadingSmall">Choose Values</h3>
    <div class="dualPickListContainer">
        <div class="dualPicklistAvalibleHeader">Avalible</div>
        <div class="dualPicklistAavalible">
            <div id="dualPicklistAvalibleOptions" class="dualPicklistOptions">
                <ol id="picklistOptionsAvalible">
                </ol>
            </div>
        </div>
        <div class="dualPicklistAddRemove">

            <button id="moveAvalibleToChosen" class="buttonPicklistPosition" type="button">
                <arrow class="right"> </arrow>
            </button>

            <button class="buttonPicklistPosition" type="button">
                <arrow class="left"> </arrow>
            </button>

        </div>

        <div class="dualPicklistChosenHeader">Chosen </div>
        <div class="dualPicklistChosen">
            <div id="dualPicklistChosenOptions" class="dualPicklistOptions">
            <ol id="picklistOptionsChosen">
            </ol>
            </div>
        </div>

        <div class="dualPicklistReorder ">
            <button class="buttonPicklistPosition" type="button">
                <arrow class="up"> </arrow>
            </button>
            <button class="buttonPicklistPosition" type="button">
                <arrow class="down "> </arrow>
            </button>
        </div>
    </div>

</div>

` // Stops here



function createObjectFromList(data) {
    // Creates and object that tells in which container the
    // item is and its id.
    var obj = {};

    data.forEach((item, _) => {
        id = Math.random().toString(36).substr(2, 9); // unique id
        obj[`${id}`] = item;
    });
    return obj;
}


function createList(element, data, include) {

    const keys = Object.keys(data);

    var list = ``;

    var info;
    for (const key of keys) {

        listItem = `<li id="${key}" class="picklistItem" >${data[key]} </li>`;
        list += listItem;

    }

    element.innerHTML = list;

}





class dualPicklist extends HTMLElement {
    constructor() {
        super();



        this.attachShadow({ mode: 'open' });
        this.shadowRoot.innerHTML = template;

        this.optionsList = ['item 1', 'item 2', 'item 3', 'item 4', 'item 5'];
        this._picklistAvalible = createObjectFromList(this.optionsList);
        this._selectedAvalible ;
        this._selectedChosen ;
        this.picklistChosen ;


        var element = this.shadowRoot.getElementById('picklistOptionsAvalible');
        createList(element, this._picklistAvalible, "Avalible");

    }


    connectedCallback() {
        // this.shadowRoot.querySelector("button").addEventListener('click', this._showSettings.bind(this));
        //this.shadowRoot.querySelector("button").append(this.getAttribute("title"));


        const elementOptionsAcalible = this.shadowRoot.getElementById("picklistOptionsAvalible");
        if (elementOptionsAcalible) {


            elementOptionsAcalible.addEventListener("click", e => {
                if (e.target && e.target.nodeName == "LI") {

                    console.log(e.target.id + " was clicked");

                    if (e.target.hasAttribute("selectedAvalible")) {
                        e.target.removeAttribute('selectedAvalible', '');
                        e.target.classList.remove('selectedPicklistItem');
                    } else {
                        e.target.setAttribute('selectedAvalible', '');
                        e.target.classList.add('selectedPicklistItem');
                    }


                }

                this._selectedAvalible = this.shadowRoot.querySelectorAll('[selectedAvalible]');
    
            });
        }

        const elementOptionsChosen = this.shadowRoot.getElementById("picklistOptionsChosen");
        if (elementOptionsChosen) {
            elementOptionsChosen.addEventListener("click", e => {
                if (e.target && e.target.nodeName == "LI") {

                    console.log(e.target.id + " was clicked");

                    if (e.target.hasAttribute("selectedChosen")) {
                        e.target.removeAttribute('selectedChosen', '');
                        e.target.classList.remove('selectedPicklistItem');
                    } else {
                        e.target.setAttribute('selectedChosen', '');
                        e.target.classList.add('selectedPicklistItem');
                    }

                }

            this._selectedChosen = this.shadowRoot.querySelectorAll('[selectedChosen]');       
                console.log(selectedAvalible);
            });

        }



     this.shadowRoot.getElementById("moveAvalibleToChosen").addEventListener("click", e => {
        //console.log(e.target,this.nodeName);
        this._selectedAvalible.forEach((item, index) => {
            console.log(item);
            //elementOptionsChosen.appendChild(item.removeAttribute("selectedAvalible"));

       
        });
       
    });



    }










    disconnectedCallback() {
        this.shadowRoot.getElementById("picklistOptionsAvalible").removeEventListener('click');
    }

}
customElements.define('dual-picklist', dualPicklist);