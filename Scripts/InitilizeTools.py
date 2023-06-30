import os
import sys
import maya.mel as mel
from functools import partial
import maya.cmds as cmds
scriptsFolder = cmds.optionVar(q = "JMDirectory") + "/Scripts"

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)
import Edits
Edits.Edits()



class CustomToolsJM(object):
    global customToolsDirect
    global scriptsFolder
    global iconsFolder
    customToolsDirect = cmds.optionVar(q = "JMDirectory")
        
    scriptsFolder = customToolsDirect + '/Scripts'
    iconsFolder = customToolsDirect + '/Icons'
    global CloseUI
    def CloseUI(windowName, *args):
        if cmds.window(windowName, exists = True):
            cmds.deleteUI(windowName)
    global AddingToShelf
    def AddingToShelf(moduleName, call, *args):
        global iconsFolder
        command = "import os\nimport sys\nuser = os.environ.get('USER')\nscriptsFolder = cmds.optionVar(q = 'JMDirectory') + '/Scripts'\nif scriptsFolder not in sys.path:\n    sys.path.append(nscriptsFolder)\nimport {0}\n{1}".format(moduleName, call)
        icon = iconsFolder + '/' + moduleName + '.png'
        Edits.Edits.AddButtonToShelf(str(moduleName), command, icon)

##################################################################   
    global applysameUVs
    def applysameUVs(info, shelfvar, *args):
        import applysameUVs
        if info:
            return 'Will use selected object to search the scene for similar objects and apply the same UVs to those objects.'
        else: 
            if shelfvar:
                AddingToShelf('applysameUVs', 'applysameUVs.ApplySameUVs()')
            else:   
                applysameUVs.ApplySameUVs()
##################################################################  
    global AssignUVMaterials
    def AssignUVMaterials(info, shelfvar, *args):
        import AssignUVMaterials
        if info:
            return 'Will assign a PBR material to all selected objects based on UV coordinates. This is meant to be used for use in Unity game engine.'
        else:
            if shelfvar:
                AddingToShelf('AssignUVMaterials', 'AssignUVMaterials.ApplyUVsUI()')
            else:  
                AssignUVMaterials.ApplyUVsUI()
##################################################################  
    global curvestopoly
    def curvestopoly(info, shelfvar, *args):
        import curvestopoly
        if info:
            return 'Converts any selected curves into usable 3D mesh.'
        else:
            if shelfvar:
                AddingToShelf('curvestopoly', 'curvestopoly.CurvesToPolygons()')
            else:
                curvestopoly.CurvesToPolygons()
##################################################################    
    global GroupUV
    def GroupUV(info, shelfvar, *args):
        import GroupUV
        if info:
            return 'Groups all selected objects based on UV coordinates.'
        else:
            if shelfvar:
                AddingToShelf('GroupUV', 'GroupUV.GroupByUVs()')
            else:
                GroupUV.GroupByUVs()
##################################################################  
    global KitbashUI
    def KitbashUI(info, shelfvar, *args):
        import KitbashUI
        if info:
            return 'A library of 3D objects for later use.'
        else:
            if shelfvar:
                AddingToShelf('KitbashUI', 'KitbashUI.KitbashUI()')
            else:
               KitbashUI.KitbashUI()
               
##################################################################
    global QCTool
    def QCTool(info, shelfvar, *args):
        import QCTool
        if info:
            return 'A tool for quality control on models.'
        else:
            if shelfvar:
                AddingToShelf('QCTool', 'QCTool.QCUI()')
            else:
                QCTool.QCUI()
##################################################################  
    global CreateProject
    def CreateProject(info, shelfvar, *args):
        import CreateProject
        if info:
            return 'Create a maya project for use at Index AR Solutions.'
        else:
            if shelfvar:
                AddingToShelf('CreateProject', 'CreateProject.CreateProject()')
            else:
                CreateProject.CreateProject()
################################################################## 
    global LayoutUVs
    def LayoutUVs(info, shelfvar, *args):
        import LayoutUVs
        if info:
            return 'Unfold, orient, and layouut UVs. If in edit mode, the tool will cut all selected edges first then it will unfold, orient, and layout the UV shells.'
        else:
            if shelfvar:
                AddingToShelf('LayoutUVs', 'LayoutUVs.LayoutUVs()')
            else:
                LayoutUVs.LayoutUVs()
