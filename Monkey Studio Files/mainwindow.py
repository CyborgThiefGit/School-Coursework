from PyQt4 import uic
import pyodbc
import Main_Menu

( Ui_MainWindow, QMainWindow ) = uic.loadUiType( 'mainwindow.ui' )

class MainWindow ( QMainWindow ):
    """MainWindow inherits QMainWindow"""

    def __init__ ( self, parent = None ):
        QMainWindow.__init__( self, parent )
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )

    def __del__ ( self ):
        self.ui = None
        
    def Main_Menu_Link( self ):
        self.MainMenuButton = Main_Menu.Main_Menu()
        self.MainMenuButton.exec_()