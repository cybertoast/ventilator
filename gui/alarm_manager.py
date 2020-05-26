"""
# TODO: 
#   * Add copyright, encoding, etc
#   * Logger rather than print()
#   * QCore.Property value sholud be set to constart=True
"""
import random
import time

# Todo: move config out
import config
from PySide2 import QtCore, QtQml, QtWidgets


class AlarmManager(QtCore.QObject):
    # create a signal
    alarmStatus = QtCore.Signal(str, name='alarmStatus')

    # Initialize attributes
    _status = None
    _title = None
    _info = None
    _delay = 0.5
    _starter = False
    _goOn = False
    _threader = None

    def __init__(self, parent=None, r=None):
        # if 'parent' is given then it will inherit it
        super(AlarmManager, self).__init__(parent)

    @QtCore.Property(str)
    def status(self):
        return self._status

    @status.setter
    def setStatus(self, val):
        self._status = val

    @QtCore.Property(str)
    def title(self):
        return self._title

    @title.setter
    def setTitle(self, val):
        self._title = val

    @QtCore.Property(str)
    def info(self):
        return self._info

    @info.setter
    def setinfo(self, val):
        self._info = val

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
        # Why is this an infinite loop here? There's no way out! Shouldn't this just be an event loop?
        while self._goOn:
            # TODOA what happens if redis is not used? This would end in an infinet loop!
            if config.useredis:
                try:
                    self._status = config.r.get("alarm_status")
                    self._title = config.r.get("alarm_title")
                    self._info = config.r.get("alarm_text")
                except:
                    config.logging.error("Could not get alarm data from redis")

                if "none" not in self._status:
                    print("emitting alarm ", self._info)
                self.alarmStatus.emit(config.r.get("alarm_status"))
                time.sleep(self._delay)

# -------------------------------------------------


class Threader(QtCore.QThread):
    # Initialize attributes
    _core = None

    def __init__(self, core, parent=None):
        super(Threader, self).__init__(parent)
        self._core = core

    def run(self):
        self._core()
