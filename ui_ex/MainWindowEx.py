from PyQt5.QtWidgets import  QMainWindow

from ui import Ui_MainWindow


class MainWindowEx(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindowEx, self).__init__()
        self.setupUi(self)