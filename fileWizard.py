
"""
A widget for opening modules. Allows the user to select the module
they want to open in their file system with a GUI.
"""
import sys
from PyQt4 import QtGui
import SceneManager

class FileWizard(QtGui.QWidget):
    
    def __init__(self):
        super(FileWizard, self).__init__()
        # Create a push button that links to a file dialog         
        self.fileButton = QtGui.QPushButton("Open a Module")
        self.fileButton.clicked.connect(self.openFile)        
        
        # TODO: Using this as a random variable that the filepath is 
        # being set to for now.
        self.filePath = ''
        
        # Layout for the widget
        mainLayout = QtGui.QVBoxLayout()
        mainLayout.addWidget(self.fileButton)
        self.setLayout(mainLayout)
        self.show()

    # Uses file dialog to get path to module, returns a string
    def openFile(self):
        f = QtGui.QFileDialog.getOpenFileName(self, "Open Module", "")
        # convert filepath to a string
        f = str(f)
        print(f)
        SceneManager.loadPolygonModel(f,"whateveryoufeellikeman")                      
        
        # Not sure what to do with filepath, so im setting it to a variable for now
        self.filePath = f;
        
def main():
    app = QtGui.QApplication(sys.argv)
    ex = FileWizard()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()