import sys, time
from PyQt4 import QtCore, QtGui


class MyApp(QtGui.QWidget):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)

		self.setGeometry(300, 300, 280, 600)
		self.setWindowTitle('threads')

		self.layout = QtGui.QVBoxLayout(self)

		self.testButton = QtGui.QPushButton("test")
		self.connect(self.testButton, QtCore.SIGNAL("released()"), self.buttonPress)
		self.listwidget = QtGui.QListWidget(self)

		self.layout.addWidget(self.testButton)
		self.layout.addWidget(self.listwidget)

		self.threadPool = []

	# This function adds items to the results list
	def updateList(self, text):
		self.listwidget.addItem(text)
		self.listwidget.sortItems()

	# When button is pressed this function is called
	def buttonPress(self):
		self.listwidget.clear()
		# adding by emitting signal in different thread
		self.threadPool.append(UpdateResultsThread())
		self.connect(self.threadPool[len(self.threadPool) - 1], QtCore.SIGNAL("update(QString)"), self.updateList)
		self.threadPool[len(self.threadPool) - 1].start()

# A thread to update the UI
class UpdateResultsThread(QtCore.QThread):
	def __init__(self):
		QtCore.QThread.__init__(self)

	def __del__(self):
		self.wait()

	def run(self):
		self.emit(QtCore.SIGNAL('update(QString)'), "Users Answer: ")
		self.emit(QtCore.SIGNAL('update(QString)'), "Expected Answer: ")
		self.emit(QtCore.SIGNAL('update(QString)'), "Success!")
		self.emit(QtCore.SIGNAL('update(QString)'), "Time Taken: ")
		self.emit(QtCore.SIGNAL('update(QString)'), "Accuracy: ")
		return


# run
app = QtGui.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()