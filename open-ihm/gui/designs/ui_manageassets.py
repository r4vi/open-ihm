# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_manageassets.ui'
#
# Created: Tue Apr 19 08:09:03 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ManageAssetDetails(object):
    def setupUi(self, ManageAssetDetails):
        ManageAssetDetails.setObjectName(_fromUtf8("ManageAssetDetails"))
        ManageAssetDetails.resize(572, 424)
        ManageAssetDetails.setMinimumSize(QtCore.QSize(572, 380))
        self.tabWidget = QtGui.QTabWidget(ManageAssetDetails)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 571, 341))
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabCashSavings = QtGui.QWidget()
        self.tabCashSavings.setObjectName(_fromUtf8("tabCashSavings"))
        self.label_23 = QtGui.QLabel(self.tabCashSavings)
        self.label_23.setGeometry(QtCore.QRect(260, 60, 121, 18))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.btnCashDelete = QtGui.QPushButton(self.tabCashSavings)
        self.btnCashDelete.setGeometry(QtCore.QRect(480, 150, 80, 28))
        self.btnCashDelete.setObjectName(_fromUtf8("btnCashDelete"))
        self.txtSavingCategories = QtGui.QLineEdit(self.tabCashSavings)
        self.txtSavingCategories.setGeometry(QtCore.QRect(372, 60, 181, 28))
        self.txtSavingCategories.setObjectName(_fromUtf8("txtSavingCategories"))
        self.label_25 = QtGui.QLabel(self.tabCashSavings)
        self.label_25.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.tabCashSavings)
        self.label_26.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.btnCashSave = QtGui.QPushButton(self.tabCashSavings)
        self.btnCashSave.setGeometry(QtCore.QRect(370, 150, 80, 28))
        self.btnCashSave.setObjectName(_fromUtf8("btnCashSave"))
        self.savingsListView = QtGui.QListView(self.tabCashSavings)
        self.savingsListView.setGeometry(QtCore.QRect(5, 60, 241, 201))
        self.savingsListView.setObjectName(_fromUtf8("savingsListView"))
        self.tabWidget.addTab(self.tabCashSavings, _fromUtf8(""))
        self.tabFoodStock = QtGui.QWidget()
        self.tabFoodStock.setObjectName(_fromUtf8("tabFoodStock"))
        self.txtFoodStockType = QtGui.QLineEdit(self.tabFoodStock)
        self.txtFoodStockType.setGeometry(QtCore.QRect(352, 60, 201, 28))
        self.txtFoodStockType.setObjectName(_fromUtf8("txtFoodStockType"))
        self.txtEnergyValue = QtGui.QLineEdit(self.tabFoodStock)
        self.txtEnergyValue.setGeometry(QtCore.QRect(350, 110, 201, 28))
        self.txtEnergyValue.setObjectName(_fromUtf8("txtEnergyValue"))
        self.btnFoodStockSave = QtGui.QPushButton(self.tabFoodStock)
        self.btnFoodStockSave.setGeometry(QtCore.QRect(350, 240, 80, 28))
        self.btnFoodStockSave.setObjectName(_fromUtf8("btnFoodStockSave"))
        self.btnFoodStockDelete = QtGui.QPushButton(self.tabFoodStock)
        self.btnFoodStockDelete.setGeometry(QtCore.QRect(460, 240, 80, 28))
        self.btnFoodStockDelete.setObjectName(_fromUtf8("btnFoodStockDelete"))
        self.label_3 = QtGui.QLabel(self.tabFoodStock)
        self.label_3.setGeometry(QtCore.QRect(260, 60, 54, 18))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_5 = QtGui.QLabel(self.tabFoodStock)
        self.label_5.setGeometry(QtCore.QRect(260, 120, 54, 18))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tabFoodStock)
        self.label_6.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_16 = QtGui.QLabel(self.tabFoodStock)
        self.label_16.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.txtMeasuringUnit = QtGui.QLineEdit(self.tabFoodStock)
        self.txtMeasuringUnit.setGeometry(QtCore.QRect(350, 160, 201, 31))
        self.txtMeasuringUnit.setObjectName(_fromUtf8("txtMeasuringUnit"))
        self.label_4 = QtGui.QLabel(self.tabFoodStock)
        self.label_4.setGeometry(QtCore.QRect(260, 170, 81, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.foodListView = QtGui.QListView(self.tabFoodStock)
        self.foodListView.setGeometry(QtCore.QRect(10, 50, 241, 201))
        self.foodListView.setObjectName(_fromUtf8("foodListView"))
        self.tabWidget.addTab(self.tabFoodStock, _fromUtf8(""))
        self.tabLand = QtGui.QWidget()
        self.tabLand.setObjectName(_fromUtf8("tabLand"))
        self.txtLandType = QtGui.QLineEdit(self.tabLand)
        self.txtLandType.setGeometry(QtCore.QRect(352, 60, 201, 28))
        self.txtLandType.setObjectName(_fromUtf8("txtLandType"))
        self.btnLandSave = QtGui.QPushButton(self.tabLand)
        self.btnLandSave.setGeometry(QtCore.QRect(350, 240, 80, 28))
        self.btnLandSave.setObjectName(_fromUtf8("btnLandSave"))
        self.label_7 = QtGui.QLabel(self.tabLand)
        self.label_7.setGeometry(QtCore.QRect(260, 60, 54, 18))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.tabLand)
        self.label_8.setGeometry(QtCore.QRect(260, 120, 91, 18))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.txtLandMeasuringUnit = QtGui.QLineEdit(self.tabLand)
        self.txtLandMeasuringUnit.setGeometry(QtCore.QRect(350, 110, 201, 28))
        self.txtLandMeasuringUnit.setObjectName(_fromUtf8("txtLandMeasuringUnit"))
        self.label_17 = QtGui.QLabel(self.tabLand)
        self.label_17.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.btnLandDelete = QtGui.QPushButton(self.tabLand)
        self.btnLandDelete.setGeometry(QtCore.QRect(460, 240, 80, 28))
        self.btnLandDelete.setObjectName(_fromUtf8("btnLandDelete"))
        self.label_18 = QtGui.QLabel(self.tabLand)
        self.label_18.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.landListView = QtGui.QListView(self.tabLand)
        self.landListView.setGeometry(QtCore.QRect(5, 50, 241, 201))
        self.landListView.setObjectName(_fromUtf8("landListView"))
        self.tabWidget.addTab(self.tabLand, _fromUtf8(""))
        self.tabLivestock = QtGui.QWidget()
        self.tabLivestock.setObjectName(_fromUtf8("tabLivestock"))
        self.txtLivestockEnergyValue = QtGui.QLineEdit(self.tabLivestock)
        self.txtLivestockEnergyValue.setGeometry(QtCore.QRect(350, 110, 201, 28))
        self.txtLivestockEnergyValue.setObjectName(_fromUtf8("txtLivestockEnergyValue"))
        self.label_9 = QtGui.QLabel(self.tabLivestock)
        self.label_9.setGeometry(QtCore.QRect(260, 170, 81, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.tabLivestock)
        self.label_11.setGeometry(QtCore.QRect(260, 120, 54, 18))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.txtLivestockUnit = QtGui.QLineEdit(self.tabLivestock)
        self.txtLivestockUnit.setGeometry(QtCore.QRect(350, 160, 201, 31))
        self.txtLivestockUnit.setObjectName(_fromUtf8("txtLivestockUnit"))
        self.label_24 = QtGui.QLabel(self.tabLivestock)
        self.label_24.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.btnLivestockDelete = QtGui.QPushButton(self.tabLivestock)
        self.btnLivestockDelete.setGeometry(QtCore.QRect(460, 240, 80, 28))
        self.btnLivestockDelete.setObjectName(_fromUtf8("btnLivestockDelete"))
        self.livestockListView = QtGui.QListView(self.tabLivestock)
        self.livestockListView.setGeometry(QtCore.QRect(10, 50, 241, 201))
        self.livestockListView.setObjectName(_fromUtf8("livestockListView"))
        self.txtLivestockPType = QtGui.QLineEdit(self.tabLivestock)
        self.txtLivestockPType.setGeometry(QtCore.QRect(352, 60, 201, 28))
        self.txtLivestockPType.setObjectName(_fromUtf8("txtLivestockPType"))
        self.btnLivestockSave = QtGui.QPushButton(self.tabLivestock)
        self.btnLivestockSave.setGeometry(QtCore.QRect(350, 240, 80, 28))
        self.btnLivestockSave.setObjectName(_fromUtf8("btnLivestockSave"))
        self.label_14 = QtGui.QLabel(self.tabLivestock)
        self.label_14.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_27 = QtGui.QLabel(self.tabLivestock)
        self.label_27.setGeometry(QtCore.QRect(260, 60, 54, 18))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.tabWidget.addTab(self.tabLivestock, _fromUtf8(""))
        self.tabTrees = QtGui.QWidget()
        self.tabTrees.setObjectName(_fromUtf8("tabTrees"))
        self.label_10 = QtGui.QLabel(self.tabTrees)
        self.label_10.setGeometry(QtCore.QRect(260, 60, 54, 18))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.btnTreeDelete = QtGui.QPushButton(self.tabTrees)
        self.btnTreeDelete.setGeometry(QtCore.QRect(460, 240, 80, 28))
        self.btnTreeDelete.setObjectName(_fromUtf8("btnTreeDelete"))
        self.txtTreeType = QtGui.QLineEdit(self.tabTrees)
        self.txtTreeType.setGeometry(QtCore.QRect(352, 60, 201, 28))
        self.txtTreeType.setObjectName(_fromUtf8("txtTreeType"))
        self.label_19 = QtGui.QLabel(self.tabTrees)
        self.label_19.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.txtTreeMeasuringUnit = QtGui.QLineEdit(self.tabTrees)
        self.txtTreeMeasuringUnit.setGeometry(QtCore.QRect(350, 110, 201, 28))
        self.txtTreeMeasuringUnit.setObjectName(_fromUtf8("txtTreeMeasuringUnit"))
        self.label_20 = QtGui.QLabel(self.tabTrees)
        self.label_20.setGeometry(QtCore.QRect(0, 10, 221, 18))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_12 = QtGui.QLabel(self.tabTrees)
        self.label_12.setGeometry(QtCore.QRect(260, 120, 91, 18))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.btnTreeSave = QtGui.QPushButton(self.tabTrees)
        self.btnTreeSave.setGeometry(QtCore.QRect(350, 240, 80, 28))
        self.btnTreeSave.setObjectName(_fromUtf8("btnTreeSave"))
        self.treeListView = QtGui.QListView(self.tabTrees)
        self.treeListView.setGeometry(QtCore.QRect(5, 50, 241, 201))
        self.treeListView.setObjectName(_fromUtf8("treeListView"))
        self.tabWidget.addTab(self.tabTrees, _fromUtf8(""))
        self.tabOtherTradableGoods = QtGui.QWidget()
        self.tabOtherTradableGoods.setObjectName(_fromUtf8("tabOtherTradableGoods"))
        self.label_13 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_13.setGeometry(QtCore.QRect(260, 60, 54, 18))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.btnTGoodDelete = QtGui.QPushButton(self.tabOtherTradableGoods)
        self.btnTGoodDelete.setGeometry(QtCore.QRect(460, 240, 80, 28))
        self.btnTGoodDelete.setObjectName(_fromUtf8("btnTGoodDelete"))
        self.txtTradableGoodType = QtGui.QLineEdit(self.tabOtherTradableGoods)
        self.txtTradableGoodType.setGeometry(QtCore.QRect(352, 60, 201, 28))
        self.txtTradableGoodType.setObjectName(_fromUtf8("txtTradableGoodType"))
        self.label_21 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_21.setGeometry(QtCore.QRect(290, 10, 241, 18))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.txtTradableGoodMeasuringUnit = QtGui.QLineEdit(self.tabOtherTradableGoods)
        self.txtTradableGoodMeasuringUnit.setGeometry(QtCore.QRect(350, 110, 201, 28))
        self.txtTradableGoodMeasuringUnit.setObjectName(_fromUtf8("txtTradableGoodMeasuringUnit"))
        self.label_22 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_22.setGeometry(QtCore.QRect(10, 10, 221, 18))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_15 = QtGui.QLabel(self.tabOtherTradableGoods)
        self.label_15.setGeometry(QtCore.QRect(260, 120, 91, 18))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.btnTGoodSave = QtGui.QPushButton(self.tabOtherTradableGoods)
        self.btnTGoodSave.setGeometry(QtCore.QRect(350, 240, 80, 28))
        self.btnTGoodSave.setObjectName(_fromUtf8("btnTGoodSave"))
        self.tradableGoodsListView = QtGui.QListView(self.tabOtherTradableGoods)
        self.tradableGoodsListView.setGeometry(QtCore.QRect(0, 50, 251, 192))
        self.tradableGoodsListView.setObjectName(_fromUtf8("tradableGoodsListView"))
        self.tabWidget.addTab(self.tabOtherTradableGoods, _fromUtf8(""))
        self.btnAssetsClose = QtGui.QPushButton(ManageAssetDetails)
        self.btnAssetsClose.setGeometry(QtCore.QRect(490, 350, 80, 28))
        self.btnAssetsClose.setObjectName(_fromUtf8("btnAssetsClose"))

        self.retranslateUi(ManageAssetDetails)
        self.tabWidget.setCurrentIndex(5)
        QtCore.QObject.connect(self.savingsListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageAssetDetails.pickSelectedSaving)
        QtCore.QObject.connect(self.btnCashSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.saveSavingsType)
        QtCore.QObject.connect(self.btnCashDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteSavingsType)
        QtCore.QObject.connect(self.foodListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageAssetDetails.pickSelectedFoodItem)
        QtCore.QObject.connect(self.btnFoodStockSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.saveFoodStockType)
        QtCore.QObject.connect(self.btnFoodStockDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteFoodStockType)
        QtCore.QObject.connect(self.landListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageAssetDetails.pickSelectedLandType)
        QtCore.QObject.connect(self.btnLandSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.saveLandType)
        QtCore.QObject.connect(self.btnLandDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteLandType)
        QtCore.QObject.connect(self.livestockListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageAssetDetails.pickSelectedLivestockItem)
        QtCore.QObject.connect(self.btnLivestockSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.saveLivestockType)
        QtCore.QObject.connect(self.btnLivestockDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteLivestockType)
        QtCore.QObject.connect(self.treeListView, QtCore.SIGNAL(_fromUtf8("activated(QModelIndex)")), ManageAssetDetails.pickSelectedTreeType)
        QtCore.QObject.connect(self.btnTreeSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.pickSelectedTreeType)
        QtCore.QObject.connect(self.btnTreeDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteTreeType)
        QtCore.QObject.connect(self.btnTGoodDelete, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.deleteTradableGoodType)
        QtCore.QObject.connect(self.btnTGoodSave, QtCore.SIGNAL(_fromUtf8("clicked()")), ManageAssetDetails.saveTradableGoodType)
        QtCore.QObject.connect(self.tradableGoodsListView, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), ManageAssetDetails.pickSelectedTradableGoodType)
        QtCore.QMetaObject.connectSlotsByName(ManageAssetDetails)
        ManageAssetDetails.setTabOrder(self.txtSavingCategories, self.btnCashDelete)
        ManageAssetDetails.setTabOrder(self.btnCashDelete, self.tabWidget)
        ManageAssetDetails.setTabOrder(self.tabWidget, self.savingsListView)
        ManageAssetDetails.setTabOrder(self.savingsListView, self.btnCashSave)
        ManageAssetDetails.setTabOrder(self.btnCashSave, self.btnAssetsClose)
        ManageAssetDetails.setTabOrder(self.btnAssetsClose, self.txtFoodStockType)
        ManageAssetDetails.setTabOrder(self.txtFoodStockType, self.txtEnergyValue)
        ManageAssetDetails.setTabOrder(self.txtEnergyValue, self.btnFoodStockSave)
        ManageAssetDetails.setTabOrder(self.btnFoodStockSave, self.btnFoodStockDelete)
        ManageAssetDetails.setTabOrder(self.btnFoodStockDelete, self.txtMeasuringUnit)
        ManageAssetDetails.setTabOrder(self.txtMeasuringUnit, self.foodListView)
        ManageAssetDetails.setTabOrder(self.foodListView, self.txtLandType)
        ManageAssetDetails.setTabOrder(self.txtLandType, self.btnLandSave)
        ManageAssetDetails.setTabOrder(self.btnLandSave, self.txtLandMeasuringUnit)
        ManageAssetDetails.setTabOrder(self.txtLandMeasuringUnit, self.btnLandDelete)
        ManageAssetDetails.setTabOrder(self.btnLandDelete, self.landListView)
        ManageAssetDetails.setTabOrder(self.landListView, self.txtLivestockEnergyValue)
        ManageAssetDetails.setTabOrder(self.txtLivestockEnergyValue, self.txtLivestockUnit)
        ManageAssetDetails.setTabOrder(self.txtLivestockUnit, self.btnLivestockDelete)
        ManageAssetDetails.setTabOrder(self.btnLivestockDelete, self.livestockListView)
        ManageAssetDetails.setTabOrder(self.livestockListView, self.txtLivestockPType)
        ManageAssetDetails.setTabOrder(self.txtLivestockPType, self.btnLivestockSave)
        ManageAssetDetails.setTabOrder(self.btnLivestockSave, self.btnTreeDelete)
        ManageAssetDetails.setTabOrder(self.btnTreeDelete, self.txtTreeType)
        ManageAssetDetails.setTabOrder(self.txtTreeType, self.txtTreeMeasuringUnit)
        ManageAssetDetails.setTabOrder(self.txtTreeMeasuringUnit, self.btnTreeSave)
        ManageAssetDetails.setTabOrder(self.btnTreeSave, self.treeListView)
        ManageAssetDetails.setTabOrder(self.treeListView, self.btnTGoodDelete)
        ManageAssetDetails.setTabOrder(self.btnTGoodDelete, self.txtTradableGoodType)
        ManageAssetDetails.setTabOrder(self.txtTradableGoodType, self.txtTradableGoodMeasuringUnit)
        ManageAssetDetails.setTabOrder(self.txtTradableGoodMeasuringUnit, self.btnTGoodSave)
        ManageAssetDetails.setTabOrder(self.btnTGoodSave, self.tradableGoodsListView)

    def retranslateUi(self, ManageAssetDetails):
        ManageAssetDetails.setWindowTitle(QtGui.QApplication.translate("ManageAssetDetails", "Manage Asset Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("ManageAssetDetails", "Cash Saving Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCashDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Cash Saving Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Cash Saving Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCashSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCashSavings), QtGui.QApplication.translate("ManageAssetDetails", "Cash Savings", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFoodStockSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.btnFoodStockDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("ManageAssetDetails", "KCalories", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Food Stock Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Food Stock Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabFoodStock), QtGui.QApplication.translate("ManageAssetDetails", "Food Stock", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLandSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Land Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLandDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Land Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLand), QtGui.QApplication.translate("ManageAssetDetails", "Land", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("ManageAssetDetails", "KCalories", None, QtGui.QApplication.UnicodeUTF8))
        self.label_24.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Livestocktock Details", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLivestockDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.btnLivestockSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Livetock Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabLivestock), QtGui.QApplication.translate("ManageAssetDetails", "Livestock", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTreeDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Tree Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Tree Type", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTreeSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTrees), QtGui.QApplication.translate("ManageAssetDetails", "Trees", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("ManageAssetDetails", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTGoodDelete.setText(QtGui.QApplication.translate("ManageAssetDetails", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("ManageAssetDetails", "Add/ Edit Good Details", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("ManageAssetDetails", "Select Good", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("ManageAssetDetails", "Unit of Measure", None, QtGui.QApplication.UnicodeUTF8))
        self.btnTGoodSave.setText(QtGui.QApplication.translate("ManageAssetDetails", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabOtherTradableGoods), QtGui.QApplication.translate("ManageAssetDetails", "Tradable Goods", None, QtGui.QApplication.UnicodeUTF8))
        self.btnAssetsClose.setText(QtGui.QApplication.translate("ManageAssetDetails", "Close", None, QtGui.QApplication.UnicodeUTF8))

