from PyQt4 import uic

( Ui_More_Monster_Info, QDialog ) = uic.loadUiType( 'More_Monster_Info.ui' )

class More_Monster_Info ( QDialog ):
    """More_Monster_Info inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_More_Monster_Info()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
