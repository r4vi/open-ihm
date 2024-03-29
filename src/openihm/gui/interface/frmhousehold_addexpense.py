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

from data.config import Config

Ui_AddHouseholdExpense, base_class = uic.loadUiType("gui/designs/ui_household_addexpense.ui")

from mixins import MDIDialogMixin, MySQLMixin

class FrmHouseholdExpense(QDialog, Ui_AddHouseholdExpense, MDIDialogMixin, MySQLMixin):	
    ''' Form to add or edit Household Expenditure  '''	
    def __init__(self, parent,  hhid, hhname, expid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.pid  = parent.parent.projectid
		self.hhid 		= hhid
		self.expid 		= expid
		
		self.config = Config.dbinfo().copy()
		
		self.getExpenditureTypes()
		
		if ( expid != 0 ):
			self.displayExpenditureDetails()
			self.setWindowTitle( "Edit Household Expenditure" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
    def getExpenditureTypes(self):
		''' Retrieve Expenditure Types and display them in a combobox '''
		# select query to Asset Types
		query = '''SELECT expendituretype FROM setup_expendituretypes'''
		rows = self.executeResultsQuery(query)
		
		for row in rows:
		    exptype = row[0]
		    self.cboExpenditure.addItem(exptype)
        
    def displayExpenditureDetails(self):
		''' Retrieve and display Household Expenditure details '''
		query = '''SELECT * FROM expenditure WHERE hhid=%s AND pid=%s AND expid=%s ''' % ( self.hhid, self.pid, self.expid )
		
		rows = self.executeResultsQuery(query)
		
		for row in rows:
			exptype = row[2]
			self.cboExpenditure.setCurrentIndex( self.cboExpenditure.findText( exptype ) )
			unitofmeasure = row[3]
			self.txtUnitOfMeasure.setText( unitofmeasure )
			costperunit = row[4]
			self.txtCostPerUnit.setText( str(costperunit) )
			kcalperunit = row[5]
			if ( kcalperunit == None ):
				kcalperunit = ""
			self.txtKCalPerUnit.setText( str(kcalperunit) )
			numunits = row[6]
			self.txtNumberOfUnits.setText( str(numunits) )
        
    def saveExpenditure(self):
		''' Saves expenditure to database '''    	
		
		# get the data entered by user
		exptype       = self.cboExpenditure.currentText()
		unitofmeasure = self.txtUnitOfMeasure.text() if self.txtUnitOfMeasure.text() != "" else "Kg"
		costperunit   = self.txtCostPerUnit.text() if self.txtCostPerUnit.text() != "" else "0"
		kcalperunit	  = self.txtKCalPerUnit.text() if self.txtKCalPerUnit.text() != "" else "0"
		numunits      = self.txtNumberOfUnits.text() if self.txtNumberOfUnits.text() != "" else "0"
			
		# create UPDATE query
		expid 	= self.expid
		hhid 	= self.hhid
		if (kcalperunit == ""):
			kcalperunit = "NULL"
			
		if (expid == 0):
			query = '''INSERT INTO expenditure (hhid, exptype, unitofmeasure, priceperunit, kcalperunit, totalunits, pid )
			    VALUES(%s,'%s','%s',%s,%s,%s,%s) ''' % ( hhid, exptype, unitofmeasure, costperunit, kcalperunit, numunits,  self.pid )
		else:
			query = ''' UPDATE expenditure SET exptype='%s', unitofmeasure='%s', priceperunit=%s, kcalperunit=%s,
						totalunits=%s WHERE hhid=%s AND pid=%s 
						AND expid=%s ''' % ( exptype, unitofmeasure, costperunit, kcalperunit, numunits, hhid, self.pid,  expid )
                        
#		QMessageBox.information(self,"Edit Member",query)
		
		self.executeUpdateQuery(query)
		
		# close new project window
		self.parent.retrieveHouseholdExpenses()
		self.mdiClose()
