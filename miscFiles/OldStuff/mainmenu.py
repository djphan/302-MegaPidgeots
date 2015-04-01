import sys
#sys.path.insert(0, "C:\\Users\\STAIR\\Desktop\\ProjectDR\\302-MegaPidgeots-master")
from PyQt4 import QtGui, QtCore
from chooseTest import RunTest
from results import ResultsWindow
from maintab import MainTabWidget
from troubleshooting import Help
'''
Start Page with Setup Instructions
'''
class MainWindow(QtGui.QWidget):
    
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()
        
    # Initilize the UI of the window
    def initUI(self):

        #Tabs
        tabs = QtGui.QTabWidget()
        tab1 = MainTabWidget()  
        tab2 = RunTest()
        tab3 = ResultsWindow()
        tab4 = Help()

        tabs.addTab(tab1,"Main")
        tabs.addTab(tab2,"Choose Test")
        tabs.addTab(tab3,"Results")
        tabs.addTab(tab4, "Troubleshooting")


        menu_bar = QtGui.QMenuBar() 
        file = menu_bar.addMenu("&File") 
        help = menu_bar.addMenu("&Help")
        
        mainVbox = QtGui.QVBoxLayout()
        
        mainVbox.addWidget(tabs)
        mainVbox.addWidget(menu_bar)

        self.setLayout(mainVbox)     
        """
        #Menubar
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')
        helpMenu = menubar.addMenu('&Help')
        menubar.addAction(exitAction)
        """
        """
        #Toolbar
        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(exitAction)
        self.toolbar.addAction(addTestAction)
        """
        # Create the window     
        self.resize(800, 600)         # Width: 800 pixels, height 600 pixels
        self.centerWindow()           # Center the box on the users screen              
        self.setWindowTitle('302 Project')
        # Show our pigeot pokemon icon
        self.setWindowIcon(QtGui.QIcon('pigeot_icon.png'))      
        self.show()
        
    # A function to move the window to the center of the users screen
    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
                
def main():
    app = QtGui.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()