################################################################## 
    def __init__(self):
        self.close =  True
        self.shelf = False
        backgroundColor = [.25,.25,.25]
        shelfBackgroundColor = [.2, .3, .1]
        
        buttonRGB = [.3, .3, .3]
        closeButtonRGB = [.2, .4, .5]
        shelfButtonRGB = [.4, .5, .8]
        
        self.window = 'JMTools'
        self.title = 'Custom Tools'
        self.size = (250,320)
        
        
        def AddShelf(*args):
            
            if self.shelf:
                cmds.text(topText, l =  'Double click for info.', edit = True)
                cmds.scrollLayout(scrollParent, edit = True, bgc = backgroundColor)
                cmds.button(shelfButton, edit = True, l = 'Add Tools To Shelf (OFF)', bgc = buttonRGB)
            else:
                cmds.text(topText, l = 'Add tools to shelf.', edit = True)
                cmds.scrollLayout(scrollParent, edit = True, bgc = shelfBackgroundColor)
                cmds.button(shelfButton, edit = True, l = 'Add Tools To Shelf (ON)', bgc = shelfButtonRGB)
            self.shelf = not self.shelf
        def CloseOnCommand(*args):
            
            if self.close:
                
                cmds.button(closeOnCommand, edit = True, l = 'Close On Command (OFF)', bgc = buttonRGB)
            else:
                cmds.button(closeOnCommand, edit = True, l = 'Close On Command (ON)', bgc = closeButtonRGB)
            self.close = not self.close
            
        def InfoWindow(action, *args):
            command = action + '(True, False)'
            infoWindowName = 'InfoWindow'
            
            size = (400,140)
            result = eval(command)
            
            CloseUI(infoWindowName)
            cmds.window(infoWindowName)
            cmds.rowColumnLayout(adjustableColumn = True, h = size[1], w = size[1])
            
            inputField = cmds.scrollField(tx = result, editable=False, wordWrap=True, h=100,)
            cmds.separator(h = 10)
            cmds.button(l = 'Close', c = partial(CloseUI, infoWindowName))
            cmds.showWindow(infoWindowName)
            cmds.window(infoWindowName, edit = True, widthHeight =  size, s = False)
        def DoAction(action, *args):
            if self.close and not self.shelf:
                CloseUI(self.window)
            command = action + '(False, {})'.format(self.shelf)
            
            result = eval(command)
        
        
        
        CloseUI(self.window)
        

        
        
        
        
        def CreateButtons():
            scripts = cmds.getFileList(fld = scriptsFolder)
            icons = cmds.getFileList(fld = iconsFolder)
            
            for png in icons:
                for py in scripts:
                    if png[:-4] == py[:-3]:
                        
                        cmds.iconTextButton(png[:-4], i = iconsFolder + '/' + png, c = partial(DoAction, png[:-4]), dcc = partial(InfoWindow, png[:-4]))
                        
        
           
        self.window = cmds.window(self.window, widthHeight = self.size, title = self.title, s = False)
        parentLayout = cmds.rowColumnLayout(adjustableColumn = True)
        topText = cmds.text('Double click for info.')
        cmds.separator(h = 10)
        scrollParent = cmds.scrollLayout(p = parentLayout, height = 195, bgc = backgroundColor)
        cmds.rowColumnLayout(p = scrollParent, nc = 3, cs = [(1,20), (2,20), (3,20)], rs = [(1,10),(2,10),(3, 20)])
        CreateButtons()
        
        
        shelfButton = cmds.button(p = parentLayout, l = 'Add Tools To Shelf (OFF)', bgc = buttonRGB, c = AddShelf)
        closeOnCommand = cmds.button(p = parentLayout, l = 'Close on command (ON)', c = CloseOnCommand, bgc = closeButtonRGB)
        cmds.button(p = parentLayout, l = 'Close', c = partial(CloseUI, self.window), bgc = buttonRGB)
        

        
        cmds.showWindow()
        cmds.window(self.window, edit = True, widthHeight = self.size)
CustomToolsJM()