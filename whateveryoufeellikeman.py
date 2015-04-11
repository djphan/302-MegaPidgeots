from __future__ import print_function
from calibrationWizard import CalibrationWizard
import os
import SceneManager
import ClientHandler
from button import button
from polyModel import polyModel
import time
from util import util
import datetime
from random import randint
from PyQt4 import QtCore, QtGui
from errorMessage import ErrorMessage


# Some global variables: Our Test Names
TEST1 = "Skeleton Full"
TEST2 = "Skeleton Partial"
MODEL1 = "skeleton1"
MODEL2 = "skeleton2"
PATH1 = "Skeleton_Full.OSGB"
PATH2 = "Skeleton_Back.OSGB"
C1Ans = "SkelC1HighLighted.OSGB"
T1Ans = "SkelT1HighLighted.OSGB"
L1Ans = "SkelL1HighLighted.OSGB"


# Keep track of correct answers
CORRECT = 0
CURRENT = 0
# Number of iterations in the test
ITERATIONS = 100

# List of rigid bodies
rbList = []

# Some globals for the results tab
usersAns = ""
correctAns = ""
verdict = ""

# Coordinates of bones to be tested
C1 = (0.1, 0, 0.26)
T1 = (0.1, 0, 0.190)
L1 = (0.1, 0, -0.019)

handNavModel = "NAVIGATION HAND"
handButtModel = "BUTTON HAND"
buttonModel = "Button"
greenModel = "Result Model"
circleModel = "Circle"
C1Model = "C1"
T1Model = "T1"
L1Model = "L1"

# Rigid Bodies attached to each model
rbButtHand = 0
rbNavHand = 0
rbButton = 0

handPath = "BlueSphere.OSGB"
navPath = "OrangeSphere.OSGB"
buttonPath = "HAND.OSGB"
greenPath = "GreenSphere.OSGB"

def print(*arg, **kwargs):
	for args in arg:
		f1 = open('printlog.txt', 'a')
		f1.write(args)
		f1.write("\n")
		f1.close()

# A function for handling individual bone tests
def askForBone(expectedPosition):
	global CORRECT
	global verdict
	global CURRENT
	global usersAns
	global correctAns

	# Set up button
	buttonZ = polyModel(buttonPath, buttonModel)
	#buttonPosition = util.addTuple(buttonZ.getPositionOffset(), rbButton.getPositionOffset())
	buttonPosition = buttonZ.getPositionOffset()

	print("buttonPosition: " + str(buttonPosition))

	# Set up button hand and navigation hand
	hand = polyModel(handPath, handButtModel)
	navHand = polyModel(navPath, handNavModel)
	print("Waiting for button press")
	# Wait for button press
	while (1):
		#print(" Model: " + str(hand.getPositionOffset()))
		#print(str(rbButtHand)+" has id: "+str(rbButtHand.getID())) 
		#print(" Rigid: " + str(rbButtHand.getPosition()))
		handPosition = util.addTuple(hand.getPositionOffset(), rbButtHand.getPosition())
		#print("handPosition:" +str(handPosition))
		time.sleep(0.1)
		if (util.isOver(buttonPosition, handPosition, 0.3, 0.3)):
			# Get the position of the navigation hand and check if it is in the right place
			navPosition = util.addTuple(navHand.getPositionOffset(), rbNavHand.getPosition())
			#print("navPosition: " + str(navPosition))
			if (util.isOver(navPosition, expectedPosition, 0.3, 0.3)):
				CORRECT += 1
				verdict = "Correct!"
				print("Got the correct answer!")
			else:
				verdict = "Incorrect"
				print("Answer was wrong")

			navRBHand = rbNavHand.getPosition()
			SceneManager.getModel(greenModel).setPositionOffset(navRBHand[0], navRBHand[1], navRBHand[2])
			SceneManager.addNodeToScene(greenModel, "projectorView")
			
			# Results tab housekeeping
			CURRENT += 1
			usersAns = str(navPosition)
			correctAns = str(expectedPosition)
			break

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

		# Display Position
		position = QtGui.QLabel("Current Position: (0, 0, 0)")


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
		mainVbox.addWidget(position)
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
		SceneManager.getModel(model).setScale(.025,.025,.025)
		SceneManager.getModel(model).setRotationOffset(0,0,-1,1)
		SceneManager.getModel(model).setPositionOffset(0.105,0.15,-0.711)
		SceneManager.addNodeToScene(model,"mainView")
		SceneManager.addNodeToScene(model,"projectorView")

		# Load Skeleton C1 Answer
		SceneManager.loadPolygonModel(C1Ans, C1Ans)

		#Scale Skeleton
		SceneManager.getModel(C1Ans).setScale(.025,.025,.025)
		SceneManager.getModel(C1Ans).setRotationOffset(0,0,-1,1)
		SceneManager.getModel(C1Ans).setPositionOffset(0.105,0.15,-0.711)
		SceneManager.addNodeToScene(C1Ans,"mainView")

		# Load Skeleton T1 Answer
		SceneManager.loadPolygonModel(T1Ans, T1Ans)

		#Scale Skeleton
		SceneManager.getModel(T1Ans).setScale(.025,.025,.025)
		SceneManager.getModel(T1Ans).setRotationOffset(0,0,-1,1)
		SceneManager.getModel(T1Ans).setPositionOffset(0.105,0.15,-0.711)
		SceneManager.addNodeToScene(T1Ans,"mainView")

		# Load Skeleton
		SceneManager.loadPolygonModel(L1Ans, L1Ans)

		#Scale Skeleton
		SceneManager.getModel(L1Ans).setScale(.025,.025,.025)
		SceneManager.getModel(L1Ans).setRotationOffset(0,0,-1,1)
		SceneManager.getModel(L1Ans).setPositionOffset(0.105,0.15,-0.711)
		SceneManager.addNodeToScene(L1Ans,"mainView")

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

		self.layout = QtGui.QVBoxLayout(self)
		self.button = QtGui.QPushButton("Pull Current Test Results")
		self.connect(self.button, QtCore.SIGNAL("released()"), self.buttonPress)
		self.resultList = QtGui.QListWidget(self)
		self.layout.addWidget(self.button)
		self.layout.addWidget(self.resultList)

		self.threadPool = []

	def updateList(self, text):
		self.resultList.addItem(text)

	def buttonPress(self):
		self.resultList.clear()
		self.threadPool.append(UpdateResultsThread())
		self.connect(self.threadPool[len(self.threadPool)-1], QtCore.SIGNAL("update(QString)"), self.updateList)
		self.threadPool[len(self.threadPool)-1].start()

