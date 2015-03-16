import ClientHandler
import SceneManager
import operator

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


