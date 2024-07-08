import maya.cmds as cmds
import maya.mel as mel
import os

import sys
scriptsFolder = cmds.optionVar(q = "JMDirectory") + "/Scripts"

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)
import Edits
Edits.Edits()

class CreateProject(object):
    def __init__(*args):
        windowSize = (400, 180)
        windowName = 'projectWindow'
        windowTitle = 'JM Project Window'
        def CloseWindow(*args):
            if cmds.window(windowName, q = True, exists = True):
                cmds.deleteUI(windowName, window = True)
        CloseWindow()
        def MakeFolder(*args):
            name = cmds.textField(userInput, q = True, text = True)
            chosenDirectory = cmds.button(directButton, q = True, l = True)
            if chosenDirectory == 'Choose Directory':
                cmds.warning('Must have a directory chosen to create project')
                return
            if len(name) == 0:
                cmds.warning('Must choose a name for project')
                return
            fileList = cmds.getFileList(fld = chosenDirectory)
            for f in fileList:
                if f == name:
                    cmds.warning("Project already exists with name '{0}' in '{1}'".format(name, chosenDirectory))
                    return
            projFolder = chosenDirectory + '/' + name
            print(projFolder)
            os.makedirs(projFolder)


            def create_folder( directory ):
                if not os.path.exists( directory ):
                    os.makedirs( directory )
            
            maya_dir = projFolder
            create_folder( maya_dir )
            
            
            
            for file_rule in cmds.workspace(query=True, fileRuleList=True):
                file_rule_dir = cmds.workspace(fileRuleEntry=file_rule)
                maya_file_rule_dir = os.path.join( maya_dir, file_rule_dir)
                create_folder( maya_file_rule_dir )
            os.rmdir(projFolder + '/autosave')
            os.rmdir(projFolder + '/clips')
            
            os.rmdir(projFolder + '/movies')
            os.rmdir(projFolder + '/sceneAssembly')
            os.rmdir(projFolder + '/scripts')
            os.rmdir(projFolder + '/sound')
            os.rmdir(projFolder + '/Time Editor/Clip Exports')
            os.rmdir(projFolder + '/Time Editor')
            

            
            
            
            
            
            unityDir = projFolder + '/unity'
            fbxDir = projFolder + '/fbx'
            texturesDir = projFolder + '/textures'
            os.makedirs( unityDir )
            os.makedirs( fbxDir )
            os.makedirs( texturesDir )
            evalCommand = 'setProject \"' + maya_dir + '\"'

            mel.eval(evalCommand)
            
            
            cmds.warning("Project \'" + projFolder + "\' successfully created!")
            
            
            CloseWindow()
        
        def ChooseDirectory(*args):

            directory = cmds.fileDialog2(ds = 2,fm = 2, cap = 'Choose Directory For Project', okc = 'Set')
            if directory == None:
                return
            cleanDirect = str(directory)[2:-2]
            
            cmds.button(directButton, edit = True, l = cleanDirect)
        
        
        projWindow = cmds.window(windowName, t = windowTitle, widthHeight = windowSize, s = False)
        parentLayout = cmds.rowColumnLayout(adjustableColumn = True)
        cmds.text('Create New Project Environment')
        cmds.separator(h = 10)
        directButton = cmds.button(l = 'Choose Directory',  c = ChooseDirectory)
        cmds.separator(h = 10)
        cmds.text('Choose Name for Project')
        global userInput
        userInput = cmds.textField()
        cmds.separator(h = 10)
        cmds.button(l = 'Create', c = MakeFolder)
        cmds.button(l = 'Close', c = CloseWindow)
        cmds.showWindow()
        cmds.window(windowName, e = True, widthHeight = windowSize)

                
        
        
CreateProject()