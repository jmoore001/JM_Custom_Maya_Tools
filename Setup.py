import maya.cmds as cmds
import os
import sys

user = os.environ.get('USER')
path = 'C:/Users/' + user + '/Documents/maya/JM_Custom_Maya_Tools/Scripts'
if path not in sys.path:
    sys.path.append(path)
import InitilizeTools
customToolsDirect = 'C:/Users/{}/Documents/maya/JM_Custom_Maya_Tools'.format(user)
    
scriptsFolder = customToolsDirect + '/Scripts'
iconsFolder = customToolsDirect + '/Icons'

shelfLevel = mel.eval("$tmpVar=$gShelfTopLevel")
icon = iconsFolder + '/CustomToolsIcon.png'
command = "import os\nimport sys\nuser = os.environ.get('USER')\npath = 'C:/Users/' + user + '/Documents/maya/JM_Custom_Maya_Tools/Scripts'\nif path not in sys.path:\n    sys.path.append(path)\nimport InitilizeTools\nInitilizeTools.CustomToolsJM()"
shelf = cmds.tabLayout(shelfLevel, query=1, ca=1, selectTab = True)

cmds.shelfButton(p = shelf, image1 = icon, command = command)

InitilizeTools.CustomToolsJM()