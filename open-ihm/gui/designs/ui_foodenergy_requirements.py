# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_foodenergy_requirements.ui'
#
# Created: Tue Sep 21 14:51:08 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FoodEnergyRequirements(object):
    def setupUi(self, FoodEnergyRequirements):
        FoodEnergyRequirements.setObjectName(_fromUtf8("FoodEnergyRequirements"))
        FoodEnergyRequirements.resize(452, 532)
        FoodEnergyRequirements.setMinimumSize(QtCore.QSize(452, 532))
        self.cmdFERequirementsClose = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdFERequirementsClose.setGeometry(QtCore.QRect(370, 500, 75, 23))
        self.cmdFERequirementsClose.setObjectName(_fromUtf8("cmdFERequirementsClose"))
        self.cmdAddRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdAddRow.setGeometry(QtCore.QRect(70, 500, 75, 23))
        self.cmdAddRow.setObjectName(_fromUtf8("cmdAddRow"))
        self.cmdEditRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.cmdEditRow.setGeometry(QtCore.QRect(170, 500, 75, 23))
        self.cmdEditRow.setObjectName(_fromUtf8("cmdEditRow"))
        self.DeleteRow = QtGui.QPushButton(FoodEnergyRequirements)
        self.DeleteRow.setGeometry(QtCore.QRect(270, 500, 75, 23))
        self.DeleteRow.setObjectName(_fromUtf8("DeleteRow"))
        self.tableView = QtGui.QTableView(FoodEnergyRequirements)
        self.tableView.setGeometry(QtCore.QRect(0, 10, 441, 461))
        self.tableView.setObjectName(_fromUtf8("tableView"))

        self.retranslateUi(FoodEnergyRequirements)
        QtCore.QMetaObject.connectSlotsByName(FoodEnergyRequirements)

    def retranslateUi(self, FoodEnergyRequirements):
        FoodEnergyRequirements.setWindowTitle(QtGui.QApplication.translate("FoodEnergyRequirements", "Food Energy Requirements", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdFERequirementsClose.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdAddRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdEditRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Edit", None, QtGui.QApplication.UnicodeUTF8))
        self.DeleteRow.setText(QtGui.QApplication.translate("FoodEnergyRequirements", "Delete", None, QtGui.QApplication.UnicodeUTF8))
