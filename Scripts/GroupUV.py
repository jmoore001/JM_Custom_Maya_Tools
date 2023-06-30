import maya.cmds as cmds
import os
import sys
scriptsFolder = cmds.optionVar(q = "JMDirectory") + "/Scripts"

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)
import Edits
Edits.Edits()
class GroupByUVs(object):
    def __init__(self):
        
        def CloseWindow(*args):
            cmds.deleteUI('GroupNameWindow', window = True)
        everyObject = cmds.ls(sl = True, typ = 'transform', o = True)
        if len(everyObject) > 0:
            
            def runGroups(parentName, *args):
                
                parentName = str(cmds.textField(inputField, q = True, text = True))
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
                            entry = 'UV10' + str(list[2]) + str(list[1] + 1)
                        else:
                            
                            entry = 'UV10' + str(list[1] + 1)
                        
                        if entry not in tileNumbers:
                            tileNumbers.append(entry)
                    
                    tileNumbers.sort()
                    print(tileNumbers)
                    
            
                    
                    cmds.group(em = True, name = parentName)
                    for grp in tileNumbers:
                        
                        cmds.group(em = True, name = grp, parent = parentName)
                        
                    for obj in Coords:
                        parentNode = str(cmds.listRelatives(obj[0], p = True))
                        
                        if parentNode != 'None':
                            cmds.parent(str(obj[0]), w = True)
                        if(len(str(obj[1] + 1)) == 1):
                            grpToGo = 'UV10' + str(obj[2]) + str(obj[1] + 1)
                        else:
                            
                            grpToGo = 'UV10' + str(obj[1] + 1)    
                            
                        
                        cmds.parent(obj[0], grpToGo)
                def makeObjectCoordList():
                    objectCoordList = []
                    for x in everyObject:
                        UVCoords = getUVTile(x)
                        objectCoordList.append(UVCoords)
                    
                    return objectCoordList
                   
                    
                UVCoordList = makeObjectCoordList()
                
                CreateGroupNames(UVCoordList)
                
            
            if cmds.window('GroupNameWindow', exists = True):
                CloseWindow()
            window = cmds.window('GroupNameWindow', title = 'Choose Group Name', w = 300, h = 100, s = False)
            parentlayout = cmds.rowColumnLayout(adjustableColumn = True)
            cmds.text('Choose A Name for Your Parent Group.')
            cmds.separator(h = 10)
            inputField = cmds.textField()
            
            cmds.separator(h = 10)
            cmds.button('Cancel', c = CloseWindow)
            cmds.button(l = 'Execute', c = runGroups)
            
            cmds.showWindow()
            
        else:
            cmds.warning('Must have at least one object selected.')