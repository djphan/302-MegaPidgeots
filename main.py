import ClientHandler
import SceneManager
import sys
sys.path.insert(0, "C:\\302thing\\302-MegaPidgeots") #set path to project folder
sys.path.insert(0, "C:\\Users\\Aedan\\Desktop\\Homework Folder\\CMPUT 302\\302-MegaPidgeots")

#from PyQt4 import QtGui, QtCore
import codecs
import glob
import time
import math
import random

from util import util
from polyModel import polyModel
from polyModel import polyModelDict
from button import button
#import mainmenu

print "---------------------------------------"
#model path and name
#paths = glob.glob("C:\Users\w\Documents\Models\osg-data-master\*.osg")
#paths = glob.glob("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\*.osg")
buttonpath = "C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\Button2.osgb"
handpath = "C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\hand.osgb"
markerpath = "C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\Marker.osgb"

#optitrack stuff
local_IP = "172.28.25.246"
OptiTrack_IP = "172.28.25.246"
OptiTrack_DataPort = 1511
OptiTrack_CmdPort = 1510

ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#path = 'C:\Users\w\Documents\Models\osg-data-master\cow.osg'
#path = 'C:\Program Files\ProjectDR\Model\osg-data-master\cow.osg'
#path = 'C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\cow.osg'

button = button(buttonpath,"button")

"""
print "position: "+str(model1.getPositionOffset())
print "rotation: "+str(model1.getRotationOffset())
print "scale: "+str(model1.getScale())
model1.setPositionOffset(0.2,0.5,0.2)
model1.setRotationOffset(1.0,2.0,4.0,1.0)
model1.setScale(name,(0.1,0.1,0.1)
print "position: "+str(model1.getPositionOffset())
print "rotation: "+str(model1.getRotationOffset())
print "scale: "+str(model1.getScale())
"""

startX = 10.0
startY = 0.0
startZ = 10.0

#THIS LINE SHOULD NOT BE NECESSARY
SceneManager.loadPolygonModel("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\Skeleton_Full.osgb","skeleton1")

if (SceneManager.doesModelExist("skeleton1") == True):
	skeleton = SceneManager.getModel("skeleton1")
	SceneManager.addNodeToScene("skeleton1","mainView")
elif (SceneManager.doesModelExist("skeleton1") == True):
	skeleton = SceneManager.getModel("skeleton2")
	SceneManager.addNodeToScene("skeleton2","mainView")

hand = polyModel(handpath,"hand")
hand.getModel().attachRigidBodyById(0)


a = hand.getPositionOffset()
b = skeleton.getPositionOffset()
while ( util.euclid(a,b) > -1):
	time.sleep(.050)
	#startX -= 0.050
	#startZ -= 0.050
	#model1.setPositionOffset(startX, startY, startZ)
	#model2.setPositionOffset(-startX, startY, -startZ)
	#model1.setRotationOffset(random.uniform(0,360),random.uniform(0,360),random.uniform(0,360),1)
	#model2.setRotationOffset(random.uniform(0,360),random.uniform(0,360),random.uniform(0,360),1)
	a = hand.getPositionOffset()
	b = skeleton.getPositionOffset()

model3 = polyModel(markerpath,"Marker")
model3.setScale(.1,.1,.1)
model3.setPositionOffset(0.0, 0.0,.5)
model3.attachRigidBodyById(1)
time.sleep(10)

skeleton.deleteModel()
hand.getModel().deleteModel()
model3.deleteModel()

'''
app = QtGui.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec_())
'''

#write to file
#something.encode("utf-8")
#file = codecs.open("output.txt","w","utf-8")
#file.write(something)
#file.close()

#print("done")