import sys
from PyQt4 import QtGui, QtCore
from chooseTest import ChooseTestWindow

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
        tab1 = QtGui.QWidget()   
        tab2 = QtGui.QWidget()
        tab3 = QtGui.QWidget()

        # Create a window for our layouts
        page = QtGui.QVBoxLayout(tab1)
        page2 = QtGui.QVBoxLayout(tab2)
        page3 = QtGui.QVBoxLayout(tab3)

        tabs.addTab(tab1,"Main")
        tabs.addTab(tab2,"Choose Test")
        tabs.addTab(tab3,"Results")

        # Instructions text box
        instruText = QtGui.QLabel("How to Cailbrate OptiTrack")
        font = QtGui.QFont()
        font.setPointSize(18)
        instruText.setFont(font)

        # Instructions
        self.step1 = QtGui.QLabel("Step 1: Select Cailbrate", self)
        self.step2 = QtGui.QLabel("Step 2: Wave Wand Around", self)
        self.step3 = QtGui.QLabel("Step 3: Apply Cailbrations", self)

        menu_bar = QtGui.QMenuBar() 
        file = menu_bar.addMenu("&File") 
        help = menu_bar.addMenu("&Help")
        
        # Test image
        pixmap = QtGui.QPixmap('pidgey.png')
        pixmap = pixmap.scaledToHeight(200)
        self.img = QtGui.QLabel(self)
        self.img.setPixmap(pixmap)
            
        # Ok and Exit buttons
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.buttonClicked)
        cancelButton = QtGui.QPushButton("Exit")
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        exitAction = QtGui.QAction(QtGui.QIcon('pigeot_icon.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        addTestAction = QtGui.QAction(QtGui.QIcon('pigeot_icon.png'), '&AddTest' , self)
        addTestAction.setStatusTip("Add Test")

        hbuttons = QtGui.QHBoxLayout()
        hbuttons.addStretch(1)
        hbuttons.addWidget(okButton)
        hbuttons.addWidget(cancelButton)
        vbuttons = QtGui.QVBoxLayout()
        vbuttons.addStretch(1)
        vbuttons.addLayout(hbuttons)
        
        page.addWidget(instruText)
        page.addWidget(self.step1)
        page.addWidget(self.step2)
        page.addWidget(self.step3)
        page.addWidget(self.img)
        page.addWidget(cancelButton)

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
        self.setWindowTitle('Main Menu')
        # Show our pigeot pokemon icon
        self.setWindowIcon(QtGui.QIcon('pigeot_icon.png'))      
        self.show()
        

     # Do something when the "Ok" button is clicked
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
        
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