# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_managecroptypes.ui'
#
# Created: Fri Mar  5 09:48:21 2010
#      by: PyQt4 UI code generator 4.3.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_CropTypes(object):
    def setupUi(self, CropTypes):
        CropTypes.setObjectName("CropTypes")
        CropTypes.resize(QtCore.QSize(QtCore.QRect(0,0,389,270).size()).expandedTo(CropTypes.minimumSizeHint()))
        CropTypes.setMinimumSize(QtCore.QSize(389,261))

        self.btnManageCropsClose = QtGui.QPushButton(CropTypes)
        self.btnManageCropsClose.setGeometry(QtCore.QRect(270,220,80,28))
        self.btnManageCropsClose.setObjectName("btnManageCropsClose")

        self.pushButton_3 = QtGui.QPushButton(CropTypes)
        self.pushButton_3.setGeometry(QtCore.QRect(40,220,80,28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.comboBox = QtGui.QComboBox(CropTypes)
        self.comboBox.setGeometry(QtCore.QRect(120,10,221,27))
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtGui.QComboBox(CropTypes)
        self.comboBox_2.setGeometry(QtCore.QRect(120,50,221,27))
        self.comboBox_2.setObjectName("comboBox_2")

        self.label = QtGui.QLabel(CropTypes)
        self.label.setGeometry(QtCore.QRect(10,10,54,18))
        self.label.setObjectName("label")

        self.label_2 = QtGui.QLabel(CropTypes)
        self.label_2.setGeometry(QtCore.QRect(10,60,61,18))
        self.label_2.setObjectName("label_2")

        self.comboBox_3 = QtGui.QComboBox(CropTypes)
        self.comboBox_3.setGeometry(QtCore.QRect(120,90,131,27))
        self.comboBox_3.setObjectName("comboBox_3")

        self.label_3 = QtGui.QLabel(CropTypes)
        self.label_3.setGeometry(QtCore.QRect(10,100,91,18))
        self.label_3.setObjectName("label_3")

        self.comboBox_4 = QtGui.QComboBox(CropTypes)
        self.comboBox_4.setGeometry(QtCore.QRect(120,130,131,27))
        self.comboBox_4.setObjectName("comboBox_4")

        self.label_4 = QtGui.QLabel(CropTypes)
        self.label_4.setGeometry(QtCore.QRect(10,130,101,18))
        self.label_4.setObjectName("label_4")

        self.lineEdit = QtGui.QLineEdit(CropTypes)
        self.lineEdit.setGeometry(QtCore.QRect(120,170,131,28))
        self.lineEdit.setObjectName("lineEdit")

        self.label_5 = QtGui.QLabel(CropTypes)
        self.label_5.setGeometry(QtCore.QRect(10,180,81,18))
        self.label_5.setObjectName("label_5")

        self.pushButton = QtGui.QPushButton(CropTypes)
        self.pushButton.setGeometry(QtCore.QRect(160,220,80,28))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(CropTypes)
        QtCore.QMetaObject.connectSlotsByName(CropTypes)

    def retranslateUi(self, CropTypes):
        CropTypes.setWindowTitle(QtGui.QApplication.translate("CropTypes", "Manage Crop Types", None, QtGui.QApplication.UnicodeUTF8))
        self.btnManageCropsClose.setText(QtGui.QApplication.translate("CropTypes", "Close", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("CropTypes", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("CropTypes", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("CropTypes", "Data Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("CropTypes", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("CropTypes", "Kcals per unit", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("CropTypes", "Price per Unit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("CropTypes", "Delete", None, QtGui.QApplication.UnicodeUTF8))

