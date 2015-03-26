from PyQt4 import QtGui

class CalibrationWizard(QtGui.QWizard):
    NUM_PAGES = 4
    
    (Intro, Step1, Step2, End) = range(NUM_PAGES)
    
    def __init__(self, parent=None):
        super(CalibrationWizard, self).__init__(parent)
        
        # Add pages to the wizard        
        self.setPage(self.Intro, IntroPage())
        self.setPage(self.Step1, Page1())
        self.setPage(self.Step2, Page2())
        self.setPage(self.End, LastPage())
    
        # Start with IntroPage 
        self.setStartId(self.Intro)    
        
        # Set style to mac for fun, because mac is great
        self.setWizardStyle(self.MacStyle)
    
class IntroPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(IntroPage, self).__init__(parent)
                
        self.setTitle(self.tr("Introduction"))
    
        label = QtGui.QLabel("This wizard will help you calibrate the OptiTrack system.")
        label.setWordWrap(True)
    
        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("pidgey.png")
        pixmap = pixmap.scaledToHeight(400)
        pic.setPixmap(pixmap)
    
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)
        
    def nextId(self):
        return CalibrationWizard.Step1

    
    
class Page1(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Page1, self).__init__(parent)
                
        self.setTitle(self.tr("Step 1"))
    
        label = QtGui.QLabel("This will explain step 1.")
        label.setWordWrap(True)
    
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
    def nextId(self):
        return CalibrationWizard.Step2
    
class Page2(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(Page2, self).__init__(parent)
                
        self.setTitle(self.tr("Step 2"))
    
        label = QtGui.QLabel("This will explain step 2.")
        label.setWordWrap(True)
    
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
    def nextId(self):
        # TODO: If you add more pages, change this link
        return CalibrationWizard.End
        
class LastPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(LastPage, self).__init__(parent)
                
        self.setTitle(self.tr("Last Page"))
    
        label = QtGui.QLabel("Calibration Complete")
        label.setWordWrap(True)
    
        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        self.setLayout(layout)
        
    def nextId(self):
        # Return -1 when done
        return -1

if __name__ == '__main__':

    import sys
    app = QtGui.QApplication(sys.argv)    
    
    wizard = CalibrationWizard()
    wizard.show()

    sys.exit(wizard.exec_())