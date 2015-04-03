from __future__ import print_function
from calibrationWizard import CalibrationWizard
import os
import SceneManager
import ClientHandler
#from multiprocessing import Process
import button
import polyModel
import time

# Some global variables: Our Test Names
TEST1 = "Skeleton Full"
TEST2 = "Skeleton Partial"
MODEL1 = "skeleton1"
MODEL2 = "skeleton2"
PATH1 = "C:\Users\Aedan\Documents\ProjectDR\Skeleton_Full.OSGB"
PATH2 = "C:\Users\Aedan\Documents\ProjectDR\Skeleton_Back.OSGB"

from PyQt4 import QtCore, QtGui

handNavModel = "NAVIGATION HAND"
handButtModel = "BUTTON HAND"
buttonModel = "Button"
greenModel = "Result Model"
handPath = "C:\Users\Aedan\Documents\ProjectDR\Blue.OSGB"
navPath = "C:\Users\Aedan\Documents\ProjectDR\Orange.OSGB"
buttonPath = "C:\Users\Aedan\Documents\ProjectDR\HAND.OSGB"
greenPath = "C:\Users\Aedan\Documents\ProjectDR\GREEN.OSGB"

#def print(*arg, **kwargs):
    #for args in arg:
        #f1 = open('printlog.txt', 'a')
        #f1.write(args)
        #f1.write("\n")
        #f1.close()


class TabDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        super(TabDialog, self).__init__(parent)

        # Create our tabs
        tabWidget = QtGui.QTabWidget()
        tabWidget.addTab(CalibrationTab(), "Calibration")
        tabWidget.addTab(SetupTab(), "Set Up Test")
        tabWidget.addTab(ResultsTab(), "Results")

        # Exit buttons
        buttonBox = QtGui.QDialogButtonBox(QtGui.QDialogButtonBox.Close)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(tabWidget)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("302 Project")
        self.resize(1000, 600)

# This tab deals with OptiTrack setup and calibration.
class CalibrationTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(CalibrationTab, self).__init__(parent)

        # The tabs contains a button to open the wizard.
        self.text = QtGui.QLabel("The calibration wizard can be used to guide you through OptiTrack setup.")
        self.button = QtGui.QPushButton("Open Wizard")
        self.button.clicked.connect(self.openWizard)

        # Layout for buttons
        hbuttons = QtGui.QHBoxLayout()
        hbuttons.addStretch(1)
        hbuttons.addWidget(self.button)
        vbuttons = QtGui.QVBoxLayout()
        vbuttons.addStretch(1)
        vbuttons.addLayout(hbuttons)

        # Layout for the widget
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.text)
        mainLayout.addLayout(vbuttons)
        self.setLayout(mainLayout)
        self.show()

    # Uses file dialog to get path to module, returns a string
    def openWizard(self):
        wizard = CalibrationWizard()
        wizard.exec_()

