# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_report_householdincome.ui'
#
# Created: Sun Oct 17 13:58:35 2010
#      by: PyQt4 UI code generator 4.7.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HouseholdIncomeReport(object):
    def setupUi(self, HouseholdIncomeReport):
        HouseholdIncomeReport.setObjectName(_fromUtf8("HouseholdIncomeReport"))
        HouseholdIncomeReport.resize(632, 628)
        HouseholdIncomeReport.setMinimumSize(QtCore.QSize(632, 628))
        self.cmbProjects = QtGui.QComboBox(HouseholdIncomeReport)
        self.cmbProjects.setGeometry(QtCore.QRect(80, 10, 551, 22))
        self.cmbProjects.setObjectName(_fromUtf8("cmbProjects"))
        self.label = QtGui.QLabel(HouseholdIncomeReport)
        self.label.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label.setObjectName(_fromUtf8("label"))
        self.cmdClose = QtGui.QPushButton(HouseholdIncomeReport)
        self.cmdClose.setGeometry(QtCore.QRect(530, 600, 101, 23))
        self.cmdClose.setObjectName(_fromUtf8("cmdClose"))
        self.cmdShowReport = QtGui.QPushButton(HouseholdIncomeReport)
        self.cmdShowReport.setGeometry(QtCore.QRect(410, 600, 111, 23))
        self.cmdShowReport.setObjectName(_fromUtf8("cmdShowReport"))
        self.treeView = QtGui.QTreeView(HouseholdIncomeReport)
        self.treeView.setGeometry(QtCore.QRect(10, 220, 201, 291))
        self.treeView.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.treeView.setObjectName(_fromUtf8("treeView"))
        self.listViewHCharacteristics = QtGui.QListView(HouseholdIncomeReport)
        self.listViewHCharacteristics.setGeometry(QtCore.QRect(220, 220, 201, 291))
        self.listViewHCharacteristics.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listViewHCharacteristics.setObjectName(_fromUtf8("listViewHCharacteristics"))
        self.listViewPersonalCharacteristics = QtGui.QListView(HouseholdIncomeReport)
        self.listViewPersonalCharacteristics.setGeometry(QtCore.QRect(430, 220, 191, 291))
        self.listViewPersonalCharacteristics.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.listViewPersonalCharacteristics.setObjectName(_fromUtf8("listViewPersonalCharacteristics"))
        self.label_4 = QtGui.QLabel(HouseholdIncomeReport)
        self.label_4.setGeometry(QtCore.QRect(225, 200, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(HouseholdIncomeReport)
        self.label_5.setGeometry(QtCore.QRect(430, 200, 181, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_5 = QtGui.QFrame(HouseholdIncomeReport)
        self.line_5.setGeometry(QtCore.QRect(0, 510, 631, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.label_8 = QtGui.QLabel(HouseholdIncomeReport)
        self.label_8.setGeometry(QtCore.QRect(10, 520, 241, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.frame_2 = QtGui.QFrame(HouseholdIncomeReport)
        self.frame_2.setGeometry(QtCore.QRect(430, 560, 181, 21))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.opt2Ascending = QtGui.QRadioButton(self.frame_2)
        self.opt2Ascending.setGeometry(QtCore.QRect(10, 0, 82, 17))
        self.opt2Ascending.setObjectName(_fromUtf8("opt2Ascending"))
        self.opt2Descending = QtGui.QRadioButton(self.frame_2)
        self.opt2Descending.setGeometry(QtCore.QRect(100, 0, 82, 17))
        self.opt2Descending.setObjectName(_fromUtf8("opt2Descending"))
        self.cmbOrderCriteria2 = QtGui.QComboBox(HouseholdIncomeReport)
        self.cmbOrderCriteria2.setGeometry(QtCore.QRect(320, 560, 101, 22))
        self.cmbOrderCriteria2.setObjectName(_fromUtf8("cmbOrderCriteria2"))
        self.line_3 = QtGui.QFrame(HouseholdIncomeReport)
        self.line_3.setGeometry(QtCore.QRect(0, 530, 631, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.cmbOrderCriteria1 = QtGui.QComboBox(HouseholdIncomeReport)
        self.cmbOrderCriteria1.setGeometry(QtCore.QRect(10, 560, 101, 22))
        self.cmbOrderCriteria1.setObjectName(_fromUtf8("cmbOrderCriteria1"))
        self.cmbOrderCriteria1.addItem(_fromUtf8(""))
        self.cmbOrderCriteria1.addItem(_fromUtf8(""))
        self.frame = QtGui.QFrame(HouseholdIncomeReport)
        self.frame.setGeometry(QtCore.QRect(130, 560, 171, 21))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.opt1Ascending = QtGui.QRadioButton(self.frame)
        self.opt1Ascending.setGeometry(QtCore.QRect(10, 0, 111, 17))
        self.opt1Ascending.setObjectName(_fromUtf8("opt1Ascending"))
        self.opt1Descending = QtGui.QRadioButton(self.frame)
        self.opt1Descending.setGeometry(QtCore.QRect(90, 0, 82, 17))
        self.opt1Descending.setObjectName(_fromUtf8("opt1Descending"))
        self.line_2 = QtGui.QFrame(HouseholdIncomeReport)
        self.line_2.setGeometry(QtCore.QRect(0, 580, 631, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_7 = QtGui.QLabel(HouseholdIncomeReport)
        self.label_7.setGeometry(QtCore.QRect(320, 540, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_6 = QtGui.QLabel(HouseholdIncomeReport)
        self.label_6.setGeometry(QtCore.QRect(10, 540, 111, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(HouseholdIncomeReport)
        self.line.setGeometry(QtCore.QRect(300, 540, 20, 51))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.treeViewHouseholds = QtGui.QTreeView(HouseholdIncomeReport)
        self.treeViewHouseholds.setGeometry(QtCore.QRect(10, 50, 611, 141))
        self.treeViewHouseholds.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.treeViewHouseholds.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.treeViewHouseholds.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.treeViewHouseholds.setObjectName(_fromUtf8("treeViewHouseholds"))

        self.retranslateUi(HouseholdIncomeReport)
        QtCore.QMetaObject.connectSlotsByName(HouseholdIncomeReport)

    def retranslateUi(self, HouseholdIncomeReport):
        HouseholdIncomeReport.setWindowTitle(QtGui.QApplication.translate("HouseholdIncomeReport", "Report: Households by Income Source", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdShowReport.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Show Report", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Report Data Sort Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.opt2Ascending.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Ascending", None, QtGui.QApplication.UnicodeUTF8))
        self.opt2Descending.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Descending", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOrderCriteria1.setItemText(0, QtGui.QApplication.translate("HouseholdIncomeReport", "Household Number", None, QtGui.QApplication.UnicodeUTF8))
        self.cmbOrderCriteria1.setItemText(1, QtGui.QApplication.translate("HouseholdIncomeReport", "Household Name", None, QtGui.QApplication.UnicodeUTF8))
        self.opt1Ascending.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Ascending", None, QtGui.QApplication.UnicodeUTF8))
        self.opt1Descending.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "Descending", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "2nd Ordering Criteria", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("HouseholdIncomeReport", "1st Ordering Criteria", None, QtGui.QApplication.UnicodeUTF8))
