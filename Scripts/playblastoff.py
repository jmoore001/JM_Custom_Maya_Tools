import maya.cmds as cmds

import time

def blastoff(direct, filepref):
    import KitbashUI
    
    imagefile = direct + '/' + filepref + '.png'
    mafile = direct + '/' + filepref + '.ma'

    if cmds.modelEditor('temppanel1', exists = True):
        cmds.deleteUI('temppanel1', pnl = True)
    temppanel1 = cmds.modelPanel('temppanel1', mbv = False, l = 'Thumnail Preview', toc = True, bl = False)
        

    
    selection = cmds.ls(sl = True, typ = 'transform')
    
    print(selection)
    
    hiddenstuff = cmds.ls(iv = True,typ = 'transform')

    cmds.modelEditor(temppanel1, edit = True,hud = False, da = 'smoothShaded', vs = True, av = True)
    
    cmds.duplicate(n = filepref, rc = True, un = False)
    
    global grpname
    grpname = filepref + 'temp_grp'
    cmds.group(n = grpname )


    cmds.CenterPivot()
    cmds.setFocus(temppanel1)
    cmds.HideUnselectedObjects()
    cmds.move(0,0,0, rpr = True)
    cmds.FreezeTransformations()
    
    cmds.camera(n = 'tempcamera1', fl = 50)
    
    cmds.setFocus(temppanel1)
    
    cmds.lookThru('tempcamera1')
    
    
    
    
    cmds.select('tempcamera1')
    cmds.rotate(-30,0,0)
    cmds.group(n = 'CameraGroup')
    cmds.move(0,0,0, "CameraGroup.rotatePivot", rpr = True)
    cmds.rotate(30, y = True, a = True)
    cmds.select(grpname)
    cmds.setFocus(temppanel1)
    cmds.viewFit()
    cmds.setFocus(temppanel1)
    cmds.viewFit()
    cmds.select('CameraGroup')
    cmds.setToolTo('selectSuperContext')
    
    

                 
    def closewindows(*args):
        if cmds.window('cameraangle', exists = True):
            cmds.deleteUI('cameraangle', window = True)
        if cmds.window('waitwindow', exists = True):
            cmds.deleteUI('waitwindow', window = True)
        if cmds.modelEditor('temppanel1', exists = True):
            cmds.deleteUI('temppanel1', pnl = True)
        
    
    
        cmds.showHidden(all = True)
                
    
        cmds.delete(grpname)
    
    
    
        cmds.delete('CameraGroup')
    
            
        cmds.hide(hiddenstuff)
        cmds.select(selection)

        
    def waitwindow(*args):
        if cmds.window('waitwindow', exists = True):
            cmds.deleteUI('waitwindow', window = True)
        
        cmds.window('waitwindow', title = 'Please Wait', w = 125, h = 35, s = False)
        cmds.rowColumnLayout(adjustableColumn = True)
        
        cmds.text('Please Wait')
        
        cmds.showWindow()

    def exportplayblast(*args):
        waitwindow()
        if cmds.window('cameraangle', exists = True):
            cmds.deleteUI('cameraangle', window = True)

        
        print(grpname)
        currentframe = int(cmds.currentTime(q = True))

        
        newmatobj = cmds.listRelatives(grpname)
        shadename = filepref + '_mtl'
        tempblinn = cmds.shadingNode('blinn', asShader=True, n = shadename)
        cmds.select(newmatobj)
        cmds.hyperShade(a = tempblinn)
              
        cmds.select('tempcamera1')
        cmds.setFocus(temppanel1)        
        
        cmds.playblast(cf = imagefile,p = 100, w = 200, h = 200, os = True, v = False, orn = False, fmt = 'image', fr = currentframe)        
        time.sleep(.5)
        
        cmds.select(grpname, r = True)
        cmds.file(mafile, es = True, type='mayaAscii', ch = False)
        
        

        cmds.delete(tempblinn)  
        time.sleep(.75)

        KitbashUI.KitbashUI()
        closewindows()
        
        

    
    
              
    def camerawindow(*args):
        def rcamx(*args):
            xrot = cmds.intSlider(xslider, q = True, v =  True)
            
            cmds.rotate(xrot, x = True)
        def rcamy(*args):
                
            yrot = cmds.intSlider(yslider, q = True, v =  True)
            cmds.rotate(yrot, y = True, a = True)    
            
        cmds.window('cameraangle', title = 'Camera Angle', w = 400, h = 100, s = False)
        cameralayout = cmds.rowColumnLayout(adjustableColumn = True)
        cmds.text('Choose angle for thumbnail.', h = 30, font = 'boldLabelFont')
        cmds.text('X Rotation')
        xslider = cmds.intSlider(min = -45, max = 135, dc = rcamx)
        cmds.text('Y Rotation')
        yslider = cmds.intSlider(min = 0, max = 360, dc = rcamy)
        cmds.rowColumnLayout(nc = 2, adjustableColumn = True)
        cmds.button(l = 'Add to Library', c = exportplayblast)
        cmds.button(l = 'Cancel', c = closewindows)
        cmds.showWindow()
            
        
    

    camerawindow()
                
                
                
        
    
        
    