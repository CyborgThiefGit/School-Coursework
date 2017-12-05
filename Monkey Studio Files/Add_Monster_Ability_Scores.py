from PyQt4 import uic
import pyodbc
import os.path

( Ui_Add_Monster_Ability_Scores, QDialog ) = uic.loadUiType( 'Add_Monster_Ability_Scores.ui' )

class Add_Monster_Ability_Scores ( QDialog ):
    """Add_Monster_Ability_Scores inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Monster_Ability_Scores()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
        
    def Add_Monster_Abilty_Scores_Save_DB( self ):
        Current_Path = os.path.dirname(__file__)
        Database_Location = os.path.join(Current_Path, "DungeonsAndDatabases.accdb")
        BaseConnect = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=%s;' %Database_Location)
        BaseSelect = BaseConnect.cursor()
        BaseSelect.execute("insert into Abilities(Strength,Dex,Con,Intelligence,Wis,Charisma) values (?,?,?,?,?,?)",self.ui.Ability_Scores_Str.text(),self.ui.Ability_Scores_Dex.text(),self.ui.Ability_Scores_Con.text(),self.ui.Ability_Scores_Int.text(),self.ui.Ability_Scores_Wis.text(),self.ui.Ability_Scores_Cha.text())
        BaseConnect.commit()
        BaseSelect.execute("SELECT @@IDENTITY AS ID")
        TempAbilitiesID = BaseSelect.fetchone()
        BaseConnect.close()
        TempFile = open("TempAbilitiesID.txt",'w')
        TempFile.write(str(TempAbilitiesID.ID))
        TempFile.close()