import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import "./material/qml/material"
import "./config.js" as Config
import "./componentBCreation.js" as MyScript
import "."

Item {
    id: name
    width: 650
    height: 460
    signal presetClicked()
    onPresetClicked: {
        view.push(selectbreathe)
    }
    Component.onCompleted:{
        MyScript.createButtonComponent(MyScript.toArray(ModeSelect.buttonList))
    }


    Flickable{
        id: flickablePage
        interactive: false
        contentHeight: 500
        anchors.fill: parent
        Text {
            id: title
            y: 78
            text: qsTr("Select Mode")
            horizontalAlignment: Text.AlignHCenter
            anchors.left: parent.left
            anchors.right: parent.right
            font.pointSize: 32
        }
        Button{
            text: "back"
            onClicked: MyScript.backButton()
            
        }

        Row {
            id: rowButtons
            y: 213
            spacing: 15
            anchors.rightMargin: 20
            anchors.leftMargin: 20+this.spacing
            anchors.right: parent.right
            anchors.left: parent.left
        }

        Row {
            id: rowBreath
            y: 213
            spacing: 15
            anchors.rightMargin: 20
            anchors.leftMargin: 20+this.spacing
            anchors.right: parent.right
            anchors.left: parent.left
        }

        Row {
            id: rowTrigger
            y: 213
            spacing: 15
            anchors.rightMargin: 20
            anchors.leftMargin: 20+this.spacing
            anchors.right: parent.right
            anchors.left: parent.left
        }

        Item{
            visible:false
            id: flickableItems
        }
    }
}



/*##^##
Designer {
    D{i:0;formeditorZoom:0.8999999761581421}D{i:2;anchors_height:300;anchors_width:300;anchors_x:88;anchors_y:128}
D{i:1;anchors_height:200;anchors_width:200}
}
##^##*/
