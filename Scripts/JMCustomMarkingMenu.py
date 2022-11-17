import maya.cmds as cmds
import os
import sys


user = os.environ.get('USER')
path = 'C:/Users/{}/Documents/maya/JM_Custom_Maya_Tools/Scripts'.format(user)
if path not in sys.path:
    sys.path.append(path)

class JMCustomToolsMarkingMenu(object):

    
    def __init__(self):
        self.RemoveOld()
        self.Build()
        
    def RemoveOld(self):

        if cmds.popupMenu('JMCustomMarkingMenu', ex=True):

            cmds.deleteUI('JMCustomMarkingMenu')
    def Build(self):
        customMenu = cmds.popupMenu('JMCustomMarkingMenu', ctl = True, alt = True, mm = True, b = 3, pmo = True, pmc = self.BuildMarkingMenu, p = "viewPanes")
    
    def BuildMarkingMenu(self, menu, parent):


        user = os.environ.get('USER')
        path = 'C:/Users/{}/Documents/maya/JM_Custom_Maya_Tools/Scripts'.format(user)
        if path not in sys.path:
            sys.path.append(path)
        
        iconFolder = 'C:/Users/{}/Documents/maya/JM_Custom_Maya_Tools/Icons'.format(user)

        def LibraryCommand(*args):
            import KitbashUI
            KitbashUI.KitbashUI()
        def AssignUVMatCommand(*args):
            import AssignUVMaterials
            AssignUVMaterials.ApplyUVsUI()
        def ApplyUVsCommand(*args):
            import applysameUVs
            applysameUVs.ApplySameUVs()
        def CurvesToPolyCommand(*args):
            import curvestopoly
            curvestopoly.CurvesToPolygons()
        def GroupUVsCommand(*args):
            import GroupUV
            GroupUV.GroupByUVs()
        def LayoutUVsCommannd(*args):
            import LayoutUVs
            LayoutUVs.LayoutUVs()
        def CreateProjectCommand(*args):
            import CreateProject
            CreateProject.CreateProject()
        def ToolKitCommand(*args):
            import InitilizeTools
            InitilizeTools.CustomToolsJM()
        def QCToolCommand(*args):
            import QCTool
            QCTool.QCUI()
        

        cmds.menuItem(p=menu, l="Library", rp="S", i=iconFolder + '/KitbashUI.png',c = LibraryCommand)
        cmds.menuItem(p=menu, l="Assign Materials By UVs", rp="W", i=iconFolder + '/AssignUVMaterials.png',c = AssignUVMatCommand)
        cmds.menuItem(p=menu, l="Apply Same UVs", rp="E", i=iconFolder + '/applysameUVs.png',c = ApplyUVsCommand)
        cmds.menuItem(p=menu, l="Curves To Geometry", rp="SE", i=iconFolder + '/curvestopoly.png',c = CurvesToPolyCommand)
        cmds.menuItem(p=menu, l="Group By UVs", rp="SW", i=iconFolder + '/GroupUV.png',c = GroupUVsCommand)
        cmds.menuItem(p=menu, l="Layout UVs", rp="NW", i=iconFolder + '/LayoutUVs.png',c = LayoutUVsCommannd)
        cmds.menuItem(p=menu, l="Create Project", rp="NE", i=iconFolder + '/CreateProject.png',c = CreateProjectCommand)
        cmds.menuItem(p=menu, l="Tool Kit", rp="N", i=iconFolder + '/CustomToolsIcon.png',c = ToolKitCommand)
        cmds.menuItem(p=menu, l="Quality Control", i=iconFolder + '/QCTool.png',c = QCToolCommand)
    
JMCustomToolsMarkingMenu()