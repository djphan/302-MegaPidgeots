from polyModel import polyModel


class button():
	def __init__(self,path,name):
		self.buttonModel = polyModel(path,name)
		self.trackModel = None
		self.width = 1.0
		self.length = 1.0
		self.overDist = 10
		self.pressedDist = 0.05
		self.over = False
		self.pressed = False

	def attachTrackModel(self,polyModel):
		self.trackModel = polyModel
		return

	def isOver(self):
		trackPos = self.trackModel.getAbsPositionOffset()
		buttonPos = self.trackModel.getPositionOffset()

		X1 = buttonPos[0] - self.width/2
		X2 = buttonPos[0] + self.width/2
		Y1 = buttonPos[1] - self.length/2
		Y2 = buttonPos[1] + self.length/2

		return (trackPos[0]>=X1 and trackPos[0]<=X2) and (trackPos[0]>=Y1 and trackPos[0]<=Y2) and (abs(trackPos[2] - buttonPos[2]) < overDist)


	def isPressed(self):
		trackPos = self.trackModel.getAbsPositionOffset()
		buttonPos = self.trackModel.getPositionOffset()

		X1 = buttonPos[0] - self.width/2
		X2 = buttonPos[0] + self.width/2
		Y1 = buttonPos[1] - self.length/2
		Y2 = buttonPos[1] + self.length/2

		return (trackPos[0]>=X1 and trackPos[0]<=X2) and (trackPos[0]>=Y1 and trackPos[0]<=Y2) and (abs(trackPos[2] - buttonPos[2]) < pressedDist)

	def removeButton(self):
		self.buttonModel.deleteModel()

	def setPositionOffset(self,x,y,z):
		try:
			self.buttonModel.setPositionOffset(x,y,z)
		except:
			return 1
		return 0


	def setRotationOffset(self,x,y,z,w):
		try:
			self.buttonModel.setRotationOffset(x,y,z,w)
		except:
			return 1
		return 0

	def setScale(self,x,y,z):
		try:
			self.buttonModel.setScale(x,y,z)
		except:
			return 1
		return 0