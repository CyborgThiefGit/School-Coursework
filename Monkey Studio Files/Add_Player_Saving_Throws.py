from PyQt4 import uic

( Ui_Add_Player_Saving_Throws, QDialog ) = uic.loadUiType( 'Add_Player_Saving_Throws.ui' )

class Add_Player_Saving_Throws ( QDialog ):
    """Add_Player_Saving_Throws inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Add_Player_Saving_Throws()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
