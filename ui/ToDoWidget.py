# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git_project\ToDoList\ui\ToDoWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ToDoWidget(object):
    def setupUi(self, ToDoWidget):
        ToDoWidget.setObjectName("ToDoWidget")
        ToDoWidget.resize(400, 602)
        self.verticalLayout = QtWidgets.QVBoxLayout(ToDoWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolBox = QtWidgets.QToolBox(ToDoWidget)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 382, 532))
        self.page.setObjectName("page")
        self.toolBox.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 382, 532))
        self.page_2.setObjectName("page_2")
        self.toolBox.addItem(self.page_2, "")
        self.verticalLayout.addWidget(self.toolBox)

        self.retranslateUi(ToDoWidget)
        self.toolBox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(ToDoWidget)

    def retranslateUi(self, ToDoWidget):
        _translate = QtCore.QCoreApplication.translate
        ToDoWidget.setWindowTitle(_translate("ToDoWidget", "ToDo"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("ToDoWidget", "Page 1"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("ToDoWidget", "Page 2"))
