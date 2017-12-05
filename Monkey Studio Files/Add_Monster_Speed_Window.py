from PyQt4 import uic
import pyodbc
import os.path

( Ui_Add_Monster_Speed_Window, QDialog ) = uic.loadUiType( 'Add_Monster_Speed_Window.ui' )

class Add_Monster_Speed_Window ( QDialog ):
    """Add_Monster_Speed_Window inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Monster_Speed_Window()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def Add_Monster_Speeds_Save_DB( self ):
        Current_Path = os.path.dirname(__file__)
        Database_Location = os.path.join(Current_Path, "DungeonsAndDatabases.accdb")
        BaseConnect = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=%s;' %Database_Location)
        BaseSelect = BaseConnect.cursor()
        BaseSelect.execute("insert into Speed(Walk,Burrow,Fly,Climb,Swim) values (?,?,?,?,?)",self.ui.Speeds_Walk.text(),self.ui.Speeds_Burrow.text(),self.ui.Speeds_Fly.text(),self.ui.Speeds_Climb.text(),self.ui.Speeds_Swim.text())
        BaseConnect.commit()
        BaseSelect.execute("SELECT @@IDENTITY AS ID")
        TempSpeedID = BaseSelect.fetchone()
        BaseConnect.close()
        TempFile = open("TempSpeedID.txt",'w')
        TempFile.write(str(TempSpeedID.ID))
        TempFile.close()