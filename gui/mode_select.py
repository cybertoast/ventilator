from PySide2 import QtCore, QtWidgets, QtQml

mode_breath = {
    "VAC": ["MVC", "MVA"],
    "PAC": ["MPC", "MPA"],
    "PSV": ["MPS"],
    "VMV": ["MVC", "MVA", "MPS"],
    "PMV": ["MPC","MPA", "MPS"]
}

breath_trigger = {
    "MVC": ["TTV"],
    "MVA": ["TPV", "TFV"],
    "MPC": ["TTP"],
    "MPA": ["TPP", "TFP"],
    "MPS": ["TPS", "TFS"],
}

trigger_input = {
    "TTV": ["IE", "VT", "BPM", "PEEP", "FIO2"],
    "TPV": ["IE", "VT", "BPM", "PS", "PEEP", "FIO2"],
    "TFV": ["IE", "VT", "BPM", "FS", "PEEP", "FIO2"],
    "TTP": ["IE", "IP", "BPM", "PEEP", "FIO2"],
    "TPP": ["IE", "IP", "BPM", "PS", "PEEP", "FIO2"],
    "TFP": ["IE", "IP", "BPM", "FS", "PEEP", "FIO2"],
    "TPS": ["IE", "IP", "BPM", "PS", "FC", "PEEP", "FIO2"],
    "TFS": ["IE", "IP", "BPM", "FS", "FC", "PEEP", "FIO2"],
}


class ModeSelect(QtCore.QObject):
    def __init__(self, parent=None):
        super(ModeSelect, self).__init__(parent)
        self._currMode = ""
        self._currBreath = ""
        self._currTrigger = ""

    @QtCore.Property(str)
    def buttonList(self):
        buttonList = ","

        if self._currTrigger is not "":
            input_list = trigger_input[self._currTrigger]
            return buttonList.join(input_list)

        if self._currBreath is not "":
            trigger_list = breath_trigger[self._currBreath]
            return buttonList.join(trigger_list)
        # choose mode
        if self._currMode is not "":
            # list of breath
            breath_list = mode_breath[self._currMode]
            return buttonList.join(breath_list)

        return buttonList.join(mode_breath.keys())





      

    @QtCore.Property(str)
    def mode(self):
        return self._currMode

    @mode.setter
    def setMode(self, mode):
        print("mode is ", mode)
        self._currMode=mode

    @QtCore.Property(str)
    def breath(self):
        return self._currBreath

    @breath.setter
    def setBreath(self, breath):
        print("breath is ", breath)
        self._currBreath=breath

    @QtCore.Property(str)
    def trigger(self):
        return self._currTrigger

    @trigger.setter
    def setTrigger(self, trigger):
        print("trigger is ", trigger)
        self._currTrigger=trigger


    @QtCore.Property(str)
    def modeList(self):
        modes_str = ""
        for key in mode_breath:
            modes_str=key+","+modes_str

        #print(modes_str)
        return modes_str



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