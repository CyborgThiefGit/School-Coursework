from PyQt4 import uic
import Add_Monster_Ability_Scores
import Add_Monster_Saving_Throws
import Add_Monster_Speed_Window
import os.path
import pyodbc

( Ui_Add_Monster, QDialog ) = uic.loadUiType( 'Add_Monster.ui' )

class Add_Monster ( QDialog ):
    """Add_Monster inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Monster()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    def Close_Window( self ):
        self.close()

    def Monster_Ability_Scores_Link( self ):
        self.MonsterAbilityScoresButton = Add_Monster_Ability_Scores.Add_Monster_Ability_Scores()
        self.MonsterAbilityScoresButton.exec_()
    
    def Monster_Saving_Throws_Link( self ):
        self.MonsterSavingThrowsButton = Add_Monster_Saving_Throws.Add_Monster_Saving_Throws()
        self.MonsterSavingThrowsButton.exec_()
    
    def Monster_Speed_Link( self ):
        self.MonsterSpeedButton = Add_Monster_Speed_Window.Add_Monster_Speed_Window()
        self.MonsterSpeedButton.exec_()
    
    def Import_Foreign_Key( self ):
        TempFile = open("TempSpeedID.txt", 'r')
        TempSpeedID = TempFile.readline()
        self.ui.Speed_Foreign_Key.setText(TempSpeedID)
        TempFile.close()
        TempFile = open("TempSavingThrowsID.txt", 'r')
        TempSavingThrowsID = TempFile.readline()
        self.ui.Saving_Throws_Foreign_Key.setText(TempSavingThrowsID)
        TempFile.close()
        TempFile = open("TempAbilitiesID.txt", 'r')
        TempAbilitiesID = TempFile.readline()
        self.ui.Abilities_Foreign_Key.setText(TempAbilitiesID)
        TempFile.close()
    
    def Race_Populate( self ):
        
    
    def Class_Populate( self ):
        
    
    def Add_Monster_Add_To_DB( self ):
        Current_Path = os.path.dirname(__file__)
        Database_Location = os.path.join(Current_Path, "DungeonsAndDatabases.accdb")
        BaseConnect = pyodbc.connect('Driver={Microsoft Access Driver (*.mdb, *.accdb)}; Dbq=%s;' %Database_Location)
        BaseSelect = BaseConnect.cursor()
        BaseSelect.execute("insert into MonsterManual(MonsterName,MonsterRace,MonsterSize,MonsterAC,MonsterHP,MonsterChallenge,Speeds,MonsterAbilities,MonsterSavingThrows,Lore) values (?,?,?,?,?,?,?,?,?,?)",self.ui.Add_Monster_Name.text(),self.ui.Add_Monster_Race.text(),self.ui.Add_Monster_Size.text(),self.ui.Add_Monster_Armour_Class.text(),self.ui.Add_Monster_Hit_Points.text(),self.ui.Add_Monster_Challenge.text(),self.ui.Speed_Foreign_Key.text(),self.ui.Abilities_Foreign_Key.text(),self.ui.Saving_Throws_Foreign_Key.text(),self.ui.Add_Monster_Lore.toPlainText())
        BaseConnect.commit()
        BaseConnect.close()
        Close_Window()