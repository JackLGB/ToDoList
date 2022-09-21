from PyQt5.QtWidgets import QWidget

from ui import Ui_FootWidget


class FootWidgetEx(QWidget, Ui_FootWidget):
    def __init__(self):
        super(FootWidgetEx, self).__init__()
        self.setupUi(self)