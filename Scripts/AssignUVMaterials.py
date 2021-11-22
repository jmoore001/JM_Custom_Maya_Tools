import maya.cmds as cmds
import pymel.core as pm
import maya.mel as mel
import os.path
from functools import partial
class ApplyUVsUI(object):
    def __init__(self):
        def FindProjectRoot(*args):
            projectFile = cmds.workspace(q = True, rd = True)
            folderList = cmds.getFileList(fld = projectFile)
            for folder in folderList:
                if folder == 'textures':
                    returnFolder = cmds.workspace( q=True, rd=True ) + 'textures'
                    return returnFolder
                    
            return projectFile
        global projectRoot
        projectRoot = FindProjectRoot()
        print('projectRoot is ' + projectRoot)
        albedoFile = 'None'
        albedoList = []
        metalicFile = 'None'
        metalicList = []
        normalFile = 'None'
        normalList = []
        print('albedo list ' + str(albedoList))
        print('normal list ' + str(metalicList))
        print('metalic list ' + str(normalList))
        tempList = []
        def CloseWindow(*args):
            cmds.deleteUI('GroupNameWindow', window = True)
        everyObject = cmds.ls(sl = True, typ = 'transform', o = True)
        if len(everyObject) > 0:
            
            def ChooseFileAlbedo(*args):
                global projectRoot
                chosenFile = cmds.fileDialog2(ff = '*.png', dir = projectRoot, fm = 1)
            
                cleanFile = str(chosenFile)[3:-2]
                direct = os.path.dirname(cleanFile)
                
                fileText = str(chosenFile).replace(str(direct), '')[4:-2]
                
                
                albedoFile = cleanFile
                
                
                directory = albedoFile.replace(fileText, '')
                fileList = cmds.getFileList(fld = direct)
                del tempList[:]
                del albedoList[:]
                for f in fileList:
                    
                    
                    if fileText[:-9] in str(f):
                        albedoList.append(f)
                
                projectRoot = direct
                cmds.text(albedoText, edit = True, l = 'Albedo - (' + str(len(albedoList)) + ') files detected')
                cmds.button(albedoButton, edit = True, l = fileText)
                    
            def ChooseFileMetalic(*args):
                global projectRoot   
                chosenFile = cmds.fileDialog2(ff = '*.png', dir = projectRoot, fm = 1)
            
                cleanFile = str(chosenFile)[3:-2]
                direct = os.path.dirname(cleanFile)
                fileText = str(chosenFile).replace(str(direct), '')[4:-2]
            
                
                metalicFile = cleanFile
                
                directory = metalicFile.replace(fileText, '')
                fileList = cmds.getFileList(fld = directory)
                del tempList[:]
                del metalicList[:]
                for f in fileList:
                    
                    
                    if fileText[:-9] in str(f):
                        metalicList.append(f)
                
                projectRoot = direct
                cmds.text(metalicText, edit = True, l = 'Metalic - (' + str(len(metalicList)) + ') files detected')
                cmds.button(metalicButton, edit = True, l = fileText)
                
            def ChooseFileNormal(*args):
                global projectRoot    
                chosenFile = cmds.fileDialog2(ff = '*.png', dir = projectRoot, fm = 1)
            
                cleanFile = str(chosenFile)[3:-2]
                direct = os.path.dirname(cleanFile)
                fileText = str(chosenFile).replace(str(direct), '')[4:-2]
            
                
                normalFile = cleanFile
                
                directory = normalFile.replace(fileText, '')
                fileList = cmds.getFileList(fld = directory)
                del normalList[:]
                del tempList[:]
                for f in fileList:
                    
                    
                    if fileText[:-9] in str(f):
                        normalList.append(f)
                
                projectRoot = direct
                cmds.text(normalText, edit = True, l = 'Normal - (' + str(len(normalList)) + ') files detected')
                cmds.button(normalButton, edit = True, l = fileText)
            def RunGroups(*args):
                
                
                materialName = str(cmds.textField(matName, q = True, text = True))
                CloseWindow()
                everyObject = cmds.ls(sl = True)
                
                
                
                
                
                
                def getUVTile(object):
                    cmds.select(object, r = True)
                    cmds.ConvertSelectionToUVs()
                    UVValues = cmds.polyEditUV(query=True)
                    
                    firstNum = str(UVValues[0])[0]
                    secondNum = str(UVValues[1])[0]
                    if firstNum == '-' or secondNum == '-':
                        cmds.error('Cannot Have shells in negative UV space.')
                    UVTile = [object, int(firstNum), int(secondNum)]
                    
                    return UVTile
                    
                def CreateGroupNames(Coords):
                    order = []
                    
                    tileNumbers = []
                    
                    for list in Coords:
                        
                        if(len(str(list[1] + 1)) == 1):
                            entry = materialName + 'UV10' + str(list[2]) + str(list[1] + 1)
                        else:
                            
                            entry = materialName + 'UV10' + str(list[1] + 1)
                            
                        if entry not in tileNumbers:
                            tileNumbers.append(entry)
                    
                    tileNumbers.sort()
                    
                    listItem = 0
                    for x in tileNumbers:
                        
                        albedoNodeName = str(albedoList[listItem])
                        metalicNodeName = str(metalicList[listItem])
                        normalNodeName = str(normalList[listItem])
                        albedoNode = cmds.shadingNode('file', at = True, n = albedoNodeName)
                        metalicNode = cmds.shadingNode('file', at = True, n = metalicNodeName)
                        
                        normalNode = cmds.shadingNode('file', at = True, n = normalNodeName)
                        shader = cmds.shadingNode('StingrayPBS', asShader = True, name = str(x))
                        shaderGroup = cmds.sets(renderable=True,noSurfaceShader=True,empty=True, name = str(x) + '_Shader_Group')
                        
                        cmds.connectAttr(shader + '.outColor', shaderGroup + '.surfaceShader')
                        attributeList = cmds.listAttr(shader)
                        
                        
                        cmds.setAttr(albedoNode + '.fileTextureName', albedoList[listItem], type = 'string')
                        cmds.setAttr(metalicNode + '.fileTextureName', metalicList[listItem], type = 'string')
                        cmds.setAttr(normalNode + '.fileTextureName', normalList[listItem], type = 'string')
                        
                        
                        
                        mel.eval('shaderfx -sfxnode {0} -update'.format(shader))
                        
                        
                        cmds.setAttr(str(shader) + ".use_color_map", 1)
                        cmds.setAttr(shader + '.use_normal_map', 1)
                        cmds.setAttr(shader + '.use_metallic_map', 1)
                        
                        
                        cmds.connectAttr(albedoNode + '.outColor', shader + '.TEX_color_map', force = True)
                        cmds.connectAttr(metalicNode + '.outColor', shader + '.TEX_metallic_map', force = True)
                        cmds.connectAttr(normalNode + '.outColor', shader + '.TEX_normal_map', force = True)
                        
        
                        
                        
                        
                        listItem += 1
                   
                    for obj in Coords:
                        
                        if(len(str(obj[1] + 1)) == 1):
                            matToAssign = materialName + 'UV10' + str(obj[2]) + str(obj[1] + 1)
                        else:
                            
                            matToAssign = materialName + 'UV10' + str(obj[1] + 1)
                        
                        
                        
                        print(matToAssign)
                        materials = cmds.ls(mat = True)
                        for mat in materials:
                            if matToAssign in mat:
                                shader = mat
                        
                                cmds.sets(obj[0], e = True, forceElement = shader + '_Shader_Group')
                        cmds.select(obj[0], r = True)
        
                def makeObjectCoordList():
                    objectCoordList = []
                    for x in everyObject:
                        UVCoords = getUVTile(x)
                        objectCoordList.append(UVCoords)
                    
                    return objectCoordList
                   
                    
                UVCoordList = makeObjectCoordList()
                
                CreateGroupNames(UVCoordList)
                
        
            
            def CloseWindow(*args):
                cmds.deleteUI('AssignUVMaterials', window = True)
                
        
                
            if cmds.window('AssignUVMaterials', exists = True):
                CloseWindow()
                
                
        
            
                    
                    
                
               
            window = cmds.window('AssignUVMaterials', title = 'Choose Material Files', w = 500, h = 300, s = True)
            parentlayout = cmds.rowColumnLayout(adjustableColumn = True)
            albedoText = cmds.text('Albedo')
            albedoButton = cmds.button('Choose Albedo', c = ChooseFileAlbedo)
            cmds.separator(h = 10)
            metalicText = cmds.text('Metalic')
            metalicButton = cmds.button('Choose Metalic', c = ChooseFileMetalic)
            cmds.separator(h = 10)
            normalText = cmds.text('Normal')
            normalButton = cmds.button('Choose Normal', c = ChooseFileNormal)
            cmds.separator(h = 15)
            cmds.text('Choose name for materials.')
            
            matName = cmds.textField()
            
            cmds.separator(h = 10)
            cmds.button('Cancel', c = CloseWindow)
            cmds.button(l = 'Execute', c = RunGroups)
            
            cmds.showWindow()    
            
        else:
            cmds.warning('Must have at least one object selected.')
            
ApplyUVsUI()