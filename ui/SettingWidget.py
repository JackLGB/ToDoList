# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git_project\ToDoList\ui\SettingWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingWidget(object):
    def setupUi(self, SettingWidget):
        SettingWidget.setObjectName("SettingWidget")
        SettingWidget.resize(400, 699)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(SettingWidget)
        QtCore.QMetaObject.connectSlotsByName(SettingWidget)

    def retranslateUi(self, SettingWidget):
        _translate = QtCore.QCoreApplication.translate
        SettingWidget.setWindowTitle(_translate("SettingWidget", "setting"))
