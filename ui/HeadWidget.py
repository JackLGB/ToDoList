# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\git_project\ToDoList\ui\HeadWidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HeadWidget(object):
    def setupUi(self, HeadWidget):
        HeadWidget.setObjectName("HeadWidget")
        HeadWidget.resize(400, 40)
        HeadWidget.setMinimumSize(QtCore.QSize(0, 40))
        self.horizontalLayout = QtWidgets.QHBoxLayout(HeadWidget)
        self.horizontalLayout.setContentsMargins(0, 3, 0, 3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnNewItem = QtWidgets.QPushButton(HeadWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnNewItem.sizePolicy().hasHeightForWidth())
        self.btnNewItem.setSizePolicy(sizePolicy)
        self.btnNewItem.setObjectName("btnNewItem")
        self.horizontalLayout.addWidget(self.btnNewItem)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(HeadWidget)
        QtCore.QMetaObject.connectSlotsByName(HeadWidget)

    def retranslateUi(self, HeadWidget):
        _translate = QtCore.QCoreApplication.translate
        HeadWidget.setWindowTitle(_translate("HeadWidget", "head"))
        self.btnNewItem.setText(_translate("HeadWidget", "新建"))