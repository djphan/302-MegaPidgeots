"""
A widget for opening modules. Allows the user to select the module
they want to open in their file system with a GUI.
"""
import sys
import os
from PyQt4 import QtGui
# import SceneManager

class FileWizard(QtGui.QWidget):
	def __init__(self):
		super(FileWizard, self).__init__()
		# Create a push button that links to a file dialog
		self.fileButton = QtGui.QPushButton("Open a Module")
		self.fileButton.clicked.connect(self.openFile)

		# Layout for the widget
		mainLayout = QtGui.QVBoxLayout()
		mainLayout.addWidget(self.fileButton)
		self.setLayout(mainLayout)
		self.show()

	# Uses file dialog to get path to module, returns a string
	def openFile(self):
		path = QtGui.QFileDialog.getOpenFileName(self, "Open Module", "")

		# convert path to a string
		path = str(path)
		# get filename from path
		(dir, file) = os.path.split(path)

		# based on the file, pick the name for the model
		if (file == 'Skeleton_FULL.OSGB'):
			model = 'skeleton1'
		elif (file == 'Skeleton_Back.OSGB'):
			model = 'skeleton2'
		else:
			title = "Invalid File"
			error = "Please choose Skeleton_FULL or Skeleton_Back."
			QtGui.QMessageBox.critical(None, title, error, QtGui.QMessageBox.Close)
			return

		# Send the model to scene manager
		SceneManager.loadPolygonModel(path, model)
		return


def main():
	app = QtGui.QApplication(sys.argv)
	ex = FileWizard()
	sys.exit(app.exec_())


if __name__ == '__main__':
	main()