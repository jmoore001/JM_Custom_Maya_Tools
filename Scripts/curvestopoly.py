import math

import maya.cmds as cmds


import functools
class CurvesToPolygons(object):
    def __init__(self):
        
        def createUI(pWindowTitle, pApplyCallback):
            windowID = 'myWindowID'
            if cmds.window(windowID, exists = True):
                cmds.deleteUI(windowID)
            
            cmds.window(windowID, title = pWindowTitle, sizeable = False, resizeToFitChildren= True)
            
            cmds.rowColumnLayout( numberOfColumns = 2, columnWidth = [(1,200), (2, 90)], columnOffset =[(1, 'right', 3)])
            
            cmds.text( label = 'Round Subdivisions (8-32)')
            
            Roundsubdivfield = cmds.intField( value = 12)
            
            cmds.text( label = 'Wire Radius')
            
            Radiusfield = cmds. floatField(value = .3)
            
            cmds.text( label = 'Curve Divisions')
            
            Curvedivsfield = cmds. intField(value = 30)
            
            
            cmds.separator(h = 10, style = 'none')
            cmds.separator(h = 10, style = 'none')
            cmds.separator(h = 10, style = 'none')
            
            cmds.separator(h = 10, style = 'none')
            
            cmds.button(label = 'Apply', command = functools.partial(pApplyCallback, Roundsubdivfield, Radiusfield, Curvedivsfield))
            
            def cancelCallback( *pArgs):
                if cmds.window(windowID, exists = True):
                    cmds.deleteUI(windowID)
            
            
            
            cmds.button(label = 'Cancel', command = cancelCallback)
            
            cmds.showWindow()
            
        def applyCallback(pRoundsubdivfield, pRadiusfield, pCurvedivsfield, *pArgs):
            
            
        
            
            
            subdivitions = cmds.intField(pRoundsubdivfield, query = True, value = True)
            radius = cmds.floatField(pRadiusfield, query = True, value = True)
            divisions = cmds.intField(pCurvedivsfield, query = True, value = True)
            
            
            
            selectionlist = cmds.ls(sl = True)
            
            
            iteration = 0
            initial = 0
            
            relist = 0
            
            curvelist = []
            
            for curves in selectionlist:
                newitem = relist
                curvelist.append(newitem)
                relist += 1
            
            for everyitem in curvelist:
                cmds.select(selectionlist[initial], r = True)
                
                cmds.rename('path')
                
                
                
            
                
                
                if subdivitions < 8 or subdivitions >32:
                    print('must have a between 8 and 32 subdivitions')
            
            
                    
                if subdivitions >= 8 and subdivitions <= 32:
                    cmds.polyCylinder(r = radius, h = 0, sx = subdivitions, name = 'tempname') 
                
                
                def faceselect(subdivitions):
                    if subdivitions == 8:
                        faces = cmds.select('tempname.f[0:8]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 9:
                        faces = cmds.select('tempname.f[0:9]')
                        cmds.polyDelFacet()
                        
                            
                    elif subdivitions == 10:
                        faces = cmds.select('tempname.f[0:10]')
                        cmds.polyDelFacet()
                       
                        
                    elif subdivitions == 11:
                        faces = cmds.select('tempname.f[0:11]')
                        cmds.polyDelFacet()
                       
                        
                    elif subdivitions == 12:
                        faces = cmds.select('tempname.f[0:12]')
                        cmds.polyDelFacet()
                       
                    
                    
                    elif subdivitions == 13:
                        faces = cmds.select('tempname.f[0:13]')
                        cmds.polyDelFacet()
                      
                    
                    
                    elif subdivitions == 14:
                        faces = cmds.select('tempname.f[0:14]')
                        cmds.polyDelFacet()
                       
                    
                    elif subdivitions == 15:
                        faces = cmds.select('tempname.f[0:15]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 16:
                        faces = cmds.select('tempname.f[0:16]')
                        cmds.polyDelFacet()
                        
                    
                    
                    elif subdivitions == 17:
                        faces = cmds.select('tempname.f[0:17]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 18:
                        faces = cmds.select('tempname.f[0:18]')
                        cmds.polyDelFacet()
                        
                    
                    
                    elif subdivitions == 19:
                        faces = cmds.select('tempname.f[0:19]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 20:
                        faces = cmds.select('tempname.f[0:20]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 21:
                        faces = cmds.select('tempname.f[0:21]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 22:
                        faces = cmds.select('tempname.f[0:22]')
                        cmds.polyDelFacet()
                        
                    
                    elif subdivitions == 23:
                        faces = cmds.select('tempname.f[0:23]')
                        cmds.polyDelFacet()
                       
                    
                    elif subdivitions == 24:
                        faces = cmds.select('tempname.f[0:24]')
                        cmds.polyDelFacet()
                    
                    
                    elif subdivitions == 25:
                        faces = cmds.select('tempname.f[0:25]')
                        cmds.polyDelFacet()
                    
                    elif subdivitions == 26:
                        faces = cmds.select('tempname.f[0:26]')
                        cmds.polyDelFacet()
                    
                    elif subdivitions == 27:
                        faces = cmds.select('tempname.f[0:27]')
                        cmds.polyDelFacet()
                    
                    elif subdivitions == 28:
                        faces = cmds.select('tempname.f[0:28]')
                        cmds.polyDelFacet()
                    
                    
                    elif subdivitions == 29:
                        faces = cmds.select('tempname.f[0:29]')
                        cmds.polyDelFacet()
                    
                    
                    elif subdivitions == 30:
                        faces = cmds.select('tempname.f[0:30]')
                        cmds.polyDelFacet()
                    
                    
                    elif subdivitions == 31:
                        faces = cmds.select('tempname.f[0:31]')
                        cmds.polyDelFacet()
                    
                    elif subdivitions == 32:
                        faces = cmds.select('tempname.f[0:32]')
                        cmds.polyDelFacet()
                        
                
                
                faceselect(subdivitions)
                
                
                
                
                
                
                
                curvestart = cmds.pointPosition( 'path.cv[0]' )
                
                xpos = curvestart[0]
                ypos = curvestart[1]
                zpos = curvestart[2]
                
                
                cmds.move(xpos, ypos, zpos, 'tempname')
                
                
                
                
                
                curvestart = cmds.pointPosition( 'path.cv[0]' )
                
                
                curvepointtwo = cmds.pointPosition( 'path.cv[1]' )
                
                x1pos = curvestart[0]
                y1pos = curvestart[1]
                z1pos = curvestart[2]
                
                x2pos = curvepointtwo[0]
                y2pos = curvepointtwo[1]
                z2pos = curvepointtwo[2]
                
                xdif = abs(x1pos-x2pos)
                ydif = abs(y1pos-y2pos)
                zdif = abs(z1pos-z2pos)
                
                
                
                cmds.select('tempname')
                
                # z rotation
                
                if xdif == 0:
                    zrot = 0
                
                else:
                    ztheta = math.atan(ydif/xdif)
                
                    if x1pos < x2pos:
                        
                        ztheta = ztheta * -1
                        
                    else:
                       
                        ztheta = ztheta
                    
                    
                    
                    zrot = (math.degrees(ztheta))
                
                
                
                
                
                
                
                #cmds.FreezeTransformations('tempname*')
                
                
                
                
                
                
                # y rotation
                
                if xdif == 0:
                    yrot = 0
                
                else:
                    ytheta = math.atan(zdif/xdif)
                    
                    if x1pos < x2pos:
                        
                        ytheta = ytheta * -1
                    else:
                        
                        ytheta = ytheta
                    
                    yrot = (math.degrees(ytheta))
                
                
                
                
                
                
                
                #x rotation
                
                if ydif == 0:
                    xrot = 0
                else:
                
                    xtheta = math.atan(zdif/ydif)
                    
                    if z1pos < z2pos:
                        
                        xtheta = xtheta * 1
                        
                    else:
                        
                        xtheta = xtheta * -1
                
                
                    xrot = math.degrees(xtheta)
                
                cmds.rotate(0,yrot,0, 'tempname')
                cmds.FreezeTransformations()
                
                cmds.rotate(xrot,0,zrot, 'tempname')
                
                cmds.FreezeTransformations()
                cmds.delete(ch = True)
                
                if y1pos > y2pos:
                    cmds.scale(1,-1,1)
                    cmds.FreezeTransformations()
                    
                    
                cmds.select('tempname.f[0]')
                
                cmds.select('path*', tgl = True)
                
                
                cmds.polyExtrudeFacet(d = divisions, inc = 'path')
                    
                    
                    
                cmds.select('path', r = True)
                cmds.rename('curve' + str(initial))
                
                cmds.select('tempname', r = True)
                cmds.rename('wire' + str(initial))
                cmds.delete(ch = True)
                
                
                
                
                
                    
                initial += 1
                
            cmds.group('wire*', n= 'wires')
            cmds.group('path*', n = 'curves')
            
            
            
        createUI('Curves To Geometry', applyCallback)
            