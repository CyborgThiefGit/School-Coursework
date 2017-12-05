from PyQt4 import uic
import View_Players

( Ui_Add_Players, QDialog ) = uic.loadUiType( 'Add_Players.ui' )

class Add_Players ( QDialog ):
    """Add_Players inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Players()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
