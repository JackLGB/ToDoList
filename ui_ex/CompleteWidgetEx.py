from PyQt5.QtWidgets import QWidget

from ui import Ui_CompleteWidget


class CompleteWidgetEx(QWidget, Ui_CompleteWidget):
    def __init__(self):
        super(CompleteWidgetEx, self).__init__()
        self.setupUi(self)