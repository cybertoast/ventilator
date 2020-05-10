// margin from the left
var leftX = 50;
// number of total components
var componentNumber;
// height of each component
// should be the same for all
var componentHeight = 90
// basic slider shape
var baseSlider = Qt.createComponent("BaseSlider.qml");
// basic radio group
var baseRadioGroup = Qt.createComponent("BaseRadioGroup.qml");

// classes that hold default values for
// every input, changes should be made here
class PIP{
    constructor(){
        this.name="PIP"
        this.initialVal=25
        this.minVal=15
        this.maxVal=40
        this.stepSize=5
    }
}

class BPM{
    constructor(){
        this.name="BPM"
        this.initialVal=20
        this.minVal=8
        this.maxVal=40
        this.stepSize=2
    }
}

class PMAX{
    constructor(){
        this.name="PMAX"
        this.initialVal=20
        this.minVal=0
        this.maxVal=40
        this.stepSize=5
    }
}

class PEEP{
    constructor(){
        this.name="PEEP"
        this.initialVal=10
        this.minVal=5
        this.maxVal=20
        this.stepSize=5
    }
}

class FIO2{
    constructor(){
        this.name="FIO2%"
        this.initialVal=60
        this.minVal=21
        this.maxVal=100
        this.stepSize=5
    }
}

// create a slider component given the slider class
function createSliderComponent(componentInstance, componentNumber) {
    var createComp = baseSlider.createObject(flickableItems, {
        x:leftX,
        y:componentNumber*componentHeight,
        name: componentInstance.name,
        initialVal: componentInstance.initialVal,
        minVal: componentInstance.minVal,
        maxVal: componentInstance.maxVal,
        stepSize: componentInstance.stepSize,
    })
    
    return createComp
}

// create IE ratio radio group
// change this if more radio groups are needed
function createIERatio(componentNumber) {
    var createComp = baseRadioGroup.createObject(flickableItems, {
        x:80,
        y:componentNumber*componentHeight
    })

    return createComp
}

// adds all components to view given a list of inputs
// the list must be a list of strings with names matching the component names
function addToView(componentList){
    for (let i = 0; i < componentList.length; i++) {
        const element = componentList[i];
        switch (element) {
            case "PIP":
                var pipComponent = new PIP();
                var component = createSliderComponent(pipComponent, componentNumber)
                if (component === null) {
                    // Error Handling
                    console.log("Error creating object "+element);
                }
                componentNumber++;
                break;
            case "BPM":
                var bpmComponent = new BPM();
                var component = createSliderComponent(bpmComponent, componentNumber);
                componentNumber++;
                if (component === null) {
                    // Error Handling
                    console.log("Error creating object "+element);
                }
                break
                case "IE":
                    var component = createIERatio(componentNumber);
                    componentNumber++;
                    if (component === null) {
                        // Error Handling
                        console.log("Error creating object "+element);
                    }
                    break
            case "PMAX":
                var pmaxComponent = new PMAX();
                var component = createSliderComponent(pmaxComponent, componentNumber)
                componentNumber++;
                if (component === null) {
                    // Error Handling
                    console.log("Error creating object "+element);
                }
                break
            case "PEEP":
                var peepComponent = new PEEP();
                var component = createSliderComponent(peepComponent, componentNumber)
                componentNumber++;
                if (component === null) {
                    // Error Handling
                    console.log("Error creating object "+element);
                }
                break
            case "FIO2":
                var fio2Component = new FIO2();
                var component = createSliderComponent(fio2Component, componentNumber)
                componentNumber++;
                if (component === null) {
                    // Error Handling
                    console.log("Error creating object "+element);
                }
                break
            default:
                console.log("Dont have the value "+ element)
                break;
        } 
    }
}


function getComponents(inputList) {
    componentNumber=1;
    var wantedComponents = inputList
    addToView(wantedComponents)

    return componentNumber
}

// takes in the view and sends name and value to python
function getComponentsValues(sliders){
    for(var i = 0; i < sliders.children.length; ++i)
        foo.test_slot(sliders.children[i].name, sliders.children[i].value)

}
