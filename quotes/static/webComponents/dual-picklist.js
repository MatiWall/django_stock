


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
    
    let list = ``;

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
       

        this._selectedAvalible;
        this._selectedChosen;
        this.picklistChosen;

        this.shadowRoot.innerHTML = `

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
                overflow-y: auto;
              
        
            }
        
        
            ol {
                width: 100%; 
                list-style-type: none; 
                display: flex; 
                flex-direction: column;
                padding: 0;
            }
           
        
            .picklistItem {
                all: unset;
                cursor: pointer;
                display: block;
                width: 100%;
            }
        
            .picklistItem:hover {
                background-color: lightgrey;
            }
        
            .selectedPicklistItem {
                border: solid;
                border-width: 1px;
                border-radius: 3px;
                border-color: lightgrey;
                
                background-color: rgba(200,200,200, 0.4);
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
            <h3 id="title" class="textHeadingSmall"></h3>
            <div class="dualPickListContainer">
                <div class="dualPicklistAvalibleHeader">Avalible</div>
                <div class="dualPicklistAavalible">
                    <div id="dualPicklistAvalibleOptions" class="dualPicklistOptions">
                        <ol id="picklistOptionsAvalible" class="picklistTable">
                        </ol>
                    </div>
                </div>
                <div class="dualPicklistAddRemove">
        
                    <button id="moveAvalibleToChosen" class="buttonPicklistPosition" type="button">
                        <arrow class="right"> </arrow>
                    </button>
        
                    <button id="moveChosenToAvalible" class="buttonPicklistPosition" type="button">
                        <arrow class="left"> </arrow>
                    </button>
        
                </div>
        
                <div class="dualPicklistChosenHeader">Chosen </div>
                <div class="dualPicklistChosen">
                    <div id="dualPicklistChosenOptions" class="dualPicklistOptions">
                    <ol id="picklistOptionsChosen" class="picklistTable">
                    </ol>
                    </div>
                </div>
        
                <div class="dualPicklistReorder ">
                    <button id="moveItemUp" class="buttonPicklistPosition" type="button">
                        <arrow class="up"> </arrow>
                    </button>
                    <button id="moveItemDown" class="buttonPicklistPosition" type="button">
                        <arrow class="down "> </arrow>
                    </button>
                </div>
            </div>
        
        </div>
        
        `;


        this._element = this.shadowRoot.getElementById('picklistOptionsAvalible');

   

    }

   

    connectedCallback() {
       
        this._elementOptionsChosen = this.shadowRoot.getElementById("picklistOptionsChosen");
        this._elementOptionsChosen.addEventListener("click", (e) => { this._attributeTrackerResponce(e, "Chosen") } );

        this.shadowRoot.getElementById(`moveAvalibleToChosen`).addEventListener("click", this._moveAvalibleToChosen.bind(this));
    


        

        this._elementOptionsAvalible = this.shadowRoot.getElementById("picklistOptionsAvalible");
        this._elementOptionsAvalible.addEventListener("click", (e) => {this._attributeTrackerResponce(e, "Avalible") } );
        this.shadowRoot.getElementById(`moveChosenToAvalible`).addEventListener("click", this._moveChosenToAvalible.bind(this));
    
       



        this.shadowRoot.getElementById("moveItemUp").addEventListener("click", this._responeceMoveItemUp.bind(this));


        this.shadowRoot.getElementById("moveItemDown").addEventListener("click", this._responceMoveItemDown.bind(this));


        // Set title
        this.shadowRoot.querySelector('#title').innerHTML = this.getAttribute('title');


    }


    disconnectedCallback() {
        this.shadowRoot.getElementById("picklistOptionsAvalible").removeEventListener('click',  (e) => {this._attributeTrackerResponce(e, "Avalible") } );
        this.shadowRoot.getElementById("picklistOptionsChosen").removeEventListener('click',  (e) => { this._attributeTrackerResponce(e, "Chosen") });
        this.shadowRoot.getElementById("moveAvalibleToChosen").removeEventListener("click", this._moveAvalibleToChosen);
        this.shadowRoot.getElementById("moveChosenToAvalible").removeEventListener("click", this._moveChosenToAvalible );
        this.shadowRoot.getElementById("moveItemDown").removeEventListener("click", this._responceMoveItemDown);
        this.shadowRoot.getElementById("moveItemUp").removeEventListener("click", this._responeceMoveItemUp);
    }


    get items() {
        return this._optionsList;
    }

    set items(values) {
        this._picklistAvalible = createObjectFromList(values);
        createList(this._element, this._picklistAvalible, "Avalible");
    }

    get chosenItems () {
        return this.picklistChosen;
    }





    _moveChosenToAvalible() { 
        this.shadowRoot.querySelectorAll(`[selected=Chosen]`).forEach((item, index) => {
        item.removeAttribute('selected');
        item.classList.remove('selectedPicklistItem');
        this._elementOptionsAvalible.appendChild(item);
    });}

    _moveAvalibleToChosen() {
        this.shadowRoot.querySelectorAll(`[selected=Avalible]`).forEach((item, index) => {
            item.removeAttribute('selected');
            item.classList.remove('selectedPicklistItem');
            this._elementOptionsChosen.appendChild(item);
        });
    }


    _responeceMoveItemUp() {
        var list = this.shadowRoot.getElementById("picklistOptionsChosen");
        var items = list.getElementsByTagName("LI");
        for (var i = 1; i < items.length; i++) {

            if (items[i].hasAttribute('selected')) {
                items[i].parentNode.insertBefore(items[i], items[i - 1]);
            }

        }
    }

    _responceMoveItemDown() {
            var list = this.shadowRoot.getElementById("picklistOptionsChosen");
            var items = list.getElementsByTagName("LI");
            for (var i = (items.length - 2); i >= 0; i--) {

                if (items[i].hasAttribute('selected')) {
                    items[i].parentNode.insertBefore(items[i + 1], items[i]);
                }

            }
    }


  

    _attributeTrackerResponce(e, type) {
            if (e.target && e.target.nodeName == "LI") {

                if (e.target.hasAttribute('selected')) {
                    e.target.removeAttribute('selected', type);
                    e.target.classList.remove('selectedPicklistItem');
                } else {
                    e.target.setAttribute('selected', type);
                    e.target.classList.add('selectedPicklistItem');
                }
            }
        }


}
customElements.define('dual-picklist', dualPicklist);