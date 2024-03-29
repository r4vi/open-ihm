#!/usr/bin/env python

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
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

# import the Manage Income Dialog design class
Ui_ManageIncome, base_class = uic.loadUiType("gui/designs/ui_manageincomedetails.ui")


from mixins import MDIDialogMixin, MySQLMixin

class FrmIncomeSourceDetails(QDialog, Ui_ManageIncome, MySQLMixin, MDIDialogMixin):	
	''' Creates the Manage Income Source Details from. Uses the design class
		in gui.designs.ui_manageincomedetails. '''	
	def __init__(self, parent):
		''' Set up the dialog box interface '''
		self.parent = parent
        	QDialog.__init__(self)
       		self.setupUi(self)
        	self.parent = parent

		self.getCropTypes()
		self.getEmploymentCategories()
		self.getWildFoodTypes()
		self.getLivestockTypes()
		self.getTransferSourceCategories()
		self.getTransferTypes()

		#set input validator and restrict input to numeric values,
                myIntVal = QIntValidator(0, 10000, self.txtEnergyValue)
                                
                self.txtEnergyValue.setValidator(myIntVal)
                self.txtLivestockEnergyValue.setValidator(myIntVal)
                self.txtWildFoodEnergyValue.setValidator(myIntVal)

        #Begin block of methods for managing Foodstock details
	def clearCropTextboxes(self):
                self.txtCropTypeName.clear()
        	self.txtEnergyValue.clear()
        	self.txtMeasuringUnit.clear()
        	
	def getCropTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT name FROM setup_foods_crops WHERE category='crops' '''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.cropListView.setModel(model)
		self.cropListView.show()	

        def pickselectedCropItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedCropItem = self.cropListView.model().item(index.row(),0).text()
                self.txtCropTypeName.setText(selectedCropItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (selectedCropItem)

		rowset = self.executeResultsQuery(query)
	      		
		for row in rowset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtEnergyValue.setText(str(kcalValue))
                self.txtMeasuringUnit.setText(str(unitOfMeasure))

        def saveCropType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myfoodtype = self.txtCropTypeName.text()
        	myenergyvalue = self.txtEnergyValue.text()
        	unitofmeasure = self.txtMeasuringUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myfoodtype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = len(recordset)
		category='crops'
				      	
		if numrows == 0:
                        query = '''INSERT INTO setup_foods_crops(name, category,energyvalueperunit, unitofmeasure) 
                     		VALUES('%s','%s',%s,'%s')''' % (myfoodtype,category, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_foods_crops SET name='%s', category ='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     		WHERE name='%s' ''' % (myfoodtype, category, myenergyvalue, unitofmeasure, myfoodtype)
			
        	# execute query and commit changes
		self.executeUpdateQuery(query)
		#refresh categories list
		self.getCropTypes()
		self.clearCropTextboxes()
                                
	def deleteCropType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myfoodtype = self.txtCropTypeName.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myfoodtype)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)

		if numrows <> 0:
                        			
                        msg = "Are sure sure you want to delete this record?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_foods_crops WHERE name='%s' ''' % (myfoodtype)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)
			
                                #self.cmbKCalories.clear()
			
                                #refresh categories list
                                self.getCropTypes()
                                self.clearCropTextboxes()
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Crop Types

	#Begin block of methods for managing Employment Categories 	
	def getEmploymentCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT incomesource FROM setup_employment'''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtEmploymentType = QStandardItem( "%s" % row[0])
            		qtEmploymentType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtEmploymentType )
            		num = num + 1
                        		
        	self.employmentListView.setModel(model)
		self.employmentListView.show()

        def pickSelectedEmployment(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.employmentListView.model().item(index.row(),0).text()
                self.txtEmploymentType.setText(selectedItem)
                
        def saveEmploymentType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	employment = self.txtEmploymentType.text()		
        	
		# check if record exists
		query = '''SELECT incomesource FROM setup_employment WHERE incomesource='%s' ''' % (employment)    
		
                recordset = self.executeResultsQuery(query)

		numrows = len(recordset)
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_employment(incomesource) 
                     		VALUES('%s')''' % (employment)
		else:
			query = '''UPDATE setup_employment SET incomesource='%s'	WHERE incomesource='%s' ''' % (employment, employment)
    
                self.executeUpdateQuery(query)
		#refresh categories list
                self.txtEmploymentType.clear()
		self.getEmploymentCategories()               
                
	def deleteEmploymentType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	employment = self.txtEmploymentType.text()		
        	
		# check if record exists
		query = '''SELECT incomesource FROM setup_employment WHERE incomesource='%s' ''' % (employment)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)	

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Employment Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_employment WHERE incomesource='%s' ''' % (employment)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)
                                self.txtEmploymentType.clear()
                                #refresh categories list
                                self.getEmploymentCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Employment Categories


        #Begin block of methods for managing Wild Foods details
	def clearWildFoodTextboxes(self):
                self.txtWildFoodType.clear()
        	self.txtWildFoodEnergyValue.clear()
        	self.txtWildFoodUnit.clear()
        	
	def getWildFoodTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT name FROM setup_foods_crops WHERE category='wildfoods' '''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.wildFoodsListView.setModel(model)
		self.wildFoodsListView.show()	

        def pickselectedWildFoodItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedWildFoodItem = self.wildFoodsListView.model().item(index.row(),0).text()
                self.txtWildFoodType.setText(selectedWildFoodItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (selectedWildFoodItem)

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtWildFoodEnergyValue.setText(str(kcalValue))
                self.txtWildFoodUnit.setText(str(unitOfMeasure))

        def saveWildFoodType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myincomesource = self.txtWildFoodType.text()
        	myenergyvalue = self.txtWildFoodEnergyValue.text()
        	unitofmeasure = self.txtWildFoodUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)    
		
		recordset = self.executeResultsQuery(query)
		numrows = len(recordset)
		category ='wildfoods'
				      	
		if numrows == 0:
                        query = '''INSERT INTO setup_foods_crops(name, category,energyvalueperunit, unitofmeasure) 
                     		VALUES('%s','%s',%s,'%s')''' % (myincomesource,category, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_foods_crops SET name='%s', category ='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     		WHERE name='%s' ''' % (myincomesource, category, myenergyvalue, unitofmeasure, myincomesource)
			
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
		#refresh categories list
		self.getWildFoodTypes()
		self.clearWildFoodTextboxes()
                                
	def deleteWildFoodType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myincomesource = self.txtWildFoodType.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Food Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)
                                #refresh categories list
                                self.getWildFoodTypes()
                                self.clearWildFoodTextboxes()
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing WildFood Types
			

        #Begin block of methods for managing Livestock details

	def clearLivestockTextboxes(self):
                self.txtLivestockPType.clear()
        	self.txtLivestockEnergyValue.clear()
        	self.txtLivestockUnit.clear()
        	
	def getLivestockTypes(self):
                '''Get pre-existing savings categories from database and populate categories list'''
               	# select query to retrieve Food types
        	query = '''SELECT name FROM setup_foods_crops WHERE category='livestock' '''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtFoodType = QStandardItem( "%s" % row[0])
            		qtFoodType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtFoodType )
            		num = num + 1
                        		
        	self.livestockListView.setModel(model)
		self.livestockListView.show()	

        def pickselectedLivestockItem(self,index):
                '''get selected item and populate categories textbox'''
                
                selectedLivestockItem = self.livestockListView.model().item(index.row(),0).text()
                self.txtLivestockPType.setText(selectedLivestockItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
        	query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (selectedLivestockItem)

                recordset = self.executeResultsQuery(query)
	      		
		for row in recordset:
                        kcalValue = row[0]
			unitOfMeasure = row[1]

		self.txtLivestockEnergyValue.setText(str(kcalValue))
                self.txtLivestockUnit.setText(str(unitOfMeasure))

        def saveLivestockType(self):
        	''' Saves newly created data to database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()
        	myenergyvalue = self.txtLivestockEnergyValue.text()
        	unitofmeasure = self.txtLivestockUnit.text()
                        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)    
		
                recordset = self.executeResultsQuery(query)

		numrows = len(recordset)
		category = 'livestock'
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_foods_crops(name, category,energyvalueperunit, unitofmeasure) 
                     		VALUES('%s','%s',%s,'%s')''' % (myincomesource,category, myenergyvalue, unitofmeasure)
		else:
			query = '''UPDATE setup_foods_crops SET name='%s', category ='%s', energyvalueperunit=%s, unitofmeasure='%s'
                     		WHERE name='%s' ''' % (myincomesource, category, myenergyvalue, unitofmeasure, myincomesource)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
		#refresh categories list
		self.getLivestockTypes()

		self.clearLivestockTextboxes()
                                
	def deleteLivestockType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	myincomesource = self.txtLivestockPType.text()		
        	
		# check if record exists
		query = '''SELECT energyvalueperunit, unitofmeasure FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Livestock Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_foods_crops WHERE name='%s' ''' % (myincomesource)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)
                                #refresh categories list
                                self.getLivestockTypes()

                                self.clearLivestockTextboxes()
			
		else:
			QMessageBox.information(self, 'Delete Food Type', "Record not found")
        #End block of methods for managing Livestock Types

	#Begin block of methods for managing Transfer Source Categories	
	def getTransferSourceCategories(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Asset Categories
        	query = '''SELECT sourceoftransfer FROM setup_transfers WHERE assistancetype='EXTERNAL' '''
        	recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtTransferSourceType = QStandardItem(row[0])
            		qtTransferSourceType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtTransferSourceType )
            		num = num + 1
                        		
        	self.transferSourcesListView.setModel(model)
		self.transferSourcesListView.show()

        def pickSelectedTransferSource(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.transferSourcesListView.model().item(index.row(),0).text()
                self.txtTransferSources.setText(selectedItem)
                #select query to retrieve food-energy value and measuring unit for selected food item 
                
        def saveTransferSourceType(self):
        	''' Saves newly created data to database '''
        	# get the data entered by user
        	mytransfertype = self.txtTransferSources.text()
		# check if record exists
		query = '''SELECT sourceoftransfer FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='EXTERNAL' ''' % (mytransfertype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = len(recordset)
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_transfers(assistancetype,sourceoftransfer) 
                     		VALUES('EXTERNAL','%s')''' % (mytransfertype)
		else:
			query = '''UPDATE setup_transfers SET sourceoftransfer='%s' WHERE sourceoftransfer='%s'
                                AND assistancetype='EXTERNAL' ''' % (mytransfertype, mytransfertype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
                self.txtTransferSources.clear()
		#refresh categories list
		self.getTransferSourceCategories()              

                
	def deleteTransferSourceType(self):
		''' Deletes record from database '''

        	# get the data entered by user
        	mytransfersource = self.txtTransferSources.text()		
        	
		# check if record exists
		query = '''SELECT sourceoftransfer FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='EXTERNAL' ''' % (mytransfersource)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this Transfer Source Type?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='EXTERNAL' ''' % (mytransfersource)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)			
                                self.txtTransferSources.clear()
                                #refresh categories list
                                self.getTransferSourceCategories()			
			
		else:
			QMessageBox.information(self, 'Delete Transfer Source', "Record not found")
        #End block of methods for managing Transfer Source Categories

	#Begin block of methods for managing Transfer Types	
	def getTransferTypes(self):
                '''Get pre-existing assets categories from database and populate categories list'''
               	# select query to retrieve Social Transfer Sources
        	query = '''SELECT sourceoftransfer FROM setup_transfers WHERE assistancetype='INTERNAL' '''
        	
                recordset = self.executeResultsQuery(query)
				
		model = QStandardItemModel()
		num = 0

       		for row in recordset:
			qtTransferType = QStandardItem( "%s" % str(row[0]))
            		qtTransferType.setTextAlignment( Qt.AlignLeft )
            		model.setItem( num, 0, qtTransferType )
            		num = num + 1
                        		
        	self.transferTypesListView.setModel(model)
		self.transferTypesListView.show()

        def pickSelectedTransfer(self,index):
                '''get selected item and populate categories textbox'''
                selectedItem = self.transferTypesListView.model().item(index.row(),0).text()
                self.txtTransferType.setText(selectedItem)

                #select query to retrieve food-energy value and measuring unit for selected food item 
                
        def saveTransferType(self):
        	''' Saves newly created official transfer to database '''

        	# get the data entered by user
        	mytransfertype = self.txtTransferType.text()
		# check if record exists
		query = '''SELECT sourceoftransfer FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='INTERNAL' ''' % (mytransfertype)    
		
                recordset = self.executeResultsQuery(query)

		numrows = len(recordset)
				      	
		if numrows == 0:
			
			query = '''INSERT INTO setup_transfers(assistancetype,sourceoftransfer) 
                     		VALUES('INTERNAL','%s')''' % (mytransfertype)
		else:
			query = '''UPDATE setup_transfers SET sourceoftransfer='%s' WHERE sourceoftransfer='%s'
                                        AND assistancetype='INTERNAL' ''' % (mytransfertype, mytransfertype)
    
        	# execute query and commit changes
                self.executeUpdateQuery(query)
                self.txtTransferType.clear()
		#refresh categories list
		self.getTransferTypes()               
                
	def deleteTransferType(self):
		''' Deletes Transfer Type record from database '''

        	# get the data entered by user
        	mytransfertype = self.txtTransferType.text()		
        	
		# check if record exists
		query = '''SELECT sourceoftransfer FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='INTERNAL' ''' % (mytransfertype)    
		
                recordset = self.executeResultsQuery(query)
		numrows = len(recordset)

		if numrows <> 0:
			
                        msg = "Are sure sure you want to delete this record?"
                        ret = QMessageBox.question(self,"Confirm Deletion", msg, QMessageBox.Yes|QMessageBox.No)
                        if ret == QMessageBox.Yes:

                                query = '''DELETE FROM setup_transfers WHERE sourceoftransfer='%s' AND assistancetype='INTERNAL' ''' % (mytransfertype)

                                # execute query and commit changes
                                self.executeUpdateQuery(query)

                                #refresh categories list
                                self.getTransferTypes()
                                self.txtTransferType.clear()
			
		else:
			QMessageBox.information(self, 'Delete Transfer Type', "Record not found")
        #End block of methods for managing Transfer Types
