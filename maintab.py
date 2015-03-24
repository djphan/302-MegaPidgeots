import sys
from PyQt4 import QtGui, QtCore

'''
Page with test results
'''
class MainTabWidget(QtGui.QWidget):
    

    def __init__(self):
        super(MainTabWidget, self).__init__()
        self.initUI()
        
    # Initilize the UI of the window
    def initUI(self):
        page = QtGui.QVBoxLayout()

        # Instructions text box
        instruText = QtGui.QLabel("How to Cailbrate OptiTrack")
        font = QtGui.QFont()
        font.setPointSize(18)
        instruText.setFont(font)

        # Instructions
        self.step1 = QtGui.QLabel("Step 1: Select Cailbrate", self)
        self.step2 = QtGui.QLabel("Step 2: Wave Wand Around", self)
        self.step3 = QtGui.QLabel("Step 3: Apply Cailbrations", self)

        menu_bar = QtGui.QMenuBar() 
        file = menu_bar.addMenu("&File") 
        help = menu_bar.addMenu("&Help")
        
        # Test image

        pic = QtGui.QLabel()
        pic.setPixmap(QtGui.QPixmap('pidgey.png'))

        addTestAction = QtGui.QAction(QtGui.QIcon('pigeot_icon.png'), '&AddTest' , self)
        addTestAction.setStatusTip("Add Test")
        
        page.addWidget(instruText)
        page.addWidget(self.step1)
        page.addWidget(self.step2)
        page.addWidget(self.step3)
        page.addWidget(pic)

        mainVbox = QtGui.QVBoxLayout()
        mainVbox.addWidget(menu_bar)

        self.setLayout(page)       
        self.show()
                
def main():
    app = QtGui.QApplication(sys.argv)
    window = MainTabWidget()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()