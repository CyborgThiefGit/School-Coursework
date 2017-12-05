from PyQt4 import uic

( Ui_Info_Monster_Ability_Scores, QDialog ) = uic.loadUiType( 'Info_Monster_Ability_Scores.ui' )

class Info_Monster_Ability_Scores ( QDialog ):
    """Info_Monster_Ability_Scores inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Info_Monster_Ability_Scores()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
