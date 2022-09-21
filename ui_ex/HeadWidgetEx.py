from PyQt5.QtWidgets import QWidget

from ui import Ui_HeadWidget


class HeadWidgetEx(QWidget, Ui_HeadWidget):
    def __init__(self):
        super(HeadWidgetEx, self).__init__()
        self.setupUi(self)