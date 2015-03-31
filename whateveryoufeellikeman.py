from PyQt4 import QtCore, QtGui
from calibrationWizard import CalibrationWizard
import os
import SceneManager

# Some global variables: Our Test Names
TEST1 = "Skeleton Full"
TEST2 = "Skeleton Partial"
MODEL1 = "skeleton1"
MODEL2 = "skeleton2"

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
			path = "C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\Skeleton_Full.OSGB"
		else:
			path = "C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\Skeleton_Back.OSGB"

		# Notify the user that model was successfully loaded.
		title = "Model Loaded"
		error = "Model was successfully loaded into ProjectDr."
		QtGui.QMessageBox.information(None, title, error, QtGui.QMessageBox.Ok)

		# Send the model to scene manager
		SceneManager.loadPolygonModel(path, model)
		SceneManager.getModel(model).setScale(.05,.05,.05)
		SceneManager.getModel(model).setRotationOffset(0,0,-1,1)
		SceneManager.getModel(model).setPositionOffset(0,0,-1.4)
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




if __name__ == '__main__':

	import sys

	app = QtGui.QApplication(sys.argv)

	tabdialog = TabDialog()
	sys.exit(tabdialog.exec_())
