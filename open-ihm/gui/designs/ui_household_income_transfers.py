# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_transfers.ui'
#
# Created: Tue Apr 19 03:45:25 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdIncomeTransfers(object):
    def setupUi(self, AddHouseholdIncomeTransfers):
        AddHouseholdIncomeTransfers.setObjectName(_fromUtf8("AddHouseholdIncomeTransfers"))
        AddHouseholdIncomeTransfers.resize(432, 382)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.cmbSourceOfTransfer = QtGui.QComboBox(AddHouseholdIncomeTransfers)
        self.cmbSourceOfTransfer.setGeometry(QtCore.QRect(130, 40, 251, 22))
        self.cmbSourceOfTransfer.setEditable(True)
        self.cmbSourceOfTransfer.setObjectName(_fromUtf8("cmbSourceOfTransfer"))
        self.txtCash = QtGui.QLineEdit(AddHouseholdIncomeTransfers)
        self.txtCash.setGeometry(QtCore.QRect(130, 80, 111, 20))
        self.txtCash.setObjectName(_fromUtf8("txtCash"))
        self.cmdCancel = QtGui.QPushButton(AddHouseholdIncomeTransfers)
        self.cmdCancel.setGeometry(QtCore.QRect(340, 340, 75, 31))
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.label = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label.setGeometry(QtCore.QRect(20, 10, 91, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 91, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeTransfers)
        self.lblHouseholdName.setGeometry(QtCore.QRect(130, 10, 271, 21))
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.cmdSave = QtGui.QPushButton(AddHouseholdIncomeTransfers)
        self.cmdSave.setGeometry(QtCore.QRect(20, 340, 75, 31))
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.groupBox = QtGui.QGroupBox(AddHouseholdIncomeTransfers)
        self.groupBox.setGeometry(QtCore.QRect(10, 110, 411, 221))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.txtUnitsConsumed = QtGui.QLineEdit(self.groupBox)
        self.txtUnitsConsumed.setGeometry(QtCore.QRect(120, 100, 111, 20))
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.txtUnitOfMeasure = QtGui.QLineEdit(self.groupBox)
        self.txtUnitOfMeasure.setGeometry(QtCore.QRect(120, 60, 111, 20))
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 100, 91, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.txtUnitsSold = QtGui.QLineEdit(self.groupBox)
        self.txtUnitsSold.setGeometry(QtCore.QRect(120, 140, 111, 20))
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 91, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 81, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.cmbFoodType = QtGui.QComboBox(self.groupBox)
        self.cmbFoodType.setGeometry(QtCore.QRect(120, 20, 281, 22))
        self.cmbFoodType.setEditable(True)
        self.cmbFoodType.setObjectName(_fromUtf8("cmbFoodType"))
        self.txtUnitPrice = QtGui.QLineEdit(self.groupBox)
        self.txtUnitPrice.setGeometry(QtCore.QRect(120, 180, 111, 20))
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(20, 180, 81, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))

        self.retranslateUi(AddHouseholdIncomeTransfers)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeTransfers.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeTransfers.saveIncome)
        QtCore.QObject.connect(self.cmbFoodType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeTransfers.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeTransfers)
        AddHouseholdIncomeTransfers.setTabOrder(self.cmbSourceOfTransfer, self.txtCash)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtCash, self.cmbFoodType)
        AddHouseholdIncomeTransfers.setTabOrder(self.cmbFoodType, self.txtUnitOfMeasure)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsConsumed)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtUnitsConsumed, self.txtUnitsSold)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeTransfers.setTabOrder(self.txtUnitPrice, self.cmdSave)
        AddHouseholdIncomeTransfers.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeTransfers):
        AddHouseholdIncomeTransfers.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Add Transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Source of Transfer:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Cash per Year:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Food Transfer", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Food Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeTransfers", "Price per Unit:", None, QtGui.QApplication.UnicodeUTF8))