# A thread to update the UI
class UpdateResultsThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)

	def __del__(self):
		self.wait()

	def run(self):
		global usersAns
		global correctAns
		global CORRECT
		global CURRENT
		self.emit(QtCore.SIGNAL('update(QString)'), "Users Answer: "+usersAns)
		self.emit(QtCore.SIGNAL('update(QString)'), "Expected Answer: "+correctAns)
		self.emit(QtCore.SIGNAL('update(QString)'), verdict)
		if CURRENT == 0:
			self.emit(QtCore.SIGNAL('update(QString)'), "Accuracy: ")
		else:
			percent = (float(CORRECT)/float(CURRENT)) * 100.0
			self.emit(QtCore.SIGNAL('update(QString)'), "Accuracy: "+str(percent)+"%")

# A thread to run the tests on OptiTrack
class WorkThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)

	def __del__(self):
		self.wait()

	def run(self):
		old = 0
		new = 0

		print("Running the Test")

		# Begin timer
		startTime = time.time()
		print("Start Timer")

		for i in range(ITERATIONS):
			# Randomly choose a bone. Make sure we don't ask for same bone twice.
			print("Starting For Loop")
			while new == old:
				new = randint(1, 3)

			print("After While Loop")
			if new == 1:
				print("C1")
				SceneManager.getModel(C1Model).setPositionOffset(0.35, 0, -0.09)
				SceneManager.addNodeToScene(C1Model, "projectorView")
				askForBone(C1)
				SceneManager.removeNodeFromScene(MODEL1, "projectorView")
				SceneManager.addNodeToScene(C1Ans,"projectorView")
				time.sleep(4)
				SceneManager.removeNodeFromScene(C1Ans,"projectorView")
				SceneManager.removeNodeFromScene(C1Model, "projectorView")
			elif new == 2:
				print("T1")
				SceneManager.getModel(T1Model).setPositionOffset(0.35, 0, -0.09)
				SceneManager.addNodeToScene(T1Model, "projectorView")
				askForBone(T1)
				SceneManager.removeNodeFromScene(MODEL1, "projectorView")
				SceneManager.addNodeToScene(T1Ans,"projectorView")
				time.sleep(4)
				SceneManager.removeNodeFromScene(T1Ans,"projectorView")
				SceneManager.removeNodeFromScene(T1Model, "projectorView")
			else:
				print("L1")
				# Display text for bone we want in projector view
				SceneManager.getModel(L1Model).setPositionOffset(0.35, 0, -0.09)
				SceneManager.addNodeToScene(L1Model, "projectorView")
				askForBone(L1)
				SceneManager.removeNodeFromScene(MODEL1, "projectorView")
				SceneManager.addNodeToScene(L1Ans,"projectorView")
				time.sleep(4)
				SceneManager.removeNodeFromScene(L1Ans,"projectorView")
				SceneManager.removeNodeFromScene(L1Model, "projectorView")

			old = new
			SceneManager.removeNodeFromScene(greenModel, "projectorView")
			SceneManager.addNodeToScene(MODEL1,"projectorView")

		# Get the time after the 10 iterations
		endTime = time.time()
		elapsedTime = endTime - startTime
		elapsedTime = str(elapsedTime)+" Seconds"

		# Calculate the accuracy
		accuracy = str((CORRECT/ITERATIONS) * 100);

		# Write results to a file
		date = datetime.datetime.now().strftime("%B %d %I:%M%p")
		testName = "Skeleton Full"


		# Terminate the thread when we are done!!
		self.terminate()




