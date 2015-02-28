import ClientHandler
import SceneManager
import operator
import codecs

#model path and name
path = "C:\Users\w\Documents\Models\osg-data-master\glider.osg"
name = "somethingyouwant"

#optitrack stuff
local_IP = "25.79.169.119"
OptiTrack_IP = "25.79.169.119"
OptiTrack_DataPort = 1511
OptiTrack_CmdPort = 1510

ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
SceneManager.loadPolygonModel(path,name)
model = SceneManager.getModel(name)

#output test, replace with infinite loop with a keyboard event to break 
something = ""
while i in range (1000):
	something += str(model.getPositionOffset())+"\n"

#write to file
something.encode("utf-8")
file = codecs.open("output.txt","w","utf-8")
file.write(something)
file.close()

print("done")