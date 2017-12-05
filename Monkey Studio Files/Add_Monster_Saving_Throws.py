from PyQt4 import uic
import pyodbc
import os.path

( Ui_Add_Monster_Saving_Throws, QDialog ) = uic.loadUiType( 'Add_Monster_Saving_Throws.ui' )

class Add_Monster_Saving_Throws ( QDialog ):
    """Add_Monster_Saving_Throws inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Monster_Saving_Throws()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def Add_Monster_Saving_Throws_Save_DB( self ):
        Current_Path = os.path.dirname(__file__)
        Database_Location = os.path.join(Current_Path, "DungeonsAndDatabases.accdb")
        BaseConnect = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=%s;' %Database_Location)
        BaseSelect = BaseConnect.cursor()
        BaseSelect.execute("insert into SavingThrows(Strength,Dex,Con,Intelligence,Wis,Charisma) values (?,?,?,?,?,?)",self.ui.Saving_Throws_Str.text(),self.ui.Saving_Throws_Dex.text(),self.ui.Saving_Throws_Con.text(),self.ui.Saving_Throws_Int.text(),self.ui.Saving_Throws_Wis.text(),self.ui.Saving_Throws_Cha.text())
        BaseConnect.commit()
        BaseSelect.execute("SELECT @@IDENTITY AS ID")
        TempSavingThrowID = BaseSelect.fetchone()
        BaseConnect.close()
        TempFile = open("TempSavingThrowsID.txt",'w')
        TempFile.write(str(TempSavingThrowID.ID))
        TempFile.close()
        