# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'H:\Computing\Transport Folder\Monkey Studio Files\View_Monsters.ui'
#
# Created: Wed Nov 15 10:02:53 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_View_Monsters(object):
    def setupUi(self, View_Monsters):
        View_Monsters.setObjectName(_fromUtf8("View_Monsters"))
        View_Monsters.resize(600, 480)
        View_Monsters.setStyleSheet(_fromUtf8("background-color: rgb(255, 55, 0);"))
        self.Monster_Manual_Label = QtGui.QLabel(View_Monsters)
        self.Monster_Manual_Label.setGeometry(QtCore.QRect(150, 20, 300, 50))
        self.Monster_Manual_Label.setObjectName(_fromUtf8("Monster_Manual_Label"))
        self.Back_Button = QtGui.QPushButton(View_Monsters)
        self.Back_Button.setGeometry(QtCore.QRect(490, 420, 100, 30))
        self.Back_Button.setStyleSheet(_fromUtf8("background-color: rgb(140, 140, 140);"))
        self.Back_Button.setDefault(False)
        self.Back_Button.setFlat(False)
        self.Back_Button.setObjectName(_fromUtf8("Back_Button"))
        self.View_Monster_Table = QtGui.QTableWidget(View_Monsters)
        self.View_Monster_Table.setGeometry(QtCore.QRect(3, 77, 596, 320))
        self.View_Monster_Table.setStyleSheet(_fromUtf8("background-color: rgb(140, 140, 140);"))
        self.View_Monster_Table.setObjectName(_fromUtf8("View_Monster_Table"))
        self.View_Monster_Table.setColumnCount(6)
        self.View_Monster_Table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.View_Monster_Table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.View_Monster_Table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.View_Monster_Table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.View_Monster_Table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.View_Monster_Table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.View_Monster_Table.setHorizontalHeaderItem(5, item)
        self.View_Monster_Table.horizontalHeader().setDefaultSectionSize(98)
        self.View_Monster_Table.horizontalHeader().setMinimumSectionSize(20)
        self.View_Monster_Table.verticalHeader().setDefaultSectionSize(30)

        self.retranslateUi(View_Monsters)
        QtCore.QMetaObject.connectSlotsByName(View_Monsters)

    def retranslateUi(self, View_Monsters):
        View_Monsters.setWindowTitle(_translate("View_Monsters", "View Monsters", None))
        self.Monster_Manual_Label.setText(_translate("View_Monsters", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">View Monsters</span></p></body></html>", None))
        self.Back_Button.setText(_translate("View_Monsters", "Back", None))
        item = self.View_Monster_Table.horizontalHeaderItem(0)
        item.setText(_translate("View_Monsters", "Name", None))
        item = self.View_Monster_Table.horizontalHeaderItem(1)
        item.setText(_translate("View_Monsters", "Race", None))
        item = self.View_Monster_Table.horizontalHeaderItem(2)
        item.setText(_translate("View_Monsters", "Size", None))
        item = self.View_Monster_Table.horizontalHeaderItem(3)
        item.setText(_translate("View_Monsters", "AC", None))
        item = self.View_Monster_Table.horizontalHeaderItem(4)
        item.setText(_translate("View_Monsters", "HP", None))
        item = self.View_Monster_Table.horizontalHeaderItem(5)
        item.setText(_translate("View_Monsters", "Challenge", None))

