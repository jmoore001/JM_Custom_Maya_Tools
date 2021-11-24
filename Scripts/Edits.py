import maya.cmds as cmds
import os
import sys
class Edits():

    user = os.environ.get('USER')
    path = 'C:/Users/' + user + '/Documents/maya/JM_Custom_Maya_Tools/Scripts'
    if path not in sys.path:
        sys.path.append(path)

    import JMCustomMarkingMenu
    JMCustomMarkingMenu.JMCustomToolsMarkingMenu()
    version = cmds.about(version = True)

    destWindows = 'C:/Users/' + user + '/Documents/maya/' + version + '/scripts/userSetup.mel'
    srcWindows = path + '/userSetup.mel'
    cmds.sysFile( srcWindows, copy=destWindows )
        
Edits()