# This tab deals with selecting a test to run.
class SetupTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(SetupTab, self).__init__(parent)

        # Instructions text box
        instruText = QtGui.QLabel("Choose a test from the drop-down menu.")
        font = QtGui.QFont()
        font.setPointSize(14)
        instruText.setFont(font)

        # Items that can be selected from the drop-down menu
        self.combo = QtGui.QComboBox(self)
        self.combo.addItem(TEST1)
        self.combo.addItem(TEST2)

        # Test image
        self.img = QtGui.QLabel(self)
        pixmap = QtGui.QPixmap('spooky.png')
        pixmap = pixmap.scaledToHeight(400)
        self.img.setPixmap(pixmap)

        # Set the default test to be displayed on launch in text description box
        self.descriptionText = QtGui.QLabel("Tests vertebrae for sections C1 through C7.", self)

        # Ok Button
        select = QtGui.QPushButton("Start Test")
        select.clicked.connect(self.selectTest)

        # Layout for Ok Button (this makes it in the bottom right-hand corner)
        hbuttons = QtGui.QHBoxLayout()
        hbuttons.addStretch(1)
        hbuttons.addWidget(select)
        vbuttons = QtGui.QVBoxLayout()
        vbuttons.addStretch(1)
        vbuttons.addLayout(hbuttons)

        # Add sub-widgets to the main layout
        mainVbox = QtGui.QVBoxLayout()
        mainVbox.stretch(1)
        mainVbox.addWidget(instruText)
        mainVbox.addWidget(self.combo)
        mainVbox.addWidget(self.descriptionText)
        mainVbox.addWidget(self.img)
        mainVbox.addLayout(vbuttons)
        self.setLayout(mainVbox)

        # Create the drop down list on the window
        self.combo.activated['QString'].connect(self.onActivated)
        self.show()

    # When the user selects a test to run, open models in ProjectDR
    def selectTest(self):
        # Grab currently displayed test from combo box
        chosenTest = str(self.combo.currentText())

        # Based on displayed test, send model to projectDr
        if chosenTest == TEST1:
            model = MODEL1
        else:
            model = MODEL2

        # Before we try to add a model, we should make sure one doesn't already exist
        if SceneManager.doesModelExist(MODEL1) or SceneManager.doesModelExist(MODEL2):
            title = "A skeleton model is already loaded!"
            error = "Please wait for current test to finish before attempting to start another."
            QtGui.QMessageBox.critical(None, title, error, QtGui.QMessageBox.Close)
            return

        """
        >>>>> YOU NEED TO CHANGE PATH TO MODELS BASED ON YOUR COMPUTER <<<<
        """
        # We can load the model in projectDr now
        if model == MODEL1:
            path = PATH1
        else:
            path = PATH2

        # Notify the user that model was successfully loaded.
        title = "Model Loaded"
        error = "Model was successfully loaded into ProjectDr."
        QtGui.QMessageBox.information(None, title, error, QtGui.QMessageBox.Ok)

        # Send the model to scene manager

        print("LOADING NEW TEST")

        # Load Skeleton
        SceneManager.loadPolygonModel(path, model)

        #Scale Skeleton
        SceneManager.getModel(model).setScale(.05,.05,.05)
        SceneManager.getModel(model).setRotationOffset(0,0,-1,1)
        SceneManager.getModel(model).setPositionOffset(0,.15,-1.7)
        SceneManager.addNodeToScene(model,"mainView")
        SceneManager.addNodeToScene(model,"projectorView")

        # Start thread for running test!
        self.thread = WorkThread()
        self.thread.start()
        return


    # When the user selects an item from the list, display its information
    def onActivated(self, text):
        if text == TEST1:
            text = "Tests vertebrae on the full skeleton model."
            pixmap = QtGui.QPixmap('spooky.png')

        else:
            text = "Tests vertebrae on the partial skeleton model."
            pixmap = QtGui.QPixmap('spooky2.png')

        # Change displayed text and image
        pixmap = pixmap.scaledToHeight(400)
        self.descriptionText.setText(text)
        self.descriptionText.adjustSize()
        self.img.setPixmap(pixmap)


class ResultsTab(QtGui.QWidget):
    def __init__(self, parent=None):
        super(ResultsTab, self).__init__(parent)

        f = open('TEST_RESULTS.txt')
        lines = [line.strip('\n') for line in f.readlines()]

        # Create a push button that links to a file dialog
        self.fileButton = QtGui.QPushButton("Open Results Record")
        self.fileButton.clicked.connect(self.getResults)

        fileLabel = QtGui.QLabel('Record File: ')
        testLabel = QtGui.QLabel('Test Type: ')
        dateLabel = QtGui.QLabel('Date of Test: ')
        timeTakeLabel = QtGui.QLabel('Time Taken to Complete: ')
        accuracyLabel = QtGui.QLabel('Accuracy: ')

        self.file = QtGui.QLabel('Test File')
        self.test = QtGui.QLabel(lines[0])
        self.date = QtGui.QLabel(lines[1])
        self.timeTake = QtGui.QLabel(lines[2])
        self.accuracy = QtGui.QLabel(lines[3])
        fill = QtGui.QLabel('')

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(fileLabel, 1, 0)
        grid.addWidget(self.file, 1, 1)
        grid.addWidget(testLabel, 2, 0)
        grid.addWidget(self.test, 2, 1)
        grid.addWidget(dateLabel, 3, 0)
        grid.addWidget(self.date, 3, 1)
        grid.addWidget(timeTakeLabel, 4, 0)
        grid.addWidget(self.timeTake, 4, 1)
        grid.addWidget(accuracyLabel, 5, 0)
        grid.addWidget(self.accuracy, 5, 1)
        grid.addWidget(self.fileButton, 6, 0, 1, 1)
        grid.addWidget(fill, 7, 0, 10, 5)
        self.setLayout(grid)

    # Uses file dialog to get path to results
    def getResults(self):
        path = QtGui.QFileDialog.getOpenFileName(self, "Open Results File", "", 'Text Files (*.txt)')

        # convert path to a string
        path = str(path)

        # get filename from path
        (dir, name) = os.path.split(path)

        # Read the selected results file, removed newline characters
        f = open(path)
        lines = [line.strip('\n') for line in f.readlines()]

        # Check that the file has at least 4 lines
        if len(lines) < 4:
            title = "Invalid File"
            error = "Please select a valid results file."
            QtGui.QMessageBox.critical(None, title, error, QtGui.QMessageBox.Close)
            return

        self.file = QtGui.QLabel(name)
        self.test = QtGui.QLabel(lines[0])
        self.date = QtGui.QLabel(lines[1])
        self.timeTake = QtGui.QLabel(lines[2])
        self.accuracy = QtGui.QLabel(lines[3])
        return

