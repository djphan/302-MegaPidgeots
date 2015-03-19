from PyQt4 import QtCore, QtGui


class TabDialog(QtGui.QDialog):
    def __init__(self, fileName, parent=None):
        super(TabDialog, self).__init__(parent)

        fileInfo = QtCore.QFileInfo(fileName)

        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(CalibrationTab(fileInfo), "Calibration")
        tabWidget.addTab(SetupTab(fileInfo), "Set Up Test")
        tabWidget.addTab(ResultsTab(fileInfo), "Results")

        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Ok | QtGui.QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("302 Project")


class CalibrationTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(CalibrationTab, self).__init__(parent)

        fileNameLabel = QtGui.QLabel("How to Calibrate OptiTrack")
        pathLabel = QtGui.QLabel("Step1: sfdsfdsfdsf")
        sizeLabel = QtGui.QLabel("Step2: fjdsifjdsfopdsafd")
        lastReadLabel = QtGui.QLabel("Step3: sjfiosjfiodfjid")
        lastModLabel = QtGui.QLabel("Step4: sfjidspjfdps")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(pathLabel)
        mainLayout.addWidget(sizeLabel)
        mainLayout.addWidget(lastReadLabel)
        mainLayout.addWidget(lastModLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)


class SetupTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(SetupTab, self).__init__(parent)

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
        #pixmap = QtGui.QPixmap('pidgey.png')
        #pixmap = pixmap.scaledToHeight(400)
        #self.img = QtGui.QLabel(self)
        #self.img.setPixmap(pixmap)
        
        # Set the default test to be displayed on launch in text description box
        self.descriptionText = QtGui.QLabel("Tests vertebre for sections C1 through C7.", self)
        
        # Add sub-widgets to the main layout
        mainVbox = QtGui.QVBoxLayout()
        mainVbox.stretch(1)
        mainVbox.addWidget(instruText)
        mainVbox.addWidget(combo)
        mainVbox.addWidget(self.descriptionText)
        #mainVbox.addWidget(self.img)
        self.setLayout(mainVbox)

        # Create the drop down list on the window
        combo.activated['QString'].connect(self.onActivated)    
        self.show()

    # When the user selects an item from the list, display its information
    def onActivated(self, text):
        if (text == "Test #1"):
            text = "Tests vertebre for sections C1 through C7."
            #pixmap = QtGui.QPixmap('pidgey.png')
        elif (text == "Test #2"):
            text = "Tests vertebre for sections T1 through T12."
            #pixmap = QtGui.QPixmap('Pidgeotto.png')
        elif (text == "Test #3"):
            text = "Tests vertebre for sections L1 through L5."
            #pixmap = QtGui.QPixmap('pidgeot.png')
        elif (text == "Test #4"):
            text = "Tests all vertebre."
            #pixmap = QtGui.QPixmap('pigeot_icon.png')
        elif (text == "Test #5"):
            text = "Tests vertebre for sections C1 through C7 and L1 through L5."
            #pixmap = QtGui.QPixmap('big_bird.png')
        else:
            text = "Custom Test"
            #pixmap = QtGui.QPixmap('big_bird.png')
        # Change displayed text and image
        #pixmap = pixmap.scaledToHeight(400)
        self.descriptionText.setText(text)
        self.descriptionText.adjustSize()  
        #self.img.setPixmap(pixmap)


class ResultsTab(QtGui.QWidget):
    def __init__(self, fileInfo, parent=None):
        super(ResultsTab, self).__init__(parent)
        
        fileNameLabel = QtGui.QLabel("How to Calibrate OptiTrack")
        pathLabel = QtGui.QLabel("Step1: sfdsfdsfdsf")
        sizeLabel = QtGui.QLabel("Step2: fjdsifjdsfopdsafd")
        lastReadLabel = QtGui.QLabel("Step3: sjfiosjfiodfjid")
        lastModLabel = QtGui.QLabel("Step4: sfjidspjfdps")

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(fileNameLabel)
        mainLayout.addWidget(pathLabel)
        mainLayout.addWidget(sizeLabel)
        mainLayout.addWidget(lastReadLabel)
        mainLayout.addWidget(lastModLabel)
        mainLayout.addStretch(1)
        self.setLayout(mainLayout)

if __name__ == '__main__':

    import sys

    app = QtGui.QApplication(sys.argv)

    if len(sys.argv) >= 2:
        fileName = sys.argv[1]
    else:
        fileName = "."

    tabdialog = TabDialog(fileName)
    sys.exit(tabdialog.exec_())
