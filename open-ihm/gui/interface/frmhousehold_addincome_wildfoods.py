#-------------------------------------------------------------------	
#	Filename: frmhousehold_addincome_wildfoods.py
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from data.config import Config
import data.mysql.connector 

from gui.designs.ui_household_income_wildfoods import Ui_AddHouseholdIncomeWildfoods

class FrmHouseholdWildfoodsIncome(QDialog, Ui_AddHouseholdIncomeWildfoods):	
    ''' Form to add or edit a Household Wildfoods Income  '''	
    def __init__(self, parent,  hhid, hhname, incomeid = 0 ):
		''' Set up the dialog box interface '''
		QDialog.__init__(self)
		self.setupUi(self)
		self.parent 	= parent
		self.hhid 		= hhid
		self.pid = parent.parent.projectid
		self.incomeid 	= incomeid
		
		self.config = Config.dbinfo().copy()
		
		self.getWildfoodsTypes()
		
		if ( incomeid != 0 ):
			self.displayIncomeDetails()
			self.setWindowTitle( "Edit Income Item" )
		  
		# display household name
		self.lblHouseholdName.setText(hhname)
		
		# connect relevant signals and slots
		self.connect(self.cmdCancel, SIGNAL("clicked()"), self.close)
		self.connect(self.cmdSave, SIGNAL("clicked()"), self.saveIncome)
        
    def getWildfoodsTypes(self):
		''' Retrieve Wildfoods Types and display them in a combobox '''
		# select query to Wildfoods Types
		query = '''SELECT incomesource FROM setup_wildfoods'''
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    incometype = row[0]
		    self.cboIncomeType.addItem(incometype)
		 
		cursor.close()   
		db.close()
        
    def displayIncomeDetails(self):
		''' Retrieve and display Household Income details '''
		query = '''SELECT * FROM wildfoods WHERE hhid=%s AND pid=%s AND id=%s ''' % ( self.hhid, self.pid, self.incomeid )
		
		db = data.mysql.connector.Connect(**self.config)             
		cursor = db.cursor()
		
		cursor.execute(query)
		
		for row in cursor.fetchall():
		    incometype = row[2]
		    self.cboIncomeType.setCurrentIndex( self.cboIncomeType.findText( incometype ) )
		    unitofmeasure = row[3]
		    self.txtUnitOfMeasure.setText( unitofmeasure )
		    unitsconsumed = row[4]
		    self.txtUnitsConsumed.setText( str(unitsconsumed) )
		    unitssold = row[5]
		    self.txtUnitsSold.setText( str(unitssold) )
		    unitprice = row[6]
		    self.txtUnitPrice.setText( str(unitprice) )
		 
		cursor.close()   
		db.close()
        
    def saveIncome(self):
		''' Saves wildfoods income to database '''    	
		
		# get the data entered by user
		incometype   	= self.cboIncomeType.currentText()
		unitofmeasure	= self.txtUnitOfMeasure.text()
		unitsconsumed	= self.txtUnitsConsumed.text()
		unitssold		= self.txtUnitsSold.text()
		unitprice		= self.txtUnitPrice.text()
			
		db = data.mysql.connector.Connect(**self.config)
		
		# create UPDATE query
		if (self.incomeid == 0):
			query = '''INSERT INTO wildfoods (hhid, incomesource, unitofmeasure, unitsconsumed, unitssold, unitprice, pid )
			    VALUES(%s,'%s','%s',%s,%s,%s,%s) ''' % ( self.hhid, incometype, unitofmeasure, unitsconsumed, unitssold, unitprice,  self.pid )
		else:
			query = ''' UPDATE wildfoods SET incomesource='%s', unitofmeasure='%s', unitsconsumed=%s, unitssold=%s,
						unitprice=%s WHERE hhid=%s AND pid=%s 
						AND id=%s ''' % ( incometype, unitofmeasure, unitsconsumed, unitssold, unitprice, self.hhid, self.pid, self.incomeid)
		
		# execute query and commit changes
		cursor =  db.cursor()
		cursor.execute(query)
		db.commit()
		
		# close database connection
		cursor.close()
		db.close()
		
		# close new project window
		self.parent.retrieveHouseholdWildfoodsIncome()
		self.close()
