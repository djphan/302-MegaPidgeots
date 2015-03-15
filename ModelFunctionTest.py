import ClientHandler
import SceneManager
import operator
import codecs
import glob
import time
import math

#TODO: put classes in different files

class util():
	@staticmethod
	def euclid(c1, c2):
		return ( math.sqrt( (c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2 ) )

class polyModel():
	def __init__(self,path,name):
		self.model = None
		self.name = name
		self.path = path
		if not(SceneManager.doesModelExist(name)):
			SceneManager.loadPolygonModel(path,name)
			self.model = SceneManager.getModel(name)
			SceneManager.addNodeToScene(name,"mainView")
		else:
			self.model = SceneManager.getModel(name)

	#TODO: test to see if destructor actually works
	def __del__(self):
		SceneManager.deleteModel(self.getName())
		return

	def getName(self):
		return self.name

	def getPath(self):
		return self.path

	def getModel(self):
		if self.model is None:
			print "Model is returning None"
		return self.model

	#TODO: test what it returns when there are no rigidbody attached
	#also not working...?
	def getRigidBody(self):
		return self.getModel().getRigidBody()

	def attachRigidBody(self,rigid_body):
		self.getModel().attachRigidBody(rigid_body)
		return 

	#Set/Get Translation of model in X,Y,Z
	def getPositionOffset(self):
		return self.getModel().getPositionOffset()

	#gets absolute position with the rigidbody taken into account
	#the whole tuple/operator mess adds the values for both tuples for every index.
	#otherwise you end up with (a,b) + (d,e) = (a,b,c,d) instead of (a+c,b+d)
	def getAbsPositionOffset(self):
		return tuple(map(operator.add, self.getPositionOffset(), self.getRigidBody().getPosition()))
		
	def setPositionOffset(self,x,y,z):
		try:
			self.getModel().setPositionOffset(x,y,z)
		except:
			return 1
		return 0

	#Set/Get rotation of model in X,Y,Z,W
	def getRotationOffset(self):
		return self.getModel().getRotationOffset()

	def getAbsRotationOffset(self):
		return tuple(map(operator.add, self.getRotationOffset(), self.getRigidBody().getRotation()))
	
	def setRotationOffset(self,x,y,z,w):
		try:
			self.getModel().setRotationOffset(x,y,z,w)
		except:
			return 1
		return 0

	#Set/Get Scale of model in X,Y,Z
	def getScale(self):
		return self.getModel().getScale()

	def setScale(self,x,y,z):
		try:
			self.getModel().setScale(x,y,z)
		except:
			return 1
		return 0

class polyModelDict():
	def __init__(self):
		self.polyModelDict = {}

	#some wrapped functions to play around with for the time being

	#Return size of dictionary
	def getSize(self):
		return len(self.polyModelDict)

	#Returns the entire dictionary 
	def getDict(self):
		return self.polyModelDict

	#Returns a reference to the polyModel object
	def getPolygonModel(name):
		try:
			return self.polyModelDict[name]
		except:
			return None
		return None

	#Load a polygon model
	def loadPolygonModel(self,path,name):
		self.polyModelDict[name] = polyModel(path,name)
		return
	
	#Deletes a model
	def deletePolygonModel(self,name):
		try:
			self.polyModelDict.pop(name)
		except:
			print("deletePolygonModel - something happened")
			print("name: "+name)
			return 1
		return 0



print "---------------------------------------"
#model path and name
#paths = glob.glob("C:\Users\w\Documents\Models\osg-data-master\*.osg")
paths = glob.glob("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\*.osg")
name = "Cow1"
name2 = "Cow2"
name3 = "Cow3"

#optitrack stuff
#local_IP = "25.79.169.119"
#OptiTrack_IP = "25.79.169.119"
#OptiTrack_DataPort = 1511
#OptiTrack_CmdPort = 1510

#ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
#modelist = list([0]*len(paths))
#test loading multiple models

path = 'C:\Users\w\Documents\Models\osg-data-master\cow.osg'
#path = 'C:\Program Files\ProjectDR\Model\osg-data-master\cow.osg'
#path = 'C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\cow.osg'


model1 = polyModel(path,name)
model2 = polyModel(path,name2)

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
	time.sleep(.125)
	startX -= 0.125
	startZ -= 0.125
	model1.setPositionOffset(startX, startY, startZ)
	model2.setPositionOffset(-startX, startY, -startZ)
	a = model1.getPositionOffset()
	b = model2.getPositionOffset()

model3 = polyModel(path,name3)
model3.setScale(.1,.1,.1)
model3.setPositionOffset(0.0, 0.0,.5)


#write to file
#something.encode("utf-8")
#file = codecs.open("output.txt","w","utf-8")
#file.write(something)
#file.close()

#print("done")