from PySide2 import QtCore, QtWidgets, QtQml
import json
import redis 
import config
from main import logging
import time


if config.useredis:
    logging.info("using redis")
    useredis = True
else:
    logging.info("not using redis")
    useredis=False

if useredis:
    r=config.r

mode_breath = {
    "Volume A/C": ["Volume Control", "Volume Assist"],
    "Pressure A/C": ["Pressure Control", "Pressure Assist"],
    "Pressure Support": ["Pressure Support"],
    "Volume SIMV": ["Volume Control", "Volume Assist", "Pressure Support"],
    "Pressure SIMV": ["Pressure Control","Pressure Assist", "Pressure Support"]
}

breath_trigger = {
    "Volume Control": ["Time Control"],
    "Volume Assist": ["Pressure Trigger", "Flow Trigger"],
    "Pressure Control": ["Time"],
    "Pressure Assist": ["Pressure Trigger ", "Flow Trigger "],
    "Pressure Support": ["Pressure Trigger  ", "Flow Trigger  "],
}

trigger_input = {
    "Time Control": ["IE", "VT", "Breath Per Minute", "PEEP", "FIO2"],
    "Pressure Trigger": ["IE", "VT", "Breath Per Minute", "PS", "PEEP", "FIO2"],
    "Flow Trigger": ["IE", "VT", "Breath Per Minute", "FS", "PEEP", "FIO2"],
    "Time": ["IE", "Insparotary Pressure", "Breath Per Minute", "PEEP", "FIO2"],
    "Pressure Trigger ": ["IE", "Insparotary Pressure", "Breath Per Minute", "PS", "PEEP", "FIO2"],
    "Flow Trigger ": ["IE", "Insparotary Pressure", "Breath Per Minute", "FS", "PEEP", "FIO2"],
    "Pressure Trigger  ": ["IE", "Insparotary Pressure", "Breath Per Minute", "PS", "FC", "PEEP", "FIO2"],
    "Flow Trigger  ": ["IE", "Insparotary Pressure", "Breath Per Minute", "FS", "FC", "PEEP", "FIO2"],
}


class ModeSelect(QtCore.QObject):
    # signal when mode is selected
    modeSelected = QtCore.Signal(str, name='modeSelected')
    # stop ventilation signal
    stopVent = QtCore.Signal(name='stopVent')

    def __init__(self, parent=None):
        super(ModeSelect, self).__init__(parent)
        self._currMode = ""
        self._currBreath = ""
        self._currTrigger = ""
        self._status = ""
        self._threader = None
        self._delay = 1
        # self.start() # threader start when variables are needed to be shown
        self._goOn = True
    @QtCore.Property(str)
    def buttonList(self):
        buttonList = ","

        if self._currTrigger != "":
            input_list = trigger_input[self._currTrigger]
            return buttonList.join(input_list)

        if self._currBreath != "":
            trigger_list = breath_trigger[self._currBreath]
            return buttonList.join(trigger_list)
        # choose mode
        if self._currMode != "":
            # list of breath
            breath_list = mode_breath[self._currMode]
            return buttonList.join(breath_list)

        return buttonList.join(mode_breath.keys())


    @QtCore.Property(str)
    def mode(self):
        return self._currMode

    @mode.setter
    def setMode(self, mode):
        self._currMode=mode
        if mode=="":
            logging.debug("mode reset")
        else:
            logging.debug(f'mode set: {mode}')

    @QtCore.Property(str)
    def breath(self):
        return self._currBreath

    @breath.setter
    def setBreath(self, breath):
        self._currBreath=breath
        if breath=="":
            logging.debug("breath reset")
        else:
            logging.debug(f'breath type set: {breath}')

    @QtCore.Property(str)
    def trigger(self):
        return self._currTrigger

    @trigger.setter
    def setTrigger(self, trigger):
        self._currTrigger=trigger
        if trigger=="":
            logging.debug("trigger reset")
        else:
            logging.debug(f'trigger type set: {trigger}')

    @QtCore.Property(str)
    def status(self):
        return self._status

    @status.setter
    def setStatus(self, status):
        logging.debug("status set: {}".format(status))
        self._status=status

    @QtCore.Slot()
    def stopVentilation(self):
        self._currMode = ""
        self._currTrigger = ""
        self._currBreath = ""
        logging.warning("Stopping Ventilation")
        # send status 'stop'
        if useredis:
            r.mset({"status":"stop"})        
        self.stopVent.emit()

    @QtCore.Slot()
    def startVentilation(self):
        self.status="start"
        logging.warning("Starting Ventilation")
        if useredis:
            r.mset({"status":self._status})        

    @QtCore.Slot(str, int)
    def sendValues(self, mystring, myint):
        # clean up for useredis
        if mystring=="FIO2%":
            mystring="FiO2"
        if mystring=="IE":
            mystring="ER"
        if mystring=="Insparotary Pressure":
            mystring="InspiratoryPressure"
        if mystring=="Breath Per Minute":
            mystring="Rate"
        if mystring=="PEEP":
            mystring="PEEP"

        # json get
        if useredis:
            params = r.get("PARAMS")
            params = json.loads(params)

            # json set
            params[mystring]=myint
            params["Mode"]=self._currMode
            params["BreathType"]=self._currBreath
            paramsdump = json.dumps(params)
            r.mset({"PARAMS":paramsdump})
            logging.info("Sending value to redis")

        logging.debug(f'Input {mystring} set: {myint}')
        self.modeSelected.emit(self._currMode)

    def start(self):
        self._threader = Threader(self.core, self)
        self._threader.start()

    def core(self):
        while self._goOn:
            # sends signal and then waits for delay
            # print("on thread")
            time.sleep(self._delay)

# ------------------------------------------------- 

class Threader(QtCore.QThread):
    def __init__(self,core,parent=None):
        super(Threader, self).__init__(parent)
        self._core = core

    def run(self):
        self._core()

if __name__ == "__main__":
    for key in mode_breath:
        print(key)

    # choose mode
    mode = input("choose mode\n")

    # list of breath
    breath_list = mode_breath[mode]
    print("Breathe Types ", breath_list)

    chosen_breathe = input("Choose breathe\n")
    print("Trigger Types", breath_trigger[chosen_breathe])

    chosen_trigger = input("Choose trigger\n")
    print("Inputs ", trigger_input[chosen_trigger])