import QtQuick 2.0
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0
import "src/cards"
import "./material/qml/material"
import QtGraphicalEffects 1.0

Item {
    id: root
    height: 300
    width: moderow.width+moderow.spacing
    signal clicked()


    Flickable {
        id: flickable
        contentWidth: moderow.width+moderow.spacing
        anchors.fill: parent

        RowLayout {
            id: moderow
            y: 10
            anchors.leftMargin: 10
            anchors.left: parent.left
            spacing: 15

            Rectangle {
                id: preset1
                color: "#ffffff"
                Layout.preferredHeight: 120
                Layout.preferredWidth: 194
                Card {
                    id: card1
                    anchors.fill: parent
                    raised: false
                    RaisedButton {
                        id: raisedbutton1
                        x: 0
                        y: 124
                        height: 32
                        color: "#5677fc"
                        text: "Start"
                        textColor: "#ffffff"
                        anchors.bottom: parent.bottom
                        anchors.left: parent.left
                        anchors.right: parent.right
                        rippleColor: "#deffffff"
                        onClicked: {
                            root.clicked()
                        }
                    }

                    Text {
                        id: element3
                        x: 45
                        y: 8
                        text: qsTr("Pressure A/C")
                        font.pixelSize: 18
                    }

                    Text {
                        id: element4
                        x: 63
                        y: 42
                        color: "#555555"
                        text: qsTr("+20 / -20")
                        font.pixelSize: 18
                    }
                }

                //                MouseArea {
                //                    anchors.fill: parent
                //                    Connections {
                //                        target: QmlBridge
                //                    }
                //                }
            }

            Rectangle {
                id: preset2
                color: "#ffffff"
                Layout.preferredHeight: 120
                Layout.preferredWidth: 194
                Card {
                    id: card
                    anchors.fill: parent
                    raised: false
                    RaisedButton {
                        id: raisedbutton
                        x: 0
                        y: 124
                        height: 32
                        color: "#b3b3b3"
                        text: "In development"
                        textColor: "#ffffff"
                        anchors.bottom: parent.bottom
                        anchors.left: parent.left
                        anchors.right: parent.right
                        rippleColor: "#deffffff"
                    }

                    Text {
                        id: element1
                        x: 45
                        y: 8
                        text: qsTr("VOLUME A/C")
        
                        font.pixelSize: 18
                    }

                    Text {
                        id: element2
                        x: 63
                        y: 42
                        color: "#555555"
                        text: qsTr("750 / 20")
                        font.pixelSize: 18
                    }
                }
            }

            Rectangle {
                id: preset3
                color: "#ffffff"
                Layout.preferredHeight: 120
                Layout.preferredWidth: 194
                Card {
                    id: card2
                    anchors.fill: parent
                    raised: false
                    RaisedButton {
                        id: raisedbutton2
                        x: 0
                        y: 124
                        height: 32
                        color: "#b3b3b3"
                        text: "In development"
                        textColor: "#ffffff"
                        anchors.bottom: parent.bottom
                        anchors.left: parent.left
                        anchors.right: parent.right
                        rippleColor: "#deffffff"
                    }

                    Text {
                        id: title3
                        y: 7
                        text: qsTr("PSV")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter

                        font.pixelSize: 18
                    }

                    Text {
                        id: element6
                        x: 63
                        y: 42
                        color: "#555555"
                        text: qsTr("50 / 32")
                        font.pixelSize: 18
                    }
                }
            }

            Rectangle {
                id: preset4
                color: "#ffffff"
                Layout.preferredWidth: 194
                Card {
                    id: card3
                    anchors.fill: parent
                    RaisedButton {
                        id: raisedbutton3
                        x: 0
                        y: 124
                        height: 32
                        color: "#b3b3b3"
                        text: "In development"
                        anchors.left: parent.left
                        textColor: "#ffffff"
                        rippleColor: "#deffffff"
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                    }

                    Text {
                        id: element7
                        y: 7
                        text: qsTr("P-SIMV")
                        verticalAlignment: Text.AlignVCenter
                        horizontalAlignment: Text.AlignHCenter
                        anchors.left: parent.left
                        anchors.right: parent.right
                       
                        font.pixelSize: 18
                    }

                    Text {
                        id: element8
                        x: 63
                        y: 42
                        color: "#555555"
                        text: qsTr("50 / 32")
                        font.pixelSize: 18
                    }
                    raised: false
                }
                Layout.preferredHeight: 120
            }

            Rectangle {
                id: preset5
                color: "#ffffff"
                Layout.preferredWidth: 194
                Card {
                    id: card4
                    anchors.fill: parent
                    RaisedButton {
                        id: raisedbutton4
                        x: 0
                        y: 124
                        height: 32
                        color: "#b3b3b3"
                        text: "In development"
                        anchors.left: parent.left
                        textColor: "#ffffff"
                        rippleColor: "#deffffff"
                        anchors.right: parent.right
                        anchors.bottom: parent.bottom
                    }

                    Text {
                        id: element9
                        y: 7
                        text: qsTr("V-SIMV")
                        anchors.left: parent.left
                        anchors.right: parent.right
                        horizontalAlignment: Text.AlignHCenter
                       
                        verticalAlignment: Text.AlignVCenter
                        font.pixelSize: 18
                    }

                    Text {
                        id: element10
                        x: 63
                        y: 42
                        color: "#555555"
                        text: qsTr("50 / 32")
                        font.pixelSize: 18
                    }
                    raised: false
                }
                Layout.preferredHeight: 120
            }
        }
    }


//    Rectangle {
//        id: gradient

//        anchors.fill: parent
//        LinearGradient {
//            anchors.fill: parent
//            start: 30
//            end: 50
//            gradient: Gradient {
//                GradientStop { position: 0.0; color: "white" }
//                GradientStop { position: 1.0; color: "black" }
//            }
//        }
//    }
}

/*##^##
Designer {
    D{i:0;formeditorZoom:0.5}D{i:20;anchors_x:70}D{i:26;anchors_x:70}D{i:21;anchors_width:193;anchors_x:"-69"}
D{i:32;anchors_x:70}D{i:27;anchors_width:193;anchors_x:"-69"}D{i:2;anchors_x:8}D{i:33;anchors_height:200;anchors_width:200;anchors_x:143;anchors_y:170}
}
##^##*/
