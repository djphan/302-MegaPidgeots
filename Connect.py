import ClientHandler
import SceneManager
import glob

path = "C:\Users\w\Documents\Models\osg-data-master\glider.osg"
name = "somethingyouwant"

paths = glob.glob("C:\Users\Aedan\Desktop\Homework Folder\CMPUT 302\DICOM Models\COU\*.dcm")
for i in paths:
	i = i[66:]
	print i


local_IP = "25.79.169.119"
OptiTrack_IP = "25.79.169.119"
OptiTrack_DataPort = 1511
OptiTrack_CmdPort = 1510


ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)
SceneManager.loadPolygonModel(path,name)
model = SceneManager.getModel(name)