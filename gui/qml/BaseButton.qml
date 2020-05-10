import QtQuick 2.0
import "./config.js" as Config
import "./componentCreation.js" as SlrScript
import "./componentBCreation.js" as BtnScript
import QtQuick.Controls 2.0
import QtQuick.Layouts 1.0

Item {
    id: root
    property string text: "Button"
    property bool active: false
    width: Config.button_width
    height: Config.button_height

    Button {
        id: button
        width: 100
        onClicked: {
            BtnScript.createComponent(root.text)
        }
        background: Rectangle {
            anchors.fill: parent
            radius: Config.button_radius
            height: Config.button_height
            width: Config.button_width
            color: root.active? Config.color_primary:Config.color_inactive
            visible: true
        }

        contentItem: Text{
            text: root.text
            color: "white"
            font.pixelSize: Config.button_text_size
            font.bold: true
        }
    }
}

/*##^##
Designer {
    D{i:0;autoSize:true;height:480;width:640}D{i:2;anchors_x:0}D{i:1;anchors_width:490;anchors_x:75}
}
##^##*/