if __name__ == '__main__':
	import sys

	print("Starting")
	# Load button and hand models
	SceneManager.loadPolygonModel(navPath, handNavModel)
	SceneManager.loadPolygonModel(handPath, handButtModel)
	SceneManager.loadPolygonModel(buttonPath, buttonModel)
	SceneManager.loadPolygonModel(greenPath, greenModel)


	# Scale the Green Circle
	SceneManager.getModel(greenModel).setScale(0.01, 0.01, 0.01)
	SceneManager.addNodeToScene(greenModel, "mainView")

	# Create text but do not load into view
	SceneManager.loadPolygonModel("C1.OSGB", C1Model)
	SceneManager.getModel(C1Model).setScale(0.005, 0.005, 0.005)
	SceneManager.getModel(C1Model).setPositionOffset(0.350, 0, -0.090)
	SceneManager.getModel(C1Model).setRotationOffset(0, 0, -1, 1)
	SceneManager.addNodeToScene(C1Model,"mainView")
	#print("Added C1")

	SceneManager.loadPolygonModel("T1.OSGB", T1Model)
	SceneManager.getModel(T1Model).setScale(0.005, 0.005, 0.005)
	SceneManager.getModel(T1Model).setPositionOffset(0.350, 0, -0.090)
	SceneManager.getModel(T1Model).setRotationOffset(0, 0, -1,1)
	SceneManager.addNodeToScene(T1Model,"mainView")

	#print("Added T1")

	SceneManager.loadPolygonModel("L1.OSGB", L1Model)
	SceneManager.getModel(L1Model).setScale(0.005, 0.005, 0.005)
	SceneManager.getModel(L1Model).setPositionOffset(0.350, 0, -0.090)
	SceneManager.getModel(L1Model).setRotationOffset(0, 0, -1, 1)
	SceneManager.addNodeToScene(L1Model,"mainView")

	#print("Added L1")


	print("Added all the models")

	#Scale Button Hand Models
	SceneManager.getModel(handNavModel).setScale(.006,.006,.006)
	SceneManager.getModel(handNavModel).setPositionOffset(0,0.3,0)
	SceneManager.getModel(handNavModel).setRotationOffset(0,0,0,1)
	SceneManager.getModel(handButtModel).setScale(.006,.006,.006)
	SceneManager.getModel(handButtModel).setPositionOffset(0,0.3,0)
	SceneManager.getModel(handButtModel).setRotationOffset(0,0,0,1)

	# Scale button for user to push
	SceneManager.getModel(buttonModel).setPositionOffset(0.267,.15,0.232)
	SceneManager.getModel(buttonModel).setScale(.01,.01,.01)

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
	if numRB > 1:
		SceneManager.getModel(handNavModel).attachRigidBodyById(rbList[0])
		SceneManager.getModel(handButtModel).attachRigidBodyById(rbList[1])
		
		# Get rigid bodies
		rbNavHand = ClientHandler.getRigidBody(rbList[0])
		rbButtHand = ClientHandler.getRigidBody(rbList[1])

		# Start the GUI
		app = QtGui.QApplication(sys.argv)
		tabdialog = TabDialog()
		sys.exit(tabdialog.exec_())
	else:
		app = QtGui.QApplication(sys.argv)
		errormsg = ErrorMessage()
		sys.exit(errormsg.exec_()) 

