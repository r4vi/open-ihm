# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_household_income_livestock.ui'
#
# Created: Thu Apr 21 19:28:07 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddHouseholdIncomeLivestock(object):
    def setupUi(self, AddHouseholdIncomeLivestock):
        AddHouseholdIncomeLivestock.setObjectName(_fromUtf8("AddHouseholdIncomeLivestock"))
        AddHouseholdIncomeLivestock.resize(400, 350)
        self.formLayout = QtGui.QFormLayout(AddHouseholdIncomeLivestock)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lblHouseholdName = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.lblHouseholdName.setObjectName(_fromUtf8("lblHouseholdName"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lblHouseholdName)
        self.label_2 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.cboIncomeType = QtGui.QComboBox(AddHouseholdIncomeLivestock)
        self.cboIncomeType.setEditable(True)
        self.cboIncomeType.setObjectName(_fromUtf8("cboIncomeType"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.cboIncomeType)
        self.label_7 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_7)
        self.txtUnitOfMeasure = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitOfMeasure.setObjectName(_fromUtf8("txtUnitOfMeasure"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.txtUnitOfMeasure)
        self.label_4 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.txtUnitsProduced = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsProduced.setObjectName(_fromUtf8("txtUnitsProduced"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.txtUnitsProduced)
        self.label_3 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_3)
        self.txtUnitsSold = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsSold.setObjectName(_fromUtf8("txtUnitsSold"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.txtUnitsSold)
        self.txtUnitPrice = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitPrice.setObjectName(_fromUtf8("txtUnitPrice"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.txtUnitPrice)
        self.label_8 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_8)
        self.txtUnitsOtherUses = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsOtherUses.setObjectName(_fromUtf8("txtUnitsOtherUses"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.txtUnitsOtherUses)
        self.label_5 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.txtUnitsConsumed = QtGui.QLineEdit(AddHouseholdIncomeLivestock)
        self.txtUnitsConsumed.setObjectName(_fromUtf8("txtUnitsConsumed"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.txtUnitsConsumed)
        self.groupBox = QtGui.QGroupBox(AddHouseholdIncomeLivestock)
        self.groupBox.setTitle(_fromUtf8(""))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.cmdSave = QtGui.QPushButton(self.groupBox)
        self.cmdSave.setDefault(True)
        self.cmdSave.setObjectName(_fromUtf8("cmdSave"))
        self.horizontalLayout.addWidget(self.cmdSave)
        self.cmdCancel = QtGui.QPushButton(self.groupBox)
        self.cmdCancel.setObjectName(_fromUtf8("cmdCancel"))
        self.horizontalLayout.addWidget(self.cmdCancel)
        self.formLayout.setWidget(9, QtGui.QFormLayout.SpanningRole, self.groupBox)
        self.label_6 = QtGui.QLabel(AddHouseholdIncomeLivestock)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_6)

        self.retranslateUi(AddHouseholdIncomeLivestock)
        QtCore.QObject.connect(self.cmdCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeLivestock.mdiClose)
        QtCore.QObject.connect(self.cmdSave, QtCore.SIGNAL(_fromUtf8("clicked()")), AddHouseholdIncomeLivestock.saveIncome)
        QtCore.QObject.connect(self.cboIncomeType, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), AddHouseholdIncomeLivestock.displayUnitOfMeasure)
        QtCore.QMetaObject.connectSlotsByName(AddHouseholdIncomeLivestock)
        AddHouseholdIncomeLivestock.setTabOrder(self.cboIncomeType, self.txtUnitOfMeasure)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitOfMeasure, self.txtUnitsProduced)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsProduced, self.txtUnitsSold)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsSold, self.txtUnitPrice)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitPrice, self.txtUnitsOtherUses)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsOtherUses, self.txtUnitsConsumed)
        AddHouseholdIncomeLivestock.setTabOrder(self.txtUnitsConsumed, self.cmdSave)
        AddHouseholdIncomeLivestock.setTabOrder(self.cmdSave, self.cmdCancel)

    def retranslateUi(self, AddHouseholdIncomeLivestock):
        AddHouseholdIncomeLivestock.setWindowTitle(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Add Livestock Income", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Household Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblHouseholdName.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "{householdname}", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Income Type:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Unit:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Produced:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Sold:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Other Uses:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Units Consumed:", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdSave.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdCancel.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("AddHouseholdIncomeLivestock", "Unit Price:", None, QtGui.QApplication.UnicodeUTF8))

