from PyQt4 import uic

( Ui_More_Monster_Info_Ability_Scores, QDialog ) = uic.loadUiType( 'More_Monster_Info_Ability_Scores.ui' )

class More_Monster_Info_Ability_Scores ( QDialog ):
    """More_Monster_Info_Ability_Scores inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_More_Monster_Info_Ability_Scores()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
