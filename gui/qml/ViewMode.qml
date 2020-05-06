import QtQuick 2.0
import QtQuick.Controls 2.13
import QtQuick.Layouts 1.0
import "./material/qml/material"
import "./config.js" as Config
import "./ViewModeSelector.js" as VMS

Item {
    id: name
    width: 650
    height: 460
    signal presetClicked()
    onPresetClicked: {
        view.push(selectbreathe)
    }

    StackView {
        id: view
        anchors.fill: parent
        initialItem: selectmode

        Component{
            id: selectmode
            Item{
                id: element1
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

                Row {
                    id: row
                    y: 213
                    spacing: 15
                    anchors.rightMargin: 20
                    anchors.leftMargin: 20+this.spacing
                    anchors.right: parent.right
                    anchors.left: parent.left

                    Button {
                        id: button1
                        property bool active: false
                        width: 100
                        //onClicked: view.push(selectbreathe)

                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: this.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                           text: "Volume AC"
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }

                    Button {
                        id: button2
                        property bool active: true
                        text: "Pressure AC"
                        onClicked: view.push(selectbreathe)

                        background: Rectangle {
                            id: background
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: button2.active? Config.color_primary:"red"
                            visible: true
                        }

                        contentItem: Text{
                           text: "Pressure AC"
                           color: button2.active? "white":"black"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }
                    Button {
                        id: button3
                        property bool active: false
                        width: 110
                        //onClicked: view.push(selectbreathe)


                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: this.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                            text: "PSV"
                            anchors.right: parent.right
                            anchors.left: parent.left
                            anchors.leftMargin: 0
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }
                    Button {
                        id: button4
                        property bool active: false
                        width: 100
                        //onClicked: view.push(selectbreathe)

                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: this.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                            text: "P-SIMV"
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            anchors.left: parent.left
                            anchors.right: parent.right
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }
                    Button {
                        id: button5
                        property bool active: false
                        width: 100
                        //onClicked: view.push(selectbreathe)

                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: this.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                            text: "V-SIMV"
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                            anchors.left: parent.left
                            anchors.right: parent.right
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }
                }
            }
        }

        Component{
            id: selectbreathe
            //anchors.fill: parent
            Item{
                id: element
                anchors.fill: parent
                Text {
                    id: title
                    y: 78
                    text: qsTr("Select Breathe Type")
                    horizontalAlignment: Text.AlignHCenter
                    anchors.left: parent.left
                    anchors.right: parent.right
                    font.pointSize: 32
                }
                Button{
                    id: buttonBack
                    onClicked: view.pop()
                    background: Rectangle{
                        visible: false
                    }
                    contentItem: Text{
                        text: "<"
                        font.pixelSize: 32
                        color: Config.color_dark
                        font.bold: true
                    }
                }

                Row {
                    x: 213
                    y: 213
                    spacing: 25

                    Button {
                        id: buttonAssist
                        property bool active: false
                        width: 100
                        //onClicked: view.push(selectbreathe)

                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: this.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                            text: "Assist"
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }

                    Button {
                        id: buttonControl
                        property bool active: true
                        width: 100
                        onClicked: view.push(selecttrigger)

                        background: Rectangle {
                            anchors.fill: parent
                            radius: Config.button_radius
                            height: Config.button_height
                            width: Config.button_width
                            color: buttonControl.active? Config.color_primary:Config.color_inactive
                            visible: true
                        }

                        contentItem: Text{
                            text: "Control"
                            verticalAlignment: Text.AlignVCenter
                            horizontalAlignment: Text.AlignHCenter
                           color: "white"
                           font.pixelSize: Config.button_text_size
                           font.bold: true
                        }
                    }
                }
            }
        }

        Component{
            id: selecttrigger


            Flickable{

                Button{
                    id: buttonBack2
                    onClicked: view.pop()
                    background: Rectangle{
                        visible: false
                    }
                    contentItem: Text{
                        text: "<"
                        font.pixelSize: 32
                        color: Config.color_dark
                        font.bold: true
                    }
                }

                contentHeight:testheight.flickableheight
                anchors.fill: parent

            S_m2b1t0{
                id: testheight

            }

           }
        }


    }



}


/*##^##
Designer {
    D{i:0;formeditorZoom:1.5}D{i:2;anchors_height:300;anchors_width:300;anchors_x:88;anchors_y:128}
D{i:1;anchors_height:200;anchors_width:200}
}
##^##*/
