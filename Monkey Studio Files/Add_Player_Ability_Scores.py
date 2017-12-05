from PyQt4 import uic

( Ui_Add_Player_Ability_Scores, QDialog ) = uic.loadUiType( 'Add_Player_Ability_Scores.ui' )

class Add_Player_Ability_Scores ( QDialog ):
    """Add_Player_Ability_Scores inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Player_Ability_Scores()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
