import maya.cmds as cmds
import maya.mel as mel
import os
import sys
scriptsFolder = cmds.optionVar(q = "JMDirectory") + "/Scripts"

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)
import Edits
Edits.Edits()


class ApplySameUVs(object):

    def __init__(self):
        
        selectobject = cmds.ls(sl = True)
        
        isshape = cmds.listRelatives(s = True)
        print(isshape)
        id = cmds.nodeType(isshape[0])
        print(id)
        if len(selectobject) == 1 and id == 'mesh':
            
            
            
                
                    
            similarobjects = []
                
            everyobject = cmds.filterExpand (cmds.ls (l=True, typ = 'transform'), sm=12)
            
            def findverts(object):
                verts = cmds.polyEvaluate (object, vertex=True)
                return verts
            
            def findfaces(object):
                faces = cmds.polyEvaluate (object, f = True)
                return faces
                
            mainobjectverts = float(findverts(selectobject))
            mainobjectfaces = float(findfaces(selectobject))
            
                    
               
            for x in everyobject:
                compareverts = float(findverts(x))
                comparefaces = float(findfaces(x))
                
                compareedges = cmds.polyCompare(x, selectobject, edges = True)
                
                
                print(str(x) + ' ' + str(compareedges))
                willadd = True
                for y in similarobjects:
                    if y == x:
        
                        willadd = False
        
                if compareedges == 0 and mainobjectverts == compareverts  and mainobjectfaces == comparefaces and str(x) != str(selectobject)[3:-2] and willadd == True:
        
                    similarobjects.append(x)
                    
                
                
            print(similarobjects)            
            if len(similarobjects) >= 1:        
                cmds.select(selectobject, r = True)
                cmds.delete(ch = True)
                for transferobject in similarobjects:
                    cmds.select(selectobject, r = True)
                    cmds.select(transferobject, add = True)
            
                    cmds.transferAttributes(uvs = 2, spa = 5)
                    
                cmds.select(similarobjects, r = True)
                cmds.select(selectobject, add = True)
                cmds.delete(ch = True)
                    
                    
                    
            else:
                cmds.warning('There are no similar objects in the scene.')
        if len(selectobject) == 1 and id != 'mesh':
            cmds.warning('This function only works with poly object selected.')
                
        if len(selectobject) > 1:
            cmds.warning('You may only have one object selected to use this function.')
            
        if len(selectobject) == 0:
            cmds.warning('You must have an object selected to run this command.')
        
        

