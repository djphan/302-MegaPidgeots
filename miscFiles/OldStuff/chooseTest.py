import sys
from PyQt4 import QtGui, QtCore

'''

The RunTest class is a widget where the user can select a 
premade test from a drop-down list. Once the user chooses a test, the
description matching the test is displayed along with related images.
'''
class RunTest(QtGui.QWidget):
    
    def __init__(self):
        super(RunTest, self).__init__()
        self.initUI()
        
    # Initilize the UI of the widget
    def initUI(self):   
        
        # Instructions text box
        instruText = QtGui.QLabel("Choose a test from the drop-down menu.")
        font = QtGui.QFont()
        font.setPointSize(18)
        instruText.setFont(font)
        
        # Items that can be selected from the drop-down menu
        combo = QtGui.QComboBox(self)
        combo.addItem("Test #1")
        combo.addItem("Test #2")
        combo.addItem("Test #3")
        combo.addItem("Test #4")
        combo.addItem("Test #5")    
        
        # Test image

        self.pic = QtGui.QLabel()
        self.pic.setPixmap(QtGui.QPixmap('pidgey.png'))
            
        # Ok and Exit buttons
        okButton = QtGui.QPushButton("OK")
        okButton.clicked.connect(self.buttonClicked)
        cancelButton = QtGui.QPushButton("Exit")
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        exitAction = QtGui.QAction(QtGui.QIcon('pigeot_icon.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        hbuttons = QtGui.QHBoxLayout()
        hbuttons.addStretch(1)
        hbuttons.addWidget(okButton)
        hbuttons.addWidget(cancelButton)
        vbuttons = QtGui.QVBoxLayout()
        vbuttons.addStretch(1)
        vbuttons.addLayout(hbuttons)
        
        # Set the default test to be displayed on launch in text description box
        self.descriptionText = QtGui.QLabel("Tests vertebre for sections C1 through C7.", self)
        
        # Add sub-widgets to the main layout
        mainVbox = QtGui.QVBoxLayout()
        mainVbox.stretch(1)
        mainVbox.addWidget(instruText)
        mainVbox.addWidget(combo)
        mainVbox.addWidget(self.descriptionText)
        mainVbox.addWidget(self.pic)
        mainVbox.addLayout(vbuttons)
        self.setLayout(mainVbox)

        # Create the drop down list on the window
        combo.activated['QString'].connect(self.onActivated)    
        self.show()

    # When the user selects an item from the list, display its information
    def onActivated(self, text):
        if (text == "Test #1"):
            text = "Tests vertebre for sections C1 through C7."
            self.pic.setPixmap(QtGui.QPixmap('pidgey.png'))
        elif (text == "Test #2"):
            text = "Tests vertebre for sections T1 through T12."
            self.pic.setPixmap(QtGui.QPixmap('Pidgeotto.png'))
        elif (text == "Test #3"):
            text = "Tests vertebre for sections L1 through L5."
            self.pic.setPixmap(QtGui.QPixmap('pidgeot.png'))
        elif (text == "Test #4"):
            text = "Tests all vertebre."
            self.pic.setPixmap(QtGui.QPixmap('pigeot_icon.png'))
        elif (text == "Test #5"):
            text = "Tests vertebre for sections C1 through C7 and L1 through L5."
            self.pic.setPixmap(QtGui.QPixmap('big_bird.png'))
        else:
            text = "Custom Test"
            self.pic.setPixmap(QtGui.QPixmap('big_bird.png'))
        # Change displayed text and image
        self.descriptionText.setText(text)
        self.descriptionText.adjustSize()  
      
     # Do something when the "Ok" button is clicked
     # TODO: We want to make the OK button do something useful :)
    def buttonClicked(self):
        sender = self.sender()
        self.statusBar().showMessage(sender.text() + ' was pressed')
      
def main():
    app = QtGui.QApplication(sys.argv)

    window = RunTest()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()