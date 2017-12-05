from PyQt4 import uic, QtGui
import pyodbc
import os.path

( Ui_View_Monsters, QDialog ) = uic.loadUiType( 'View_Monsters.ui' )

class View_Monsters ( QDialog ):
    """View_Monsters inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_View_Monsters()
        self.ui.setupUi( self )
        
        self.ui.View_Monster_Table.setEnabled(True)
        
        Current_Path = os.path.dirname(__file__)
        Database_Location = os.path.join(Current_Path, "DungeonsAndDatabases.accdb")
        print(Database_Location)
        BaseConnect = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=%s;' %Database_Location)
        BaseSelect = BaseConnect.cursor()
        BaseSelect.execute('select MonsterName,MonsterRace,MonsterSize,MonsterAC,MonsterHP,MonsterChallenge from MonsterManual')
        TableFill = BaseSelect.fetchall()
        BaseConnect.close()
        print(TableFill)
        for field in TableFill:
            CountTableRow = self.ui.View_Monster_Table.rowCount()
            self.ui.View_Monster_Table.insertRow(CountTableRow)
            self.ui.View_Monster_Table.setItem(CountTableRow,0,QtGui.QTableWidgetItem(str(field[0])))
            self.ui.View_Monster_Table.setItem(CountTableRow,1,QtGui.QTableWidgetItem(str(field[1])))
            self.ui.View_Monster_Table.setItem(CountTableRow,2,QtGui.QTableWidgetItem(str(field[2])))
            self.ui.View_Monster_Table.setItem(CountTableRow,3,QtGui.QTableWidgetItem(str(field[3])))
            self.ui.View_Monster_Table.setItem(CountTableRow,4,QtGui.QTableWidgetItem(str(field[4])))
            self.ui.View_Monster_Table.setItem(CountTableRow,5,QtGui.QTableWidgetItem(str(field[5])))
    
    
    def __del__ ( self ):
        self.ui = None
    
    def Close_Window( self ):
        self.close()
    
    def rowSelect( self ):
        selected = self.ui.View_Monster_Table.currentRow() # Find the row selected
        selectedID = self.ui.View_Monster_Table.item(selected,0).text()# Find the ID of that selected
        print(selected)
        print(selectedID)