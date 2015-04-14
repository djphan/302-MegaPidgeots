'''
Each calibration step is associated with a wizard page. The page is named after the image name.
'''

from PyQt4 import QtGui


class CalibrationWizard(QtGui.QWizard):
    NUM_PAGES = 16

    # Each page is assigned a unique ID. I used numbers 0 to 15.
    (Intro, Block, Calculate, StartCalibration, Wifi, Calculating, Calculate, CameraSettings, DataStreaming, DataStream,
     MakeRigidBody, SelectRigidBody, Menu, DataStream, ProjectDr, End) = range(NUM_PAGES)

    def __init__(self, parent=None):
        super(CalibrationWizard, self).__init__(parent)

        # Add each page to the wizard
        # TODO: Pages point to the wrong ones currently. (See each nextId function in each class)
        self.setPage(self.Intro, IntroPage())
        self.setPage(self.Block, BlockingPage())
        self.setPage(self.Calculate, CalculatePage())
        self.setPage(self.StartCalibration, StartCalibrationPage())
        self.setPage(self.Wifi, WifiPage())
        self.setPage(self.Calculating, CalculatingPage())
        self.setPage(self.CameraSettings, CameraSettingsPage())
        self.setPage(self.DataStreaming, DataStreamingPage())
        self.setPage(self.MakeRigidBody, MakeRigidBodiesPage())
        self.setPage(self.SelectRigidBody, SelectRigidBodiesPage())
        self.setPage(self.Menu, MenuPage())
        self.setPage(self.DataStream, DataStreamPage())
        self.setPage(self.ProjectDr, ProjectDrPage())
        self.setPage(self.End, LastPage())

        # Start with IntroPage
        self.setStartId(self.Intro)

        # Set style to mac for fun, because mac is great
        self.setWizardStyle(self.MacStyle)

        self.resize(1200, 780)
        self.centerWindow()

        # A function to move the window to the center of the users screen

    def centerWindow(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class IntroPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(IntroPage, self).__init__(parent)

        self.setTitle(self.tr("Introduction"))

        label = QtGui.QLabel("This wizard will guide you through calibrating the OptiTrack system, and ProjectDR setup \n")
        label.setWordWrap(True)


        label1 = QtGui.QLabel("""1. Begin by inserting OptiTrack Hardware Key into system \n""")
        label1.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("hardwarekey.jpg")
        pic.setPixmap(pixmap)

        label2 = QtGui.QLabel("""2. Connect the and setup the projector \n""")
        label2.setWordWrap(True)

        label3 = QtGui.QLabel("""3. Launch the following programs: Motive\n""")
        label3.setWordWrap(True)

        pic1 = QtGui.QLabel()
        pixmap = QtGui.QPixmap("motiveLogo.png")
        pic1.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(pic)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(pic1)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.Menu


class StartCalibrationPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(StartCalibrationPage, self).__init__(parent)

        self.setTitle(self.tr("Start Calibration"))

        label = QtGui.QLabel("This will explain how to start calibration.")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("StartCalibration.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.Menu


class WifiPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(WifiPage, self).__init__(parent)

        self.setTitle(self.tr("Wifi"))

        label = QtGui.QLabel("Turn off system Wireless to ensure no inteferance with Motive server")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Wifi.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.DataStream


class BlockingPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(BlockingPage, self).__init__(parent)

        self.setTitle(self.tr("Blocking"))

        label = QtGui.QLabel("If unwanted markers appear in camera preview select block to remove them")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Blocking.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.Calculate


class CalculatingPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(CalculatingPage, self).__init__(parent)

        self.setTitle(self.tr("Calculating"))

        label = QtGui.QLabel("When satisfied with your wanding select \"Calculate\" and \"Apply result\"")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Calculating.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.MakeRigidBody


class CameraSettingsPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(CameraSettingsPage, self).__init__(parent)

        self.setTitle(self.tr("Camera Settings"))

        label = QtGui.QLabel("Adjust camera settings until rigid bodys appear on camera preview")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("CameraSettings.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.Block


class DataStreamingPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(DataStreamingPage, self).__init__(parent)

        self.setTitle(self.tr("Data Streaming"))

        label = QtGui.QLabel("Choose the following settings and check \"Broadcast Frame Data\"")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("DataStreaming.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.ProjectDr


class MakeRigidBodiesPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(MakeRigidBodiesPage, self).__init__(parent)

        self.setTitle(self.tr("Make Rigid Bodies"))

        label = QtGui.QLabel("Create three rigid bodies by placing the rigid bodies under the camera one-by-one and selecting \"Create from Visible\"")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("MakeRigidBodies.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.SelectRigidBody


class MenuPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(MenuPage, self).__init__(parent)

        self.setTitle(self.tr("Menu"))

        label = QtGui.QLabel("Begin calibration by selecting \"Perform Camera Calibration\"")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Menu.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.CameraSettings


class ProjectDrPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(ProjectDrPage, self).__init__(parent)

        self.setTitle(self.tr("ProjectDr"))

        label = QtGui.QLabel("Connect OptiTrack in ProjectDr and follow their Project Calibration Wizard")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("ProjectDr.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.End


class SelectRigidBodiesPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(SelectRigidBodiesPage, self).__init__(parent)

        self.setTitle(self.tr("Select Rigid Bodies"))

        label = QtGui.QLabel("Select the rigid bodies to be sent to ProjectDR")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Select RigidBodies.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.Wifi


class DataStreamPage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(DataStreamPage, self).__init__(parent)

        self.setTitle(self.tr("Data Stream"))

        label = QtGui.QLabel("Select \"Data Streaming\" under the \"View\" Tab")
        label.setWordWrap(True)

        layout = QtGui.QVBoxLayout()
        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("DataStream.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        return CalibrationWizard.DataStreaming


class CalculatePage(QtGui.QWizardPage):
    def __init__(self, parent=None):
        super(CalculatePage, self).__init__(parent)

        self.setTitle(self.tr("Wanding"))

        label = QtGui.QLabel("Select \"Start Wanding\" and sweep the OptiTrack Wand in front of cameras")
        label.setWordWrap(True)

        pic = QtGui.QLabel()
        pixmap = QtGui.QPixmap("Calculate.png")
        pic.setPixmap(pixmap)

        layout = QtGui.QVBoxLayout()
        layout.addWidget(label)
        layout.addWidget(pic)
        self.setLayout(layout)

    def nextId(self):
        # TODO: If you add more pages, change this link
        return CalibrationWizard.Calculating


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