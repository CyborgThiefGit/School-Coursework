from PyQt4 import uic
import View_Players
import Add_Players

( Ui_Character_Sheets, QDialog ) = uic.loadUiType( 'Character_Sheets.ui' )

class Character_Sheets ( QDialog ):
    """Character_Sheets inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Character_Sheets()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None

    def Close_Window( self ):
        self.close()
    
    def View_Players_Link( self ):
        self.ViewPlayersButton = View_Players.View_Players()
        self.ViewPlayersButton.exec_()
    
    def Add_Players_Link( self ):
        self.AddPlayersButton = Add_Players.Add_Players()
        self.AddPlayersButton.exec_() 
    
    #def Comapare_Players_Link( self ):
        #self.ComaparePlayersButton = Comapare_Players.Comapare_Players()
        #self.ComaparePlayersButton.exec_() 