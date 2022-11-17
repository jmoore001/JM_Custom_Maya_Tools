
import maya.cmds as cmds
import maya.mel as mel



import Edits
Edits.Edits()


class LayoutUVs(object):

    def __init__(self):
        sel = cmds.ls(sl=True, type = 'float3')


        edges = cmds.polyListComponentConversion(sel, fe=True, te =True)




        def Layout(object):
            mel.eval("u3dUnfold -ite 1 -p 0 -bi 1 -tf 1 -ms 1024 -rs 0 " + object + ";")
            mel.eval("texOrientShells;")
            mel.eval("u3dLayout -res 256 -scl 1 -spc .004 - mar .004 " + object + ";")
        def DH(object):
            cmds.select(object)
            mel.eval("DeleteHistory;")


        selection = cmds.ls(sl = True)
        for object in selection:
            if cmds.objectType(object) == "transform":
                shapeNode = cmds.listRelatives(object, s = True)
            
            
                if shapeNode:
                    Layout(object)
                    DH(object)
                    cmds.select(selection)
        if len(edges) > 0:
        


            cmds.polyMapCut()
        
            mel.eval("InvertSelection;")
            cmds.polyMapSew()
        
            mel.eval("InvertSelection;")
        
            selectededges = cmds.ls(sl = True)
            object = selectededges[0].split(".")[0]
            Layout(object)
        
            cmds.select(selectededges)
            DH(object)
        


        


