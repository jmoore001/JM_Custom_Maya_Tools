import maya.cmds as cmds
import os
import sys
import maya.mel as mel
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



    def AddButtonToShelf(name, command, icon):
        shelfLevel = mel.eval("$tmpVar=$gShelfTopLevel")
        current_shelf = cmds.tabLayout(shelfLevel, query=1, ca=1, selectTab = True)
        
        # Get the tools in the current shelf
        shelf_tools = cmds.shelfLayout(current_shelf, q=True, ca=True)
        
        # Print the list of tools
        
        willCreate = True
        if(shelf_tools != None):

            for tool in shelf_tools:
                if('separator' not in tool):
                    tool_label = cmds.shelfButton(tool, q=True, label=True)
                    if(name ==tool_label):
                    
                        willCreate = False
                    

        if(willCreate):
        
            cmds.shelfButton(p = current_shelf, image1 = icon, command = command, l = name)
        
        else:
            cmds.warning(name + ' already exists on your shelf, this occurance is ignored')


Edits()