# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git_project\ToDoList\ui\BodyWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BodyWidget(object):
    def setupUi(self, BodyWidget):
        BodyWidget.setObjectName("BodyWidget")
        BodyWidget.resize(400, 388)
        self.verticalLayout = QtWidgets.QVBoxLayout(BodyWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(BodyWidget)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.verticalLayout.addWidget(self.stackedWidget)

        self.retranslateUi(BodyWidget)
        QtCore.QMetaObject.connectSlotsByName(BodyWidget)

    def retranslateUi(self, BodyWidget):
        _translate = QtCore.QCoreApplication.translate
        BodyWidget.setWindowTitle(_translate("BodyWidget", "body"))
