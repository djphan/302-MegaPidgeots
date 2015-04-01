import whateveryoufeellikeman
import time
from PyQt4 import QtCore, QtGui
from multiprocessing import Process

# Process with our infinite while loop inside
def myProcess(name):
	while 1:
		print "Forever"
		time.sleep(2)


if __name__ == '__main__':
	import sys

	# Create a process for the UI
	p = Process(target=myProcess, args=('Args go here if i needed them',))
	p.start()

	# Start our UI
	app = QtGui.QApplication(sys.argv)
	tabdialog = whateveryoufeellikeman.TabDialog()

	# The UI blocks until closed. On exit, get the code.
	code = tabdialog.exec_()

	# Since out UI is done, kill the process.
	p.terminate()
	sys.exit(code)
