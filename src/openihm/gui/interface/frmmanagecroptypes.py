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

from PyQt4 import QtGui, QtCore, uic

Ui_CropTypes, base_class = uic.loadUiType("gui/designs/ui_managecroptypes.ui")

from mixins import MDIDialogMixin

class FrmManageCropTypes(Ui_CropTypes, MDIDialogMixin):
    
    def setupUi(self,Form,Mdi):
        Ui_CropTypes.setupUi(self,Form)
        self.form = Form
        self.parent = Mdi
        
#        QtCore.QObject.connect(self.btnManageCropsClose, QtCore.SIGNAL("clicked()"), Mdi.closeActiveSubWindow)
