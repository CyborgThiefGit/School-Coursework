from PyQt4 import uic

( Ui_View_Players, QDialog ) = uic.loadUiType( 'View_Players.ui' )

class View_Players ( QDialog ):
    """View_Players inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_View_Players()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
    
    #def Close_Window( self ):
    #    self.close()
