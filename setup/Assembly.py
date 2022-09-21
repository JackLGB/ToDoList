import sys

from PyQt5.QtWidgets import QApplication

from ui_ex import HeadWidgetEx, MainWindowEx, BodyWidgetEx, FootWidgetEx


class Application(MainWindowEx):
    headWidget = None
    bodyWidget = None
    footWidget = None

    def __init__(self):
        super(Application, self).__init__()
        self.addHeadWidget()
        self.addBodyWidget()
        self.addFootWidget()

    def addHeadWidget(self):
        """
        添加头部组件
        :return:
        """
        self.headWidget = HeadWidgetEx()
        self.mainVLayout.addWidget(self.headWidget, 0)

    def addBodyWidget(self):
        """
        添加主体组件
        :return:
        """
        self.bodyWidget = BodyWidgetEx()
        self.mainVLayout.addWidget(self.bodyWidget, 1)

    def addFootWidget(self):
        """
        添加底部组件
        :return:
        """
        self.footWidget = FootWidgetEx()
        self.mainVLayout.addWidget(self.footWidget, 0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Application()
    main.show()
    sys.exit(app.exec())
