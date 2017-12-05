from PyQt4 import uic

( Ui_Info_Monster_Saving_Throws, QDialog ) = uic.loadUiType( 'Info_Monster_Saving_Throws.ui' )

class Info_Monster_Saving_Throws ( QDialog ):
    """Info_Monster_Saving_Throws inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Info_Monster_Saving_Throws()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
