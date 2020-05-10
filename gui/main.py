"""
https://stackoverflow.com/questions/57619227/connect-qml-signal-to-pyside2-slot
https://stackoverflow.com/questions/54010254/connect-python-signal-to-qml-ui-slot-with-pyside2

"""

import os
import sys
import time
from PySide2 import QtCore, QtWidgets, QtQml
import redis
import mode_select as ms
from patient import Patient

# r = redis.StrictRedis(
#     host='dupi1.local',
#     port=6379,
#     password='',
#     decode_responses=True)

class Foo(QtCore.QObject):
    @QtCore.Slot(str, int)
    def test_slot(self, mystring, myint):
        # r.mset({"values":string})
        # myvalue = r.get("values")
        if mystring=="FIO2%":
            mystring="FIO2"
        print("python", mystring, myint)


class Manager(QtCore.QObject):
    # create a signal
    dataReady = QtCore.Signal(QtCore.QPointF, name='dataReady')
    

    # initial values
    def __init__(self, parent=None):
        # if 'parent' is given then it will inherit it
        super(Manager, self).__init__(parent)
        self._currX = 0
        self._currY = 0
        self._delay = 0.5
        self._multiplier = 1.0
        self._power = 1.0
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
        print(val)
        if val:
            self.start()
        else:
            self.stop()
        self._starter = val

    
    @QtCore.Property(float)
    def multiplier(self):
        return self._multiplier

    # 'multiplier' can be set from qml
    # being set when slider 'multiplierSlider' is changed
    @multiplier.setter
    def setMultiplier(self, val):
        if self._multiplier == val:
            return
        print(val)
        self._multiplier = val

    # makes 'power'
    @QtCore.Property(int)
    def power(self):
        return self._power

    # sets power 
    @power.setter
    def setPower(self, val):
        if self._power == val:
            return
        print(val)
        self._power = val

    @QtCore.Property(float)
    def delay(self):
        return self._delay

    @delay.setter
    def setDelay(self, val):
        if self._delay == val:
            return
        print(val)
        self._delay = val

    @QtCore.Property(float)
    def xIncrement(self):
        return self._xIncrement

    @xIncrement.setter
    def setXIncrement(self, val):
        if self._xIncrement == val:
            return
        print(val)
        self._xIncrement = val

    def generatePoint(self):
        # increments and returns x and y

        self._currX += self._xIncrement
        self._currY = self._currY+3
        # self._currY = float(r.get("pressure"))

        return self._currX,self._currY

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
    def __init__(self,core,parent=None):
        super(Threader, self).__init__(parent)
        self._core = core

    def run(self):
        self._core()

if __name__ == "__main__":
    os.environ["QT_QUICK_CONTROLS_STYLE"] = "Material"
    app = QtWidgets.QApplication(sys.argv)

    manager = Manager()
    foo = Foo()
    patient = Patient()
    modeSelect = ms.ModeSelect()

    app.aboutToQuit.connect(manager.stop)
    manager.start()
    engine = QtQml.QQmlApplicationEngine()

    ctx = engine.rootContext()
    ctx.setContextProperty("Manager", manager)
    ctx.setContextProperty("foo", foo)
    ctx.setContextProperty("ModeSelect", modeSelect)
    ctx.setContextProperty("Patient", patient)

    # engine.load('main.qml')
    engine.load('./qml/MainQt.qml')
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec_())
