from PyQt4 import uic
import Monster_Manual
import Character_Sheets

( Ui_Main_Menu, QDialog ) = uic.loadUiType( 'Main_Menu.ui' )

class Main_Menu ( QDialog ):
    """Main_Menu inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Main_Menu()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    def Monster_Manual_Link( self ):
        self.MonsterManualButton = Monster_Manual.Monster_Manual()
        self.MonsterManualButton.exec_()
    
    def Character_Sheet_Link( self ):
        self.CharacterSheetButton = Character_Sheets.Character_Sheets()
        self.CharacterSheetButton.exec_()