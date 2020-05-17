"""
TODO: Encoding, license, copyright, authorship
"""
# https://oxfordmedicine.com/view/10.1093/med/9780198784975.001.0001/med-9780198784975-chapter-7
import argparse
import os
import random
import sys
import test
import time

from alarm_manager import AlarmManager

from PySide2 import QtCore, QtQml, QtWidgets

# from chart_manager import ChartManager as cm
import config
import mode_select as ms
from config import logging as logging
from patient import Patient
from chart_manager import ChartManager
from chart_manager2 import ChartManager2
from chart_manager3 import ChartManager3


# TODO: This should all be in the main() function
parser = argparse.ArgumentParser(description='Run the main GUI code')
parser.add_argument('-r', '--redis', action='store_true',
                    help="run GUI and send information to redis")
parser.add_argument('-f', '--fullscreen', action='store_true',
                    help="run GUI in full screen, dont have a way to kill it using touch yet")
config.args = parser.parse_args()

if config.args.redis:
    config.useredis = True

if config.args.fullscreen:
    config.fullscreen = True


def main():
    # TODO: should be in a config file, and well documented!
    # TODO: we don't know what the environment settings should be!!
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QtWidgets.QApplication(sys.argv)

    chartManager = ChartManager()
    chartManager2 = ChartManager2()
    chartManager3 = ChartManager3()

    app.aboutToQuit.connect(chartManager.stop)
    app.aboutToQuit.connect(chartManager2.stop)
    app.aboutToQuit.connect(chartManager3.stop)

    chartManager.start()
    chartManager2.start()
    chartManager3.start()

    engine = QtQml.QQmlApplicationEngine()
    alarmManager = AlarmManager()
    alarmManager.start()
    patient = Patient()
    modeSelect = ms.ModeSelect()
    dp = 0

    ctx = engine.rootContext()
    ctx.setContextProperty("ChartManager", chartManager)
    ctx.setContextProperty("ChartManager2", chartManager2)
    ctx.setContextProperty("ChartManager3", chartManager3)
    ctx.setContextProperty("ModeSelect", modeSelect)
    ctx.setContextProperty("Patient", patient)
    ctx.setContextProperty("AlarmManager", alarmManager)
    ctx.setContextProperty("dp", dp)
    ctx.setContextProperty("fs", False)
    if config.args.fullscreen:
        logging.debug("Runnin in full screen")
        ctx.setContextProperty("fs", True)

    # engine.load('main.qml')
    engine.load('./qml/MainQt.qml')
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
