from polyModel import polyModel

class button():
	def __init__(self,path,name):
		self.buttonModel = polyModel(path,name)
		self.trackModel = None
		self.width = 1.0
		self.length = 1.0
		self.pressedDist = 0.05
		self.over = False
		self.pressed = False


	def attachTrackModel(self,polyModel):
		self.trackModel = polyModel
		return

	def isOver(self):
		trackPos = self.trackModel.getAbsPositionOffset()
		buttonPos = self.buttonModel.getPositionOffset()

		X1 = buttonPos[0] - self.width/2
		X2 = buttonPos[0] + self.width/2
		Z1 = buttonPos[2] - self.length/2
		Z2 = buttonPos[2] + self.length/2
		print str(X1)+","+str(X2)+","+str(trackPos[0])+"is Over X"
		print str(Z1)+","+str(Z2)+","+str(trackPos[0])+"is over Z"
		return (trackPos[0]>=X1 and trackPos[0]<=X2) and (trackPos[2]>=Z1 and trackPos[2]<=Z2)


	def isPressed(self):
		trackPos = self.trackModel.getAbsPositionOffset()
		buttonPos = self.buttonModel.getPositionOffset()

		X1 = buttonPos[0] - self.width/2
		X2 = buttonPos[0] + self.width/2
		Z1 = buttonPos[2] - self.length/2
		Z2 = buttonPos[2] + self.length/2
		print trackPos[1]
		return (trackPos[0]>=X1 and trackPos[0]<=X2) and (trackPos[2]>=Z1 and trackPos[2]<=Z2) and (abs(trackPos[1]) < self.pressedDist)

	def removeButton(self):
		self.buttonModel.deleteModel()

	def setPositionOffset(self,x,y,z):
		try:
			self.buttonModel.setPositionOffset(x,y,z)
		except:
			return 1
		return 0

	def getPositionOffset(self):
		return self.buttonModel.getPositionOffset()

	def setRotationOffset(self,x,y,z,w):
		try:
			self.buttonModel.setRotationOffset(x,y,z,w)
		except:
			return 1
		return 0

	def getRotationOffset(self):
		return self.buttonModel.getRotationOffset(self)

	def setScale(self,x,y,z):
		try:
			self.buttonModel.setScale(x,y,z)
		except:
			return 1
		return 0

	def getScale(self):
		return self.buttonModel.getScale()
