import 
import operator

class util():
	@staticmethod
	def euclid(c1, c2):
		return ( math.sqrt( (c2[0] - c1[0])**2 + (c2[1] - c1[1])**2 + (c2[2] - c1[2])**2 ) )

	@staticmethod
	def addTuple(t1, t2):
		return tuple(map(operator.add, t1,t2))

	@staticmethod
	def test():
		print "hooooooooooooo"
		return

	@staticmethod
	def alwaysTrue():
		return True 

	@staticmethod
	def alwaysFalse():
		return False 


	@staticmethod
	def isOver(pos1,pos2,w,l): 
		#pos1 and pos2 is a length 3 tuple, where pos1 is the acting button with width and height w,l and pos2 is the thing pressing the button
		X1 = pos1[0] - w/2.0
		X2 = pos1[0] + w/2.0
		Z1 = pos1[2] - l/2.0
		Z2 = pos1[2] + l/2.0
		return ((pos2[0]>=X1 and pos2[0]<=X2) and (pos2[2]>=Z1 and pos2[2]<=Z2))

	#pos1 and pos2 is a length 3 tuple, where pos1 is the acting button with width and height w,l and pos2 is the thing pressing the button
	#pressed dist is the minimum distance between the two on the y axis in order to be considered pressed
	@staticmethod
	def isPressed(pos1,pos2,w,l,pressdist):
		X1 = pos1[0] - w/2.0
		X2 = pos1[0] + w/2.0
		Z1 = pos1[2] - l/2.0
		Z2 = pos1[2] + l/2.0

		return (((pos2[0]>=X1 and pos2[0]<=X2) and (pos2[2]>=Z1 and pos2[2]<=Z2)) and (abs(pos1[1] - pos2[1])<pressdist))
	
