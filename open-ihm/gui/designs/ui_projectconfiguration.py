# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_projectconfiguration.ui'
#
# Created: Fri Mar 05 12:18:52 2010
#      by: PyQt4 UI code generator 4.7
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_ProjectConfiguration(object):
    def setupUi(self, ProjectConfiguration):
        ProjectConfiguration.setObjectName("ProjectConfiguration")
        ProjectConfiguration.resize(669, 515)
        ProjectConfiguration.setMinimumSize(QtCore.QSize(669, 515))
        ProjectConfiguration.setSizeIncrement(QtCore.QSize(0, 0))
        self.label = QtGui.QLabel(ProjectConfiguration)
        self.label.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label.setObjectName("label")
        self.lblProjectName = QtGui.QLabel(ProjectConfiguration)
        self.lblProjectName.setGeometry(QtCore.QRect(110, 10, 71, 16))
        self.lblProjectName.setObjectName("lblProjectName")
        self.tabProject = QtGui.QTabWidget(ProjectConfiguration)
        self.tabProject.setGeometry(QtCore.QRect(10, 40, 651, 431))
        self.tabProject.setObjectName("tabProject")
        self.tabProjectPersonalCharacteristics = QtGui.QWidget()
        self.tabProjectPersonalCharacteristics.setObjectName("tabProjectPersonalCharacteristics")
        self.lstPersonalAvailableChars = QtGui.QListView(self.tabProjectPersonalCharacteristics)
        self.lstPersonalAvailableChars.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.lstPersonalAvailableChars.setObjectName("lstPersonalAvailableChars")
        self.lstPersonalSelectedChars = QtGui.QListView(self.tabProjectPersonalCharacteristics)
        self.lstPersonalSelectedChars.setGeometry(QtCore.QRect(370, 30, 261, 361))
        self.lstPersonalSelectedChars.setObjectName("lstPersonalSelectedChars")
        self.cmdPersonalMoveAll = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdPersonalMoveAll.setObjectName("cmdPersonalMoveAll")
        self.cmdPersonalRemoveAll = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdPersonalRemoveAll.setObjectName("cmdPersonalRemoveAll")
        self.cmdPersonalMoveSelected = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdPersonalMoveSelected.setObjectName("cmdPersonalMoveSelected")
        self.cmdPersonalRemoveSelected = QtGui.QPushButton(self.tabProjectPersonalCharacteristics)
        self.cmdPersonalRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdPersonalRemoveSelected.setObjectName("cmdPersonalRemoveSelected")
        self.label_3 = QtGui.QLabel(self.tabProjectPersonalCharacteristics)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.tabProjectPersonalCharacteristics)
        self.label_4.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_4.setObjectName("label_4")
        self.tabProject.addTab(self.tabProjectPersonalCharacteristics, "")
        self.tabProjectHouseholdCharacteristics = QtGui.QWidget()
        self.tabProjectHouseholdCharacteristics.setObjectName("tabProjectHouseholdCharacteristics")
        self.cmdHouseholdMoveSelected = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdMoveSelected.setGeometry(QtCore.QRect(280, 210, 81, 31))
        self.cmdHouseholdMoveSelected.setObjectName("cmdHouseholdMoveSelected")
        self.cmdHouseholdRemoveSelected = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdRemoveSelected.setGeometry(QtCore.QRect(280, 250, 81, 31))
        self.cmdHouseholdRemoveSelected.setObjectName("cmdHouseholdRemoveSelected")
        self.label_5 = QtGui.QLabel(self.tabProjectHouseholdCharacteristics)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 171, 16))
        self.label_5.setObjectName("label_5")
        self.lstHouseholdAvailableChars = QtGui.QListView(self.tabProjectHouseholdCharacteristics)
        self.lstHouseholdAvailableChars.setGeometry(QtCore.QRect(10, 30, 261, 361))
        self.lstHouseholdAvailableChars.setObjectName("lstHouseholdAvailableChars")
        self.lstHouseholdSelectedChars = QtGui.QListView(self.tabProjectHouseholdCharacteristics)
        self.lstHouseholdSelectedChars.setGeometry(QtCore.QRect(370, 30, 261, 361))
        self.lstHouseholdSelectedChars.setObjectName("lstHouseholdSelectedChars")
        self.cmdHouseholdMoveAll = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdMoveAll.setGeometry(QtCore.QRect(280, 130, 81, 31))
        self.cmdHouseholdMoveAll.setObjectName("cmdHouseholdMoveAll")
        self.cmdHouseholdRemoveAll = QtGui.QPushButton(self.tabProjectHouseholdCharacteristics)
        self.cmdHouseholdRemoveAll.setGeometry(QtCore.QRect(280, 170, 81, 31))
        self.cmdHouseholdRemoveAll.setObjectName("cmdHouseholdRemoveAll")
        self.label_6 = QtGui.QLabel(self.tabProjectHouseholdCharacteristics)
        self.label_6.setGeometry(QtCore.QRect(380, 10, 211, 16))
        self.label_6.setObjectName("label_6")
        self.tabProject.addTab(self.tabProjectHouseholdCharacteristics, "")
        self.cmdClose = QtGui.QPushButton(ProjectConfiguration)
        self.cmdClose.setGeometry(QtCore.QRect(560, 480, 91, 31))
        self.cmdClose.setObjectName("cmdClose")

        self.retranslateUi(ProjectConfiguration)
        self.tabProject.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ProjectConfiguration)

    def retranslateUi(self, ProjectConfiguration):
        ProjectConfiguration.setWindowTitle(QtGui.QApplication.translate("ProjectConfiguration", "Project Configuration", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("ProjectConfiguration", "Project Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.lblProjectName.setText(QtGui.QApplication.translate("ProjectConfiguration", "{projectname}", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdPersonalRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabProjectPersonalCharacteristics), QtGui.QApplication.translate("ProjectConfiguration", "Personal Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdMoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", ">", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdRemoveSelected.setText(QtGui.QApplication.translate("ProjectConfiguration", "<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ProjectConfiguration", "Available Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdMoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", ">>", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdHouseholdRemoveAll.setText(QtGui.QApplication.translate("ProjectConfiguration", "<<", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ProjectConfiguration", "Selected Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.tabProject.setTabText(self.tabProject.indexOf(self.tabProjectHouseholdCharacteristics), QtGui.QApplication.translate("ProjectConfiguration", "Household Characteristics", None, QtGui.QApplication.UnicodeUTF8))
        self.cmdClose.setText(QtGui.QApplication.translate("ProjectConfiguration", "Close", None, QtGui.QApplication.UnicodeUTF8))
