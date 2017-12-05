from PyQt4 import uic

( Ui_Info_Monster_Speed, QDialog ) = uic.loadUiType( 'Info_Monster_Speed.ui' )

class Info_Monster_Speed ( QDialog ):
    """Info_Monster_Speed inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Info_Monster_Speed()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
