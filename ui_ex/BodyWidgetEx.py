from PyQt5.QtWidgets import QWidget

from ui import Ui_BodyWidget



class BodyWidgetEx(QWidget, Ui_BodyWidget):
    def __init__(self):
        super(BodyWidgetEx, self).__init__()
        self.setupUi(self)