class WorkThread(QtCore.QThread):
    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        # We can load models from the thread! Yay!
        SceneManager.loadPolygonModel(PATH1, "THREAD")

        # Write to log file because science.
        #f1 = open('printlog.txt', 'a')
        #f1.write('In the thread\n')
        #f1.close()

        # Get button position once since its position is static
        
        #button = SceneManager.getModel(buttonModel)
        button = button(buttonPath,buttonModel)
        buttonPosition = button.getPositionOffset()

        # Get the initial hand position

        #hand = SceneManager.getModel(handButtModel)
        hand = polyModel(handPath,handButtModel)
        handPosition = hand.getPositionOffset()

        #Get the hand navigation model

        navHand = polyModel(navPath, handNavModel)
        navPosition = navHand.getPositionOffset()
        marker = None

        # Wait for a collision with the button
        print("Inital Button Position: "+str(buttonPosition))
        print("Inital Hand Position: "+str(handPosition))
        
        button.attachTrackModel(hand)
        

        # Flag to Double Tap
        buttonflag = 0
        while (1):
            result = navHand.getPositionOffset()

            # User Can Press the Green Marker to Undo
            if marker:
                if (marker.isPressed()):
                    # ?? Does this work?
                    marker.buttonModel.deleteModel()
                    marker = None
                    buttonflag = 0

            # User Presses Button to Mark Answer
            # User Double Taps To Confirm Selection
            if (button.isPressed()):
                # Double Tap/Hold
                if buttonflag == 1:
                    break

                #Draw Green Sphere at Users Answer Location
                marker = button(greenPath, greenModel)
                # Track both hands?
                marker.attachTrackModel(hand)
                marker.setPositionOffset(result[0], result[1], result[2])

                buttonflag += 1
                # Sleep to delay next loop iteration
                time.sleep(2)

         
        #Print results to file.
        #answers in a seperate part of the GUI

        print(">>>> A collision occured <<<<")

        
 

        # Terminate the thread when we are done!! 
        self.terminate()




if __name__ == '__main__':
    import sys
    # Load button and hand models
    SceneManager.loadPolygonModel(navPath, handNavModel)
    SceneManager.loadPolygonModel(handPath, handButtModel)
    SceneManager.loadPolygonModel(buttonPath, buttonModel)

    #Scale Button Hand Models
    SceneManager.getModel(handNavModel).setScale(.02,.02,.02)
    SceneManager.getModel(handNavModel).setPositionOffset(0,1,0)
    SceneManager.getModel(handNavModel).setRotationOffset(1,0,0,1)
    SceneManager.getModel(handButtModel).setScale(.02,.02,.02)
    SceneManager.getModel(handButtModel).setPositionOffset(0,1,0)
    SceneManager.getModel(handButtModel).setRotationOffset(1,0,0,1)

    # Scale button for user to push
    SceneManager.getModel(buttonModel).setPositionOffset(-.4,.15,-.4)
    SceneManager.getModel(buttonModel).setScale(.02,.02,.02)

    # Add models to main view
    SceneManager.addNodeToScene(buttonModel,"mainView")
    SceneManager.addNodeToScene(handNavModel,"mainView")
    SceneManager.addNodeToScene(handButtModel,"mainView")

    # Add models to projector view
    SceneManager.addNodeToScene(buttonModel,"projectorView")
    SceneManager.addNodeToScene(handNavModel,"projectorView")
    SceneManager.addNodeToScene(handButtModel,"projectorView")

    # Attach the rigid bodies
    rbList = ClientHandler.getRigidBodyList()
    numRB = len(rbList)
    print("\nNum of rigid bodies:"+str(numRB))
    # We want to attach only if we have enough rigid bodies
    if numRB > 2:
        SceneManager.getModel(handNavModel).attachRigidBodyById(rbList[0])
        SceneManager.getModel(handButtModel).attachRigidBodyById(rbList[1])
        SceneManager.getModel(buttonModel).attachRigidBodyById(rbList[2])

    # TODO: HOW DO I THROW ERRORS?????????????????????????????????????????
    # We need to complain to the user if 3 rigid bodies aren't hooked up


    # Start the GUI
    app = QtGui.QApplication(sys.argv)
    tabdialog = TabDialog()
    sys.exit(tabdialog.exec_())

