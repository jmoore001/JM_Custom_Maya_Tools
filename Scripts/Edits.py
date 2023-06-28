import maya.cmds as cmds
import os
import sys
class Edits():

    usd = cmds.internalVar(usd=True)
    version = cmds.about(version=True)
    dirWithoutVersion = usd.replace(str(version)+ "/", "")
    mayaDirectory = dirWithoutVersion.replace("/scripts/", "")
    path = mayaDirectory + "/JM_Custom_Maya_Tools"
    scriptsFolder = path + '/Scripts'

    if scriptsFolder not in sys.path:
        sys.path.append(scriptsFolder)

    import JMCustomMarkingMenu
    JMCustomMarkingMenu.JMCustomToolsMarkingMenu()
    
    
    destWindows = mayaDirectory + version + '/scripts/userSetup.mel'
    if os.path.exists(destWindows):
        cmds.warning("userSetup.mel alread exists, this is being skipped, you will need to make sure that " + destWindows + " contains the the lines of code inside of " + srcWindows)
    else:
        srcWindows = path + '/userSetup.mel'
        cmds.sysFile( srcWindows, copy=destWindows )
        customToolsDirect = mayaDirectory + "/JM_Custom_Maya_Tools"

Edits()