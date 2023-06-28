import maya.cmds as cmds
import os
import sys


scriptsFolder = cmds.optionVar(q = "JMDirectory") + "/Scripts"

if scriptsFolder not in sys.path:
    sys.path.append(scriptsFolder)

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


        usd = cmds.internalVar(usd=True)
        version = cmds.about(version=True)
        dirWithoutVersion = usd.replace(str(version)+ "/", "")
        mayaDirectory = dirWithoutVersion.replace("/scripts/", "")
        path = mayaDirectory + "/JM_Custom_Maya_Tools"
        scriptsFolder = path + '/Scripts'
        var = cmds.optionVar(sv =("JMDirectory", path))

        if scriptsFolder not in sys.path:
            sys.path.append(scriptsFolder)
        
        iconFolder = mayaDirectory + "/JM_Custom_Maya_Tools/Icons"

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