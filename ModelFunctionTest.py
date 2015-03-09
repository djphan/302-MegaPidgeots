import ClientHandler
import SceneManager
import operator
import codecs
import glob

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


	#Returns a reference to the polygon model
	def getPolygonModel(name):
		try:
			return self.polyModelDict[name]
		except:
			return None
		return None


	#Load a polygon model
	def loadPolygonModel(self,path,name):
		try:
			if not(SceneManager.doesModelExist(name)):
				SceneManager.loadPolygonModel(path,name)
				self.polyModelDict[name] = SceneManager.getModel(name)
			else:
				print("loadPolygonModel - a model with specified name already exists")
		except:
			print("loadPolygonModel - something happened")
			print("path: "+path)
			print("name: "+name)
			return 1
		return 0
	

	#Deletes a model
	def deletePolygonModel(self,name):
		try:
			SceneManager.deleteModel(name)
			self.polyModelDict.pop(name)
		except:
			print("deletePolygonModel - something happened")
			print("name: "+name)
			return 1
		return 0


	#Set/Get Translation of model in X,Y,Z
	def getPositionOffset(self,name):
		return self.polyModelDict[name].getPositionOffset()

	def setPositionOffset(self,name,position):
		try:	
			if len(position) == 3:
				self.polyModelDict[name].setPositionOffset(position[0],position[1],position[2])
			else:
				print "invalid position input"
				return 1
		except:
			return 1
		return 0

	#Set/Get rotation of model in X,Y,Z,W
	def getRotationOffset(self,name):
		return self.polyModelDict[name].getRotationOffset()

	def setRotationOffset(self,name,quat):
		try:
			if len(quat) == 4:
				self.polyModelDict[name].setRotationOffset(quat[0],quat[1],quat[2],quat[3])
			else:
				print"invalid rotation input"
				return 1
		except:
			return 1
		return 0

	#Set/Get Scale of model in X,Y,Z
	def getScale(self,name):
		return self.polyModelDict[name].getScale()

	def setScale(self,name,scale):
		try:
			if len(scale) == 3:
				self.polyModelDict[name].setScale(scale[0],scale[1],scale[2])
			else:
				print"invalid scale input"
			return 1
		except:
			return 1
		return 0

	def attachRigidBody(self,name,rigid_body):
		try:
			self.polyModelDict[name].attachRigidBody[rigid_body]
		except:
			return 1
		return 0



#model path and name
paths = glob.glob("C:\Users\w\Documents\Models\osg-data-master\*.osg")
#path = "C:\Users\w\Documents\Models\osg-data-master\glider.osg"
name = "hooooooooooo- "

#optitrack stuff
#local_IP = "25.79.169.119"
#OptiTrack_IP = "25.79.169.119"
#OptiTrack_DataPort = 1511
#OptiTrack_CmdPort = 1510

#ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
#modelist = list([0]*len(paths))
#test loading multiple models

path = 'C:\Program Files\ProjectDR\Model\osg-data-master\cessna.osg'

polyDict = polyModelDict()

polyDict.loadPolygonModel(path,name)

print "position: "+str(polyDict.getPositionOffset(name))
print "rotation: "+str(polyDict.getRotationOffset(name))
print "scale: "+str(polyDict.getScale(name))
polyDict.setPositionOffset(name,(1.0,2.0,4.0))
polyDict.setRotationOffset(name,(1.0,2.0,4.0,8.0))
polyDict.setScale(name,(1.0,2.0,4.0))
print "position: "+str(polyDict.getPositionOffset(name))
print "rotation: "+str(polyDict.getRotationOffset(name))
print "scale: "+str(polyDict.getScale(name))


#write to file
#something.encode("utf-8")
#file = codecs.open("output.txt","w","utf-8")
#file.write(something)
#file.close()

#print("done")