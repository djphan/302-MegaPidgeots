from PyQt4 import QtCore, QtGui
from calibrationWizard import CalibrationWizard
#import SceneManager

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

# This tab deals with OptiTrack setup and calibration.
class CalibrationTab(QtGui.QWidget):
	def __init__(self, parent=None):
		super(CalibrationTab, self).__init__(parent)

		# The tabs contains a button to open the wizard.
		self.text = QtGui.QLabel("The calibration wizard can be used to guide you through OptiTrack setup.")
		self.button = QtGui.QPushButton("Open Wizard")
		self.button.resize(self.button.sizeHint())
		self.button.clicked.connect(self.openWizard)

		# Layout for the widget
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(self.text)
		mainLayout.addWidget(self.button)
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
		combo = QtGui.QComboBox(self)
		combo.addItem("Skeleton Full")
		combo.addItem("Skeleton Partial")

		# Test image
		self.img = QtGui.QLabel(self)
		pixmap = QtGui.QPixmap('spooky.png')
		pixmap = pixmap.scaledToHeight(400)
		self.img.setPixmap(pixmap)

		# Set the default test to be displayed on launch in text description box
		self.descriptionText = QtGui.QLabel("Tests vertebrae for sections C1 through C7.", self)

		# Add sub-widgets to the main layout
		mainVbox = QtGui.QVBoxLayout()
		mainVbox.stretch(1)
		mainVbox.addWidget(instruText)
		mainVbox.addWidget(combo)
		mainVbox.addWidget(self.descriptionText)
		mainVbox.addWidget(self.img)
		self.setLayout(mainVbox)

		# Create the drop down list on the window
		combo.activated['QString'].connect(self.onActivated)
		self.show()

	# When the user selects an item from the list, display its information
	def onActivated(self, text):
		if text == "Skeleton Full":
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

		resultsLabel = QtGui.QLabel("Results")
		result1 = QtGui.QLabel("Result 1")
		result2 = QtGui.QLabel("Result 2")
		result3 = QtGui.QLabel("Result 3")
		result4 = QtGui.QLabel("Result 4")

		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(resultsLabel)
		mainLayout.addWidget(result1)
		mainLayout.addWidget(result2)
		mainLayout.addWidget(result3)
		mainLayout.addWidget(result4)
		mainLayout.addStretch(1)
		self.setLayout(mainLayout)


if __name__ == '__main__':

	import sys

	app = QtGui.QApplication(sys.argv)

	tabdialog = TabDialog()
	sys.exit(tabdialog.exec_())
