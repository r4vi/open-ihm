#	Filename: frm_report_householdincome.py
#
#	Display dialog for Report household income by income source.
#-------------------------------------------------------------------

# imports from PyQt4 package
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# import packages
from gui.designs.ui_report_householdincome import Ui_HouseholdIncomeReport
from data.report_settingsmanager import ReportsSettingsManager
from outputs.routines.report_householdsincome import HouseholdIncome

class HouseholdIncomeReport(QDialog, Ui_HouseholdIncomeReport):
    ''' Creates the Household Income Report by Source from. Uses the design class
		in gui.designs.ui_report_householdincome. '''	
	
    def __init__(self, parent):
        
	''' Set up the dialog box interface '''
	self.parent = parent
        QDialog.__init__(self)
       	self.setupUi(self)
        self.parent = parent

        self.getProjectNames()
        self.putMainIncomeCategories()
        self.insertHouseholdsHeader()
        	
        self.connect(self.cmdClose, SIGNAL("clicked()"), self.parent.mdi.closeActiveSubWindow)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.getHouseholdCharacteristics)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.getPersonalCharacteristics)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.putHouseholdNames)
        self.connect(self.cmbProjects, SIGNAL("currentIndexChanged(int)"), self.putCropIncomeSources)

        self.connect(self.cmdShowReport, SIGNAL("clicked()"), self.getCropReportDetails)

    def getProjectNames(self):
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


    def putMainIncomeCategories(self):
        ''' Insert Income categories in the Income sources treeview'''

        categories = ['Crops','Employment','Livestock','Loans','Transfers','Wild Foods']
        num = 0
        model = QStandardItemModel()
        parent = QModelIndex()
        child = QModelIndex()

        parent = model.index( 0, 0 )
        model.insertColumn(0, parent ) #one column for children
        model.insertRows( 0, 6, parent )
        model.setHorizontalHeaderItem(0,QStandardItem('Income Sources'))
        
        for row in categories:
            child = model.index( num, 0, parent )
            model.setData(child, row)
            num = num + 1
                        		
        self.treeView.setModel(model)
        self.treeView.show()

    def getCropsIndex(self):
        cropsindex = self.treeView.model().index(0, 0)
        return cropsindex
    
    def putCropIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getCropIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getCropsIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getEmploymentIndex(self):
        parentindex = self.treeView.model().index(1, 0)
        return parentindex


    def putEmploymentIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getEmploymentIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getEmploymentIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getLivestockIndex(self):
        parentindex = self.treeView.model().index(2, 0)
        return parentindex


    def putLivestockIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getLivestockIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getLivestockIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getLoansIndex(self):
        parentindex = self.treeView.model().index(3, 0)
        return parentindex

    def putLoanSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getLoanIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getLoansIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getTransferIncomeIndex(self):
        parentindex = self.treeView.model().index(4, 0)
        return parentindex

    def putTransferIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getTransferIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getTransferIncomeIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getWildFoodsIncomeIndex(self):
        parentindex = self.treeView.model().index(5, 0)
        return parentindex

    def putwildFoodIncomeSources(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getWildfoodsIncomeSources(projectid)
        numrows = len(rows)

        parent = self.getWildFoodsIncomeIndex()
        self.treeView.model().insertColumn(0, parent )
        self.treeView.model().insertRows( 0, numrows, parent )

        num =0
        
        for row in rows:
            child = self.treeView.model().index( num, 0, parent )
            self.treeView.model().setData(child, row[0])
            num = num + 1

    def getHouseholdNames(self):
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getProjectHouseholds(projectid)
        return rows

    def insertHouseholdsHeader(self):
        model = QStandardItemModel()
        model.setHorizontalHeaderItem(0,QStandardItem('Select Household Names'))
        self.treeViewHouseholds.setModel(model)
        self.treeViewHouseholds.show()	

    def putHouseholdNames(self):
        ''' Insert household names for the selected Project'''

        hholdnames = self.getHouseholdNames()
        model = QStandardItemModel()
        parent = QModelIndex()
        name = 'All Households'
        numberofrows = len(hholdnames)

        model.insertRow(0,parent )
        model.insertColumn(0, parent ) #one column for children
        parent = model.index( 0, 0 )
        model.setData( parent, name )

        #Insert project-specific household names as childred of the node 'All Households'
        parent = model.index(0, 0, QModelIndex())
        model.insertColumn(0, parent )
        model.insertRows( 0, numberofrows, parent )
        num = 0
        for row in hholdnames:
 
            child = model.index( num, 0, parent )
            model.setData(child, row[0])
            num = num + 1
                        		
        model.setHorizontalHeaderItem(0,QStandardItem('Select Household Names'))
        self.treeViewHouseholds.setModel(model)
        self.treeViewHouseholds.show()	

    def getHouseholdCharacteristics(self):
        
        ''' get household characteristics relevant to selected project'''
                
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getHouseholdCharacteristics(projectid)
        model = QStandardItemModel()
	num = 0

        for row in rows:
            
            qtHCharacteristic = QStandardItem( "%s" % row[0])
            qtHCharacteristic.setTextAlignment( Qt.AlignLeft )
            if ((qtHCharacteristic.text() != 'hhid')and(qtHCharacteristic.text() != 'pid') ):
                
                model.setItem( num, 0, qtHCharacteristic )
                num = num + 1
                        		
        self.listViewHCharacteristics.setModel(model)
        self.listViewHCharacteristics.show()	

    def getPersonalCharacteristics(self):
        ''' get personal characteristics relevant to the selected project'''
                
        projectid = self.getProjectID()
        settingsmgr = ReportsSettingsManager()
        rows = settingsmgr.getPersonalCharacteristics(projectid)
        model = QStandardItemModel()
	num = 0
        for row in rows:
            qtPCharacteristic = QStandardItem( "%s" % row[0])
            qtPCharacteristic.setTextAlignment( Qt.AlignLeft )
                        
            if ((qtPCharacteristic.text() != 'hhid')and(qtPCharacteristic.text() != 'personid') and (qtPCharacteristic.text() != 'pid')):
                model.setItem( num, 0, qtPCharacteristic )
                num = num + 1
                        		
        self.listViewPersonalCharacteristics.setModel(model)
        self.listViewPersonalCharacteristics.show()	

    def getSelectedHouseholdCharacteristics(self):
        ''' get list of user selected household characteristics as part of the criteria for report generation'''
		
	selectedHChars = []
	selectedIndexes = self.getSelectedHIndexes()
		
	for indexVal in selectedIndexes:
            currentitem = self.listViewHCharacteristics.model().item(indexVal.row(),0).text()
	    if currentitem not in selectedHChars:
		selectedHChars.append(str(currentitem))
	return selectedHChars

    def getSelectedHIndexes(self):
        return self.listViewHCharacteristics.selectedIndexes()

    def getSelectedPersonalCharacteristics(self):
        ''' get list of user selected househpersonal characteristics as part of the criteria for report generation'''
		
	selectedRows = []
	selectedIndexes = self.getSelectedPIndexes()
		
	for indexVal in selectedIndexes:
            currentitem = self.listViewPersonalCharacteristics.model().item(indexVal.row(),0).text()
	    if currentitem not in selectedRows:
		selectedRows.append(str(currentitem))
	return selectedRows

    def getSelectedPIndexes(self):
        return self.listViewPersonalCharacteristics.selectedIndexes()

    def getSelectedHouseholdsIndexes(self):
        return self.treeViewHouseholds.selectedIndexes()
        
    def getReportHouseholdIDs (self):
        
        householdIDsQuery =self.getHouseholdIDsQuery()
        connector = HouseholdIncome()
        householdIDs = connector.getReportHouseholdIDs(householdIDsQuery)
        print householdIDs
        return householdIDs

    def getHouseholdIDsQuery(self):

        projectid = self.getProjectID()
        selectedHChars = self.getSelectedHouseholdCharacteristics()
        selectedPChars = self.getSelectedPersonalCharacteristics()
        selectedhouseholds = self.getHouseholdsSelection()
        connector = HouseholdIncome()
        householdIDsQuery = connector.buildReportHouseholdIDsQuery(projectid,selectedhouseholds,selectedPChars,selectedHChars)
        return householdIDsQuery

    def getHouseholdsSelection(self):
        
        selectedIndexes = self.getSelectedHouseholdsIndexes()
        parentIndex = self.treeViewHouseholds.model().index(0, 0, QModelIndex())
        hholdnames = []
        
        if len(selectedIndexes) != 0:
            if parentIndex in selectedIndexes:
                houses = self.getHouseholdNames()
                for house in houses:
                    hholdnames.append(str(house[0]))
                    print house
                    
            else:
                for indexVal in selectedIndexes:
                    currentitem = self.treeViewHouseholds.model().data(indexVal, Qt.DisplayRole).toString()
                    hholdnames.append(str(currentitem))
        else:
            QMessageBox.information(self,"Households By Income Source","No Households Selected")
        return hholdnames

    def getCropReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getCropsIndex()
            selectedIndexes = self.getSelectedCropCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedCropCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        cropsroot = self.getCropsIndex()
        cropincomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == cropsroot) or (indexVal.parent() == cropsroot):
                if indexVal not in cropincomeIndexes:
                    cropincomeIndexes.append(indexVal)

        print cropincomeIndexes
        return cropincomeIndexes

    def getEmploymentReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getEmploymentIndex()
            selectedIndexes = self.getSelectedEmploymentCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedEmploymentCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getEmploymentIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)

        print incomeIndexes
        return incomeIndexes

    def getLivestockReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getLivestockIndex()
            selectedIndexes = self.getSelectedLivestockCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedLivestockCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getLivestockIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)

        print incomeIndexes
        return incomeIndexes

    def getLoansReportDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getLoansIndex()
            selectedIndexes = self.getSelectedLoansCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedLoansCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getLoansIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)

        print incomeIndexes
        return incomeIndexes

    def getTransfersDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getTransferIncomeIndex()
            selectedIndexes = self.getSelectedTransfersCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedTransfersCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getTransferIncomeIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)

        print incomeIndexes
        return incomeIndexes

    def getTransfersDetails(self):
        householdIDs = self.getReportHouseholdIDs()
        requiredDetailType =[]
        
        if len(householdIDs)!=0:
            parentIndex = self.getWildFoodsIncomeIndex()
            selectedIndexes = self.getSelectedWildFoodsCriteria()
            if len(selectedIndexes) != 0:
                if parentIndex in selectedIndexes:
                    requiredDetailType.append('All')
                else:
                    for indexVal in selectedIndexes:
                        currentitem = self.treeView.model().data(indexVal, Qt.DisplayRole).toString()
                        print currentitem
                        requiredDetailType.append(str(currentitem))
        print requiredDetailType
        return requiredDetailType
        
    def getSelectedWildFoodsCriteria(self):
        selectedIncomeIndexes = self.treeView.selectedIndexes()
        root = self.getWildFoodsIncomeIndex()
        incomeIndexes = []
        for indexVal in selectedIncomeIndexes:
            if (indexVal == root) or (indexVal.parent() == root):
                if indexVal not in incomeIndexes:
                    incomeIndexes.append(indexVal)

        print incomeIndexes
        return incomeIndexes
