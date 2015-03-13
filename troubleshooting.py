import sys
from PyQt4 import QtGui, QtCore

'''

The Troubleshoot class is a widget where the user can select from a variety
of troubleshooting problems from a drop-down list. Once the user selects an
issue, tips to resolve it will be provided.
'''
class Help(QtGui.QWidget):
    
    def __init__(self):
        super(Help, self).__init__()
        self.initUI()
        
    # Initilize the UI of the widget
    def initUI(self):   
        
        # Instructions text box
        instruText = QtGui.QLabel("Choose an issue from the drop-down menu.")
        font = QtGui.QFont()
        font.setPointSize(18)
        instruText.setFont(font)
        
        # Items that can be selected from the drop-down menu
        combo = QtGui.QComboBox(self)
        combo.addItem("Calibrating")
        combo.addItem("Troubleshooting")
        combo.addItem("Help")
        combo.addItem("More issues")
        combo.addItem("Even more issues")    
        
        # Test image
        pixmap = QtGui.QPixmap('pidgey.png')
        pixmap = pixmap.scaledToHeight(400)
        self.img = QtGui.QLabel(self)
        self.img.setPixmap(pixmap)
            
        # Ok and Exit buttons
        cancelButton = QtGui.QPushButton("Exit")
        cancelButton.clicked.connect(QtCore.QCoreApplication.instance().quit)

        exitAction = QtGui.QAction(QtGui.QIcon('pigeot_icon.png'), '&Exit', self)        
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(QtGui.qApp.quit)

        hbuttons = QtGui.QHBoxLayout()
        hbuttons.addStretch(1)
        hbuttons.addWidget(cancelButton)
        vbuttons = QtGui.QVBoxLayout()
        vbuttons.addStretch(1)
        vbuttons.addLayout(hbuttons)
        
        # Set the default test to be displayed on launch in text description box
        self.descriptionText = QtGui.QLabel("CALIBRATION ADVICE!!.", self)
        
        # Add sub-widgets to the main layout
        mainVbox = QtGui.QVBoxLayout()
        mainVbox.stretch(1)
        mainVbox.addWidget(instruText)
        mainVbox.addWidget(combo)
        mainVbox.addWidget(self.descriptionText)
        mainVbox.addWidget(self.img)
        mainVbox.addLayout(vbuttons)
        self.setLayout(mainVbox)

        # Create the drop down list on the window
        combo.activated['QString'].connect(self.onActivated)                   
        self.show()

    # When the user selects an item from the list, display its information
    def onActivated(self, text):
        if (text == "Calibrating"):
            text = "CALIBRATION ADVICE!!.."
            pixmap = QtGui.QPixmap('pidgey.png')
        elif (text == "Troubleshooting"):
            text = "TROUBLESHOOTING ADVICE."
            pixmap = QtGui.QPixmap('Pidgeotto.png')
        elif (text == "Help"):
            text = "More help stuff."
            pixmap = QtGui.QPixmap('pidgeot.png')
        elif (text == "More issues"):
            text = "All the issues in the world"
            pixmap = QtGui.QPixmap('pigeot_icon.png')
        elif (text == "Even more issues"):
            text = "More issues could go here too"
            pixmap = QtGui.QPixmap('big_bird.png')
        else:
            text = "Custom Test"
            pixmap = QtGui.QPixmap('big_bird.png')
        # Change displayed text and image
        pixmap = pixmap.scaledToHeight(400)
        self.descriptionText.setText(text)
        self.descriptionText.adjustSize()  
        self.img.setPixmap(pixmap)

      
def main():
    app = QtGui.QApplication(sys.argv)

    window = Help()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()