import ClientHandler
import SceneManager
import operator
import codecs
import glob


class polyModelDict():
	def __init__(self):
		self.polyModelDict = {}

	#some wrapped functions to play around with for the time being
	def getSize(self):
		return len(self.polyModelDict)

	def getPolygonModel(name):
		try:
			return self.polyModelDict[name]
		except:
			return None
		return None


	def loadPolygonModel(self,path,name):
		try:
			if not(SceneManager.doesModelExist(name)):
				SceneManager.loadPolygonModel(path,name)
				self.polyModelDict[name] = SceneManager.getModel(name)
			else:
				print("loadPolygonModel - a model with specified name already exists")
		except:
			print("loadPolygonModel - something happened")
			#print("path: "+path)
			#print("name: "+name)
			return 1
		return 0

	def deletePolygonModel(self,name):
		try:
			SceneManager.deleteModel(name)
			self.polyModelDict.pop(name)
		except:
			print("deletePolygonModel - something happened")
			#print("name: "+name)
			return 1
		return 0

	def setPositionOffset(self,name,position):
		try:
			self.polyModelDict[name].setPositionOffset(position)
		except:
			return 1
		return 0

	def setRotationOffset(self,name,quat):
		try:
			self.polyModelDict[name].setRotationOffset(quat)
		except:
			return 1
		return 0

	def setScale(self,name,scale):
		try:
			self.polyModelDict[name].setScale(scale)
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
paths = glob.glob("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\*.osg")
#paths = glob.glob("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\osg-data\glider.osg")
name = "hooooooooooo-"

#optitrack stuff
#local_IP = "25.79.169.119"
#OptiTrack_IP = "25.79.169.119"
#OptiTrack_DataPort = 1511
#OptiTrack_CmdPort = 1510

#ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
#modelist = list([0]*len(paths))
#test loading multiple models
polydict = polyModelDict()

modellist = []
for i in range(3):
	polydict.loadPolygonModel(paths[i],name+str(i))
	polydict.setPositionOffset(name+str(i),(90,90,90))
#print(polyModelDict)
print("Size Before: "+str(polydict.getSize()))


#for i in range(3):
	#polydict.deletePolygonModel(name+str(i))

print("Size After: "+str(polydict.getSize()))


#write to file
#something.encode("utf-8")
#file = codecs.open("output.txt","w","utf-8")
#file.write(something)
#file.close()

#print("done")