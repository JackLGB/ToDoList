from PyQt5.QtWidgets import QWidget

from ui import Ui_KanBanWidget


class KanBanWidgetEx(QWidget, Ui_KanBanWidget):
    def __init__(self):
        super(KanBanWidgetEx, self).__init__()
        self.setupUi(self)