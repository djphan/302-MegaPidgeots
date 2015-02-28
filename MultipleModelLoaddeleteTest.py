import ClientHandler
import SceneManager
import operator
import codecs
import glob

#model path and name
paths = glob.glob("C:\Users\w\Documents\Models\osg-data-master\*.osg")
#path = "C:\Users\w\Documents\Models\osg-data-master\glider.osg"
name = "hooooooooooo- "

#optitrack stuff
local_IP = "25.79.169.119"
OptiTrack_IP = "25.79.169.119"
OptiTrack_DataPort = 1511
OptiTrack_CmdPort = 1510

#ClientHandler.connect(local_IP,OptiTrack_IP,OptiTrack_DataPort,OptiTrack_CmdPort,ClientHandler.ConnectionType.Multicast)

#load model from path
#modelist = list([0]*len(paths))
#test loading multiple models
modellist = []
for i in range(3):
	print "loading"+name+paths[i]
	SceneManager.loadPolygonModel(paths[i],name+paths[i])
	modellist.append(SceneManager.getModel(name+paths[i]))

print str(len(modellist))+" length of list after adding models"
print modellist

for i in range(len(modellist)):
	SceneManager.deleteModel(name+paths[i])
	print "deleting"+name+paths[i]

print str(len(modellist))+" length of list after removing the models"
print modellist
#todo: remove all the references to the model after removing model (aka: call delete on list on specified index) 


#output test, replace with infinite loop with a keyboard event to break 
#something = ""
#while i in range (1000):
#	something += str(model.getPositionOffset())+"\n"

#write to file
#something.encode("utf-8")
#file = codecs.open("output.txt","w","utf-8")
#file.write(something)
#file.close()

#print("done")