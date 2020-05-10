// basic button 
var baseButton = Qt.createComponent("BaseButton.qml");
var inputPage;
var inputList;
var sprite;
var inputListHeight;


function createButtonComponent(buttonList) {
    for (let i = 0; i < buttonList.length; i++) {
        const mode = buttonList[i];
        var createButtonComp = baseButton.createObject(rowButtons, {
            text: mode
        })
    }

    return createButtonComp
}

function createBreathButtons(buttonList) {
    for (let i = 0; i < buttonList.length; i++) {
        const mode = buttonList[i];
        var createButtonComp = baseButton.createObject(rowBreath, {
            text: mode
        })
    }

    return createButtonComp
}

function createTriggerButtons(buttonList) {
    for (let i = 0; i < buttonList.length; i++) {
        const mode = buttonList[i];
        var createButtonComp = baseButton.createObject(rowTrigger, {
            text: mode
        })
    }

    return createButtonComp
}

function toArray(string) {
    var result = string.split(",")
    return result
}

function createComponent(chosenButton) {
    if (ModeSelect.mode===""){
        // first click
        ModeSelect.mode = chosenButton
        title.text="Select Breathe Type"
        // show breath buttons
        rowBreath.visible=true
    } else if(ModeSelect.breath===""){
        title.text="Select Trigger Type"
        ModeSelect.breath = chosenButton
        // show trigger buttons
        rowTrigger.visible=true
    } else if (ModeSelect.trigger===""){
        title.text="Select Input"
        ModeSelect.trigger = chosenButton
        // show input page
        flickableItems.visible=true
    }

    // list is updated depending if mode, breath and trigger are populated
    var list = toArray(ModeSelect.buttonList)
    // for(var i = rowButtons.children.length; i > 0 ; i--) {
    //     rowButtons.children[i-1].visible=false
    // }

    if (ModeSelect.trigger!=="") {
        // hide trigger buttons
        rowTrigger.visible=false
        // make root page scrollable
        flickablePage.interactive=true
        // make sliders using list
        createInputs(list)
        // dynamicall resize page
        flickablePage.contentHeight = flickableItems.children[0].contentHeight
    }else if(ModeSelect.breath!==""){
        // make trigger row
        console.log("making trigger")
        createTriggerButtons(list)
        // remove breath buttons
        rowBreath.visible=false
    }else if(ModeSelect.mode!==""){
        // make breath row
        console.log("making breath")
        createBreathButtons(list)
        // remove mode row
        rowButtons.visible=false
    }
}

function backButton() {
    if (ModeSelect.trigger!==""){
        // set trigger to empty
        ModeSelect.trigger=""
        // hide input page
        flickableItems.visible=false
        // make page non interactive
        flickablePage.interactive=false
        // change title
        title.text="Select Trigger Type"
        // show trigger
        rowTrigger.visible=true
    
    } else if (ModeSelect.breath!==""){
        // set breath to empty
        ModeSelect.breath=""
        // hide trigger buttons
        rowTrigger.visible=false
        // hide previous buttons
        for(var i = rowTrigger.children.length; i > 0 ; i--) {
            console.log("destroying")
            rowTrigger.children[i-1].height=0
        }
        // change title
        title.text="Select Breath Type"
        // show trigger
        rowBreath.visible=true
    
    }else if (ModeSelect.mode!==""){
        // set mode to empty
        ModeSelect.mode=""
        // hide breath buttons
        rowBreath.visible=false
        // hide previous buttons
        for(var i = rowBreath.children.length; i > 0 ; i--) {
            console.log("destroying")
            rowBreath.children[i-1].height=0
        }
        // change title
        title.text="Select Mode"
        // show trigger
        rowButtons.visible=true
    
    }
}

function finishCreation() {
    if (inputPage.status == Component.Ready) {
        sprite = inputPage.createObject(flickableItems, {
            inputList:inputList
        });
        if (sprite == null) {
            // Error Handling
            console.log("Error creating object");
        }
    } else if (inputPage.status == Component.Error) {
        // Error Handling
        console.log("Error loading component:", inputPage.errorString());
    }
}

function createInputs(newInputList) {
    inputList = newInputList

    inputPage = Qt.createComponent("InputList.qml");
    if (inputPage.status == Component.Ready){
        finishCreation();
    }
    else{
    inputPage.statusChanged.connect(finishCreation);
    }
}
