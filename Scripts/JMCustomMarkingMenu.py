import maya.cmds as cmds
import jm_path

# Ensure our Scripts folder is on sys.path even if optionVars/path separators changed
jm_path.ensure_sys_path()

class JMCustomToolsMarkingMenu(object):

    def __init__(self):
        self.RemoveOld()
        self.Build()

    def Build(self):
        self.BuildMarkingMenu('JM_Tools_MarkingMenu', parent='viewPanes')

    def RemoveOld(self):
        if cmds.popupMenu('JM_Tools_MarkingMenu', exists=True):
            cmds.deleteUI('JM_Tools_MarkingMenu')

    def BuildMarkingMenu(self, menu, parent):
        iconFolder = jm_path.get_icons_dir()

        def LibraryCommand(*args):
            import KitbashUI
            KitbashUI.KitbashUI()

        def AssignUVMatCommand(*args):
            import AssignUVMaterials
            AssignUVMaterials.ApplyUVsUI()

        def ApplySameUVCommand(*args):
            import applysameUVs
            applysameUVs.applysameUVsUI()

        def CurvesToPolyCommand(*args):
            import curvestopoly
            curvestopoly.curvestopolyUI()

        def LayoutUVsCommand(*args):
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

        # Build popup menu
        cmds.popupMenu(menu, parent=parent, button=3, ctl=True, alt=True, mm=True)

        cmds.menuItem(p=menu, l="Library", rp="S", i=iconFolder + '/KitbashUI.png', c=LibraryCommand)
        cmds.menuItem(p=menu, l="Assign Materials By UVs", rp="W", i=iconFolder + '/AssignUVMaterials.png', c=AssignUVMatCommand)
        cmds.menuItem(p=menu, l="Apply Same UVs", rp="E", i=iconFolder + '/applysameUVs.png', c=ApplySameUVCommand)
        cmds.menuItem(p=menu, l="Curves To Poly", rp="N", i=iconFolder + '/curvestopoly.png', c=CurvesToPolyCommand)
        cmds.menuItem(p=menu, l="Layout UVs", rp="NE", i=iconFolder + '/LayoutUVs.png', c=LayoutUVsCommand)
        cmds.menuItem(p=menu, l="Create Project", rp="SE", i=iconFolder + '/CreateProject.png', c=CreateProjectCommand)
        cmds.menuItem(p=menu, l="Tool Kit", rp="NW", i=iconFolder + '/CustomToolsIcon.png', c=ToolKitCommand)
        cmds.menuItem(p=menu, l="QC Tool", rp="SW", i=iconFolder + '/QCTool.png', c=QCToolCommand)
