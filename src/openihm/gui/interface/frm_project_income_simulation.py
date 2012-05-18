"""
This file is part of open-ihm.

open-ihm is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License as published by the
Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

open-ihm is distributed in the hope that it will be useful, but
WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
General Public License for more details.

You should have received a copy of the GNU General Public License
along with open-ihm.  If not, see <http://www.gnu.org/licenses/>.
"""


# imports from PyQt4 package
from datetime import date
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic
from data.config import Config
from control.controller import Controller
from mixins import MDIDialogMixin, TableViewMixin
from data.report_settingsmanager import ReportsSettingsManager
from frm_simulation_standardofliving_edit import FrmStandardOfLivingModelPrice
from frm_simulation_diet_edit import FrmDietModelPrice


Ui_HouseholdData, base_class = uic.loadUiType("gui/designs/ui_simulation.ui")

class FrmRunIncomeSimulation(QDialog, Ui_HouseholdData,MDIDialogMixin,TableViewMixin):
    
    ''' Creates the run simulations form '''	
    def __init__(self, parent, hhid=0):
        
	''' Set up the dialog box interface '''
	QDialog.__init__(self)
	self.setupUi(self)
	self.parent = parent
	self.stlitem = ""
	self.stlmodelprice = 0
	self.stlprice = 0
	
	self.connector = ReportsSettingsManager()
	self.getPorjects()
	self.insertDietHeader()
	self.insertStandardOfLivingHeader()

    def getPorjects(self):
        ''' populate projects combobox with available projects'''
                
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getProjectNames()

        for row in rows:
		project = row[0]
            	self.cmbProjects.addItem(project)

        self.cmbProjects.setCurrentIndex(-1)

    def getselectedProject(self):
        ''' get name of project selected by user'''
                
        selectedproject = self.cmbProjects.currentText()
        return selectedproject
                
    def getProjectID(self):

        ''' get ID for the selected project'''
                
        selectedproject = self.getselectedProject()
        if selectedproject !="":
                settingsmgr = ReportsSettingsManager()
                selectedprojectid = settingsmgr.getSelectedProjectID(selectedproject)
                return selectedprojectid
        else: return 0

    def insertDietHeader(self):
        '''Insert Title for treeViewHouseholds'''
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Food Type'))
        model.setHorizontalHeaderItem(1,QStandardItem('% in Diet'))
	model.setHorizontalHeaderItem(2,QStandardItem('Price'))
	model.setHorizontalHeaderItem(3,QStandardItem('Model Price'))

        self.tblDiets.setModel(model)
        self.tblDiets.show()	

    def insertStandardOfLivingHeader(self):
        '''Insert Title for listViewHCharacteristics'''
        
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Expense Type'))
	model.setHorizontalHeaderItem(1,QStandardItem('Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('Model Price'))
        
        self.tblStandardofLiving.setModel(model)
        self.tblStandardofLiving.show()	

    def getFoodEnergyRequirements(self):
        query = '''SELECT age, kCalNeedM, kCalNeedF FROM lookup_energy_needs'''
	recordset = self.executeResultsQuery(query)
	model = QStandardItemModel(1,2)
				
    def getProjectDiet(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        recordset = settingsmgr.getProjectDiet(projectid)
	model = QStandardItemModel(1,4)

	#set headers
	model.setHorizontalHeaderItem(0,QStandardItem('Food Type'))
        model.setHorizontalHeaderItem(1,QStandardItem('% in Diet'))
	model.setHorizontalHeaderItem(2,QStandardItem('Price'))
	model.setHorizontalHeaderItem(3,QStandardItem('Model Price'))
				
	# add  data rows
	num = 0
		    
	for row in recordset:
	    qtFood = QStandardItem( "%s" % row[0])
	    qtFood.setTextAlignment( Qt.AlignCenter )
		    
	    qtPercentage = QStandardItem( "%i" % row[1] )
	    qtPercentage.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    qtPricePerUnit = QStandardItem( "%i" % row[2] )
	    qtPricePerUnit.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    qtModelPrice = QStandardItem( "%i" % row[3] )
	    qtModelPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    model.setItem( num, 0, qtFood )
	    model.setItem( num, 1, qtPercentage )
	    model.setItem( num, 2, qtPricePerUnit )
	    model.setItem( num, 3, qtModelPrice )
	    num = num + 1
	    
	self.tblDiets.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblDiets.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblDiets.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblDiets.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblDiets.horizontalHeader().setResizeMode(3, QHeaderView.ResizeToContents)
	self.tblDiets.show()

    def getProjectStandardOfLiving(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        recordset = settingsmgr.getProjectStandardofLiving(projectid)
	model = QStandardItemModel(1,3)

	#set headers
        model.setHorizontalHeaderItem(0,QStandardItem('Expense Type'))
	model.setHorizontalHeaderItem(1,QStandardItem('Price'))
	model.setHorizontalHeaderItem(2,QStandardItem('Model Price'))
				
	# add  data rows
	num = 0
	for row in recordset:
	    qtItem = QStandardItem( "%s" % row[0])
	    qtItem.setTextAlignment( Qt.AlignCenter )
		    
	    qtPrice = QStandardItem( "%d" % row[1] )
	    qtPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )
		    
	    qtModelPrice = QStandardItem( "%d" % row[2] )
	    qtModelPrice.setTextAlignment( Qt.AlignRight | Qt.AlignVCenter )

	    model.setItem( num, 0, qtItem )
	    model.setItem( num, 1, qtPrice )
	    model.setItem( num, 2, qtModelPrice )
	    num = num + 1
	    
	self.tblStandardofLiving.setModel(model)
	#self.tableView.verticalHeader().hide()
        self.tblStandardofLiving.horizontalHeader().setResizeMode(0, QHeaderView.ResizeToContents)                                              
	self.tblStandardofLiving.horizontalHeader().setResizeMode(1, QHeaderView.ResizeToContents)
	self.tblStandardofLiving.horizontalHeader().setResizeMode(2, QHeaderView.ResizeToContents)
	self.tblStandardofLiving.show()
	
    def editDietPrice(self):
	if self.countRowsSelected(self.tblDiets) != 0:
	    # get the age of the selected record
	    selectedRow = self.getCurrentRow(self.tblDiets)
	    foodname = self.tblDiets.model().item(selectedRow,0).text()
	    percentageindiet = self.tblDiets.model().item(selectedRow,1).text()
	    unitprice = self.tblDiets.model().item(selectedRow,2).text()
	    modelprice = self.tblDiets.model().item(selectedRow,3).text()
	    projectid = self.getProjectID()

	    # show edit food energy requirement form
	    form = FrmDietModelPrice(self.parent,foodname,percentageindiet,unitprice,modelprice,projectid)
	    form.setWindowIcon(QIcon('resources/images/openihm.png'))
	    form.exec_()
	    self.getProjectDiet()
			
	else:
            
	    QMessageBox.information(self,"Edit Diet Model Value","Please select the row containing the model price to be edited.")

    def editStandardOfLiving(self):
	# get the age of the selected record
	if self.countRowsSelected(self.tblStandardofLiving) != 0:
            selectedRow = self.getCurrentRow(self.tblStandardofLiving)
            projectid = self.getProjectID()
            stlitem = self.tblStandardofLiving.model().item(selectedRow,0).text()
            stlprice = self.tblStandardofLiving.model().item(selectedRow,1).text()
            stlmodelprice = self.tblStandardofLiving.model().item(selectedRow,2).text()

            # show edit food energy requirement form
            form = FrmStandardOfLivingModelPrice(self.parent,stlitem, stlprice,stlmodelprice,projectid)
            form.setWindowIcon(QIcon('resources/images/openihm.png'))
            form.exec_()
            self.getProjectStandardOfLiving()
			
	else:
            
	    QMessageBox.information(self,"Edit Standard of Living Model Values","Please select the row containing the model price to be edited.")

