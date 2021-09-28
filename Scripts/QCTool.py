import maya.cmds as cmds
from functools import partial
import maya.mel as mel
class QCUI(object):
    
    def __init__(self):
        
        def CloseWindow(*args):
            cmds.deleteUI('QCWindow', window = True)
        def CloseNotes(*args):
            cmds.deleteUI('NoteWindow', window = True)
        
        def AssignMaterial(objects, shader):
            for obj in objects:
                cmds.sets(obj, e = True, forceElement = shader + 'SG')
                
        
        def NoteWindow(errorType, R,G,B, *args):
            def CreateMaterial(errorType, R,G,B, *args):
                
                selected = cmds.ls(sl = True)
                notes = str(cmds.scrollField(inputField, q = True, text = True))
                print(notes)
                if len(selected) > 0:
                    CloseNotes()
                    shader = cmds.shadingNode('lambert', asShader = True, name = errorType + 'Error')
                    cmds.addAttr( shortName='nt', longName='notes', dt = 'string')
                    shaderGroup = cmds.sets(renderable=True,noSurfaceShader=True,empty=True, name = str(shader) + 'SG')
                    cmds.connectAttr(shader + '.outColor', shaderGroup + '.surfaceShader')
                    cmds.setAttr(shader + '.color', R,G,B)
                    
                    cmds.setAttr(shader + '.notes', notes, type = 'string')
                    AssignMaterial(selected, shader)
                    cmds.select(selected)
                else:
                    cmds.warning('Must have at least one object selected.')
            window = cmds.window('NoteWindow', title = 'Notes', w = 200, h = 150, s = False)
            parentlayout = cmds.rowColumnLayout(adjustableColumn = True)
            cmds.text('Add notes to object.')
            cmds.separator(h = 10)
            inputField = cmds.scrollField( editable=True, wordWrap=True, h=50,)
            
            cmds.separator(h = 10)
            cmds.button('Cancel', c = CloseNotes)
            cmds.button(l = 'Apply', c = partial(CreateMaterial, errorType, R, G, B))
            
            cmds.showWindow()
            
        if cmds.window('QCWindow', exists = True):
            CloseWindow()
        if cmds.window('NoteWindow', exists = True):
            CloseNotes()
        
        cmds.window('QCWindow', title = 'Index QC', s = False, h = 300, w = 200)
        parentLayout = cmds.rowColumnLayout()
        cmds.separator(p = parentLayout, h = 10)
        cmds.text('Choose category of the problem.', p = parentLayout)
        cmds.separator(p = parentLayout, h = 10)
        buttonLayout = cmds.rowColumnLayout(p = parentLayout, numberOfColumns = 3, columnWidth = [(1, 90), (2, 90), (3, 10)] , cs = [(1,10),(2,20), (3, 1)], rs = [(1,10),(2,20),(3, 10)])
        
        cmds.button(p = buttonLayout, label = 'Topology', bgc = (0.224359, 0.395, 0.21014), c = partial(NoteWindow, 'Topology', 0.224359, 0.395, 0.21014))
        cmds.button(p = buttonLayout, label = 'Geometry', bgc = (0.21014, 0.238581, 0.395), c = partial(NoteWindow, 'Geometry', 0.21014, 0.238581, 0.395))
        cmds.text(' ')
        cmds.button(p = buttonLayout, label = 'Form',bgc = (0.395, 0.21014, 0.21014),  c = partial(NoteWindow, 'Form', 0.395, 0.21014, 0.21014))
        cmds.button(p = buttonLayout, label = 'Artifact', bgc = (0.395, 0.264498, 0.055695), c = partial(NoteWindow, 'Artifact', 0.395, 0.264498, 0.055695))
        cmds.text(' ')
        cmds.button(p = buttonLayout, label = 'Normals', bgc = (0.292227, 0.152075, 0.395), c = partial(NoteWindow, 'Normal', 0.292227, 0.152075, 0.395))
        cmds.button(p = buttonLayout, label = 'Other', bgc = (0.130515, 0.339, 0.314944), c = partial(NoteWindow, 'Miscellaneous', 0.130515, 0.339, 0.314944))
        cmds.text(' ')
        
        cmds.rowColumnLayout(p = parentLayout, numberOfColumns = 2, cs = [(1,10),(2,10)], rs = [(1,10),(2,10)], columnWidth = [(1, 180), (2, 10)] ) 
        cmds.separator(p = parentLayout, h = 10)
        cmds.button(p = parentLayout, label = 'Close', command = CloseWindow, bgc = (.1,.1,.1))
        
        cmds.showWindow('QCWindow')    



