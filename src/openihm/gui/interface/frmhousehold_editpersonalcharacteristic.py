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

from control.controller import Controller

Ui_EditMemberCharacteristic, base_class = uic.loadUiType("gui/designs/ui_household_editmembercharacteristic.ui")

from mixins import MDIDialogMixin, MySQLMixin

class FrmEditPersonalCharacteristic(QDialog, Ui_EditMemberCharacteristic, MySQLMixin, MDIDialogMixin):	
     ''' Creates the Edit Personal Characteristic form. '''	
     def __init__(self, parent, pid, hhid, personid, charName, charVal):
         ''' Set up the dialog box interface '''
         QDialog.__init__(self)
         self.setupUi(self)
         self.parent = parent
         self.hhid = hhid
         self.pid = pid
         self.personid = personid
         self.charName = charName
        
         # display characteristic name
         self.lblCharName.setText(charName)
         if ( self.parent.getPersonalCharacteristicDataType( charName ) == 1 ):
             self.cboYesNoVal.setVisible( True )
             self.txtValue.setVisible( False )
             if ( charVal != "Not Set" ):
                 self.cboYesNoVal.setCurrentIndex( self.cboYesNoVal.findText( charVal ) )
         else:
             self.cboYesNoVal.setVisible( False )
             self.txtValue.setVisible( True )
             if ( charVal != "Not Set" ):
                 self.txtValue.setText( charVal )

     def saveCharacteristic(self):
         ''' Saves characteristic '''
         
         if self.cboYesNoVal.isVisible():
             charVal = self.cboYesNoVal.currentText() 
         else:
             charVal = self.txtValue.text()
         
         controller = Controller()
         project = controller.getProject(self.pid)
         household = project.getHousehold(self.hhid)
         member = household.getMember(self.personid)
         
         if not member.existsCharacteristic(self.charName):
             member.addCharacteristic(self.charName, charVal)
         else:
             char = member.getCharacteristic(self.charName)
             char.editData(self.charName, charVal)
             
         # close window and refresh characteristics
         self.parent.retrievePersonalCharacteristics( self.personid )
         self.mdiClose()
