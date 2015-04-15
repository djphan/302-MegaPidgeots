"""
Opens an error message in place of the default UI if the user tries to start our app without having
at least 3 rigid bodies initialized in ProjectDr.
"""

import sys
from PyQt4 import QtGui, QtCore

class ErrorMessage(QtGui.QMainWindow):
	def __init__(self):
		super(ErrorMessage, self).__init__()

		title = "Error"
		error = "2 rigid bodies must be initialized in Motive before tests can be run."
		QtGui.QMessageBox.critical(None, title, error, QtGui.QMessageBox.Close)
		exit(0)

def main():
	app = QtGui.QApplication(sys.argv)
	ex = ErrorMessage()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
