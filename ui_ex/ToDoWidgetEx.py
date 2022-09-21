from PyQt5.QtWidgets import QWidget

from ui import Ui_ToDoWidget


class ToDoWidgetEx(QWidget, Ui_ToDoWidget):
    def __init__(self):
        super(ToDoWidgetEx, self).__init__()
        self.setupUi(self)