"""
TODO: add copyright, license, encoding
"""

import random
import time
# from main import args

import config
from PySide2 import QtCore, QtQml, QtWidgets


class ChartManager(QtCore.QObject):
    # create a signal
    dataReady = QtCore.Signal(QtCore.QPointF, name='dataReady')

    # TODO: move all initialization here

    def __init__(self, parent=None, r=None):
        # if 'parent' is given then it will inherit it
        super(ChartManager, self).__init__(parent)
        self._currX = 0
        self._currY = 0
        self._delay = 0.2
        self._xIncrement = 1.0
        self._starter = False
        self._goOn = False
        self._threader = None

    # property 'starter' can be seen in qml
    # connected to the button start
    @QtCore.Property(bool)
    def starter(self):
        return self._starter

    # set the 'starter' property
    @starter.setter
    def setStarter(self, val):
        # val is returned from qml
        if self._multiplier == val:
            return
        # TODO: move to logger
        print(val)
        if val:
            self.start()
        else:
            self.stop()
        self._starter = val

    @QtCore.Property(float)
    def delay(self):
        return self._delay

    @delay.setter
    def setDelay(self, val):
        if self._delay == val:
            return

        # TODO: move to logger
        print(val)
        self._delay = val

    @QtCore.Property(float)
    def xIncrement(self):
        return self._xIncrement

    @xIncrement.setter
    def setXIncrement(self, val):
        if self._xIncrement == val:
            return
        # TODO: move to logger
        print(val)
        self._xIncrement = val

    def generatePoint(self):
        # increments and returns x and y

        self._currX += self._xIncrement
        if not config.useredis:
            self._currY = random.randint(1, 40)
        else:
            self._currY = float(config.r.get("pressure"))

        return self._currX, self._currY

    def stop(self):
        self._goOn = False
        # checks threader, if still alive, stays inside till dead
        if self._threader is not None:
            while self._threader.isRunning():
                time.sleep(0.1)

    def start(self):
        self._goOn = True
        self._threader = Threader(self.core, self)
        self._threader.start()

    def core(self):
        while self._goOn:
            # makes an XY point object using generatepoint
            # using 'self._currX,self._currY'
            p = QtCore.QPointF(*self.generatePoint())
            # sends signal and then waits for delay
            self.dataReady.emit(p)
            time.sleep(self._delay)

# -------------------------------------------------


class Threader(QtCore.QThread):
    """TOOD: Add desription

    Arguments:
        QtCore {[type]} -- [description]
    """

    def __init__(self, core, parent=None):
        super(Threader, self).__init__(parent)
        self._core = core

    def run(self):
        self._core()
