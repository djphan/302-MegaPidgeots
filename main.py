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
buttonpath = "C:\Users\w\Desktop\Button2.OSGB"
name = "Cow1"
name2 = "Cow2"
name3 = "Cow3"

#optitrack stuff
local_IP = "172.28.25.246"
OptiTrack_IP = "172.28.25.246"
OptiTrack_DataPort = 1511
OptiTrack_CmdPort = 1510

ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
#modelist = list([0]*len(paths))
#test loading multiple models

path = 'C:\Users\w\Documents\Models\osg-data-master\cow.osg'
#path = 'C:\Program Files\ProjectDR\Model\osg-data-master\cow.osg'
#path = 'C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\cow.osg'


model1 = polyModel(path,name)
model2 = polyModel(path,name2)
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

model1.setPositionOffset(startX, startY, startZ)
model2.setPositionOffset(-startX, startY, startZ)
model1.setScale(.1,.1,.1)
model2.setScale(.1,.1,.1)

a = model1.getPositionOffset()
b = model2.getPositionOffset()
while ( util.euclid(a,b) > .8):
	time.sleep(.050)
	startX -= 0.050
	startZ -= 0.050
	model1.setPositionOffset(startX, startY, startZ)
	model2.setPositionOffset(-startX, startY, -startZ)
	model1.setRotationOffset(random.uniform(0,360),random.uniform(0,360),random.uniform(0,360),1)
	model2.setRotationOffset(random.uniform(0,360),random.uniform(0,360),random.uniform(0,360),1)
	a = model1.getPositionOffset()
	b = model2.getPositionOffset()

model3 = polyModel(path,name3)
model3.setScale(.1,.1,.1)
model3.setPositionOffset(0.0, 0.0,.5)
model3.attachRigidBodyById(0)
time.sleep(10)

model1.deleteModel()
model2.deleteModel()
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