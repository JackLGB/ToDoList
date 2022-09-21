from PyQt5.QtWidgets import QWidget

from ui import Ui_SettingWidget


class SettingWidgetEx(QWidget, Ui_SettingWidget):
    def __init__(self):
        super(SettingWidgetEx, self).__init__()
        self.setupUi(self)