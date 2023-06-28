import maya.cmds as cmds
import os
import sys
usd = cmds.internalVar(usd=True)
version = cmds.about(version=True)
dirWithoutVersion = usd.replace(str(version)+ "/", "")
mayaDirectory = dirWithoutVersion.replace("/scripts/", "")
path = mayaDirectory + "/JM_Custom_Maya_Tools"
scriptsFolder = path + '/Scripts'
var = cmds.optionVar(sv =("JMDirectory", path))

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)
import InitilizeTools
import JMCustomMarkingMenu
srcWindows = path + '/Scripts/userSetup.mel'
destWindows = mayaDirectory + "/" +  version + '/scripts/userSetup.mel'
print(destWindows)
if os.path.exists(destWindows):
    cmds.warning("userSetup.mel alread exists, this is being skipped, you will need to make sure that " + destWindows + " contains the the lines of code inside of " + srcWindows)
else:
    
    cmds.sysFile( srcWindows, copy=destWindows )



iconsFolder = path + '/Icons'

shelfLevel = mel.eval("$tmpVar=$gShelfTopLevel")
icon = iconsFolder + '/CustomToolsIcon.png'
command = "import os\nimport sys\nuser = os.environ.get('USER')\nscriptsFolder = cmds.optionVar(q = 'JMDirectory') + '/Scripts'\nif scriptsFolder not in sys.path:\n    sys.path.append(scriptsFolder)\nimport InitilizeTools\nInitilizeTools.CustomToolsJM()"
shelf = cmds.tabLayout(shelfLevel, query=1, ca=1, selectTab = True)

cmds.shelfButton(p = shelf, image1 = icon, command = command)
JMCustomMarkingMenu.JMCustomToolsMarkingMenu()
InitilizeTools.CustomToolsJM()
