# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git_project\ToDoList\ui\CompleteWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompleteWidget(object):
    def setupUi(self, CompleteWidget):
        CompleteWidget.setObjectName("CompleteWidget")
        CompleteWidget.resize(400, 639)
        self.verticalLayout = QtWidgets.QVBoxLayout(CompleteWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(CompleteWidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 382, 569))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 382, 569))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(CompleteWidget)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(CompleteWidget)

    def retranslateUi(self, CompleteWidget):
        _translate = QtCore.QCoreApplication.translate
        CompleteWidget.setWindowTitle(_translate("CompleteWidget", "complete"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("CompleteWidget", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("CompleteWidget", "Page 2"))
