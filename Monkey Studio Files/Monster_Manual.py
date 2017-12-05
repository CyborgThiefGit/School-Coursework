from PyQt4 import uic
import Add_Monster
import View_Monsters

( Ui_Monster_Manual, QDialog ) = uic.loadUiType( 'Monster_Manual.ui' )

class Monster_Manual ( QDialog ):
    """Monster_Manual inherits QDialog"""

    def __init__ ( self, parent = None ):
        QDialog.__init__( self, parent )
        self.ui = Ui_Monster_Manual()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
     
    def Close_Window( self ):
        self.close()
        
    def Add_Monster_Link( self ):
        self.AddMonsterButton = Add_Monster.Add_Monster()
        self.AddMonsterButton.exec_()
        
    def View_Monster_Link( self ):
        self.ViewMonsterButton = View_Monsters.View_Monsters()
        self.ViewMonsterButton.exec_()
