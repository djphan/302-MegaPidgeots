import math

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
