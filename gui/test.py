"""
https://stackoverflow.com/questions/57619227/connect-qml-signal-to-pyside2-slot
https://stackoverflow.com/questions/54010254/connect-python-signal-to-qml-ui-slot-with-pyside2

"""

import os
import sys
import time
from PySide2 import QtCore, QtWidgets, QtQml


if __name__ == "__main__":
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QtWidgets.QApplication(sys.argv)
    engine = QtQml.QQmlApplicationEngine()
    # engine.load('main.qml')
    engine.load('./test_qml/main.qml')
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
