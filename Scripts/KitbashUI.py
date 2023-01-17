import maya.cmds as cmds
from functools import partial
from playblastoff import blastoff
import random
import string
import os
import sys
user = os.environ.get('USER')
path = 'C:/Users/' + user + '/Documents/maya/JM_Custom_Maya_Tools/Scripts'
if path not in sys.path:
    sys.path.append(path)
import Edits
Edits.Edits()
class KitbashUI(object):

    def __init__(self):
        self.window = 'KitbashUI'
        self.title = '3D Library'
        self.size = (650, 920)
        self.newdirectory = ''
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)
        if cmds.window('namingwindow', exists = True):
            cmds.deleteUI('namingwindow', window = True)
        if cmds.modelEditor('temppanel1', exists = True):
            cmds.deleteUI('temppanel1', pnl = True)
        if cmds.window('cameraangle', exists = True):
            cmds.deleteUI('cameraangle', window = True)
        if cmds.window('waitwindow', exists = True):
            cmds.deleteUI('waitwindow', window = True)
        self.window = cmds.window(self.window, title = self.title, widthHeight = self.size, s = False)

        parentlayout = cmds.rowColumnLayout(adjustableColumn = True)

        cmds.separator(h = 20)

        ########################################################################
        #set directory function
        ########################################################################

        self.directq = cmds.optionVar(q = 'saveddirect')
        if self.directq != 0 and self.directq != 'Set Directory' and self.directq != '0':

            self.newdirectory = self.directq
        directory = ''
        def SendDirect(self):
            setdirectory()
        def setdirectory(*args):


            directory = str(cmds.fileDialog2(fm = 3, ds = 2))
            if directory != 'None':

                newdirect = directory.replace('[u\'', '')[2:]


                self.newdirectory = newdirect.replace('\']', '')

                self.directq = cmds.optionVar(sv = ('saveddirect', self.newdirectory))
                print(self.newdirectory)
                cmds.button(directorybutton, edit = True, l = self.newdirectory)
                createbuttons(self.newdirectory, True)




        def addtoscene (x, label, *args):


            groupname = str(label) + 'temp_grp'

            importlist = cmds.file(x, i = True, rnn = True)
            cmds.select(importlist)
            hiddenstuff = cmds.ls(sl = True, iv = True, typ = 'transform')




            for t in importlist:

                for h in hiddenstuff:

                    if str(t[1:]) == str(h):

                        cmds.delete(t)

            cmds.select(groupname, r = True)
            cmds.duplicate(n = label + '_Group', rc = True)
            cmds.delete(groupname)

        ########################################################################
        #create buttons function
        ########################################################################



        directorybutton = cmds.button(l = 'Set Directory', aop = True, c = SendDirect)


        cmds.text('')

        selectionimage = [0.25, 0.3, 0.3]

        cmds.text('Select objects to import into scene.')


        scrollLayoutparent = cmds.scrollLayout(h = 700, w = 600,  verticalScrollBarThickness=16)
        triLayout = cmds.rowColumnLayout(p = scrollLayoutparent, numberOfColumns = 3, w = 600)


        cmds.rowColumnLayout(adjustableColumn = True, parent = parentlayout)
        def setdirwarning(*args):
            cmds.warning('Must have directory set to add to Library.')


        ########################################################################
        #add to Library function
        ########################################################################




        def namewindow(*args):
            def initiateexport(*args):

                userinput = str(cmds.textField(textfield, q = True, text = True))


                canprocede = True
                periodwarning = False
                spacewarning = False
                for x in userinput:
                    if x == '.':
                        canprocede = False
                        periodwarning = True
                    if x == ' ':
                        canprocede = False
                        spacewarning = True
                checkfile = userinput + '.ma'
                for fi in filelist:
                    if fi == checkfile:
                        canprocede = False
                        cmds.warning('Item with name \'' + userinput + '\' already exists in the Library.')
                if spacewarning == True:
                    cmds.warning('Do not include any spaces in name.')
                if periodwarning == True:
                    cmds.warning('Do not include \'.\' in file name.')
                if len(userinput) == 0:
                    cmds.warning('Please give item a name.')
                    canprocede = False

                if canprocede == True:
                    if cmds.window('namingwindow', exists = True):
                        cmds.deleteUI('namingwindow', window = True)

                    blastoff(self.newdirectory, userinput)






            cmds.window('namingwindow', title = 'Name Item', w = 350, h = 100, s = False)

            parentlayout = cmds.rowColumnLayout(adjustableColumn = True)
            cmds.text('Enter name of item to add to Library.', h = 30)




            global textfield
            textfield = ''
            textfield = cmds.textField(ec = initiateexport)


            cmds.separator(h = 20)
            cmds.button(l = 'Add to Library', c = initiateexport)




            cmds.showWindow()








        def addtoLibrary(*args):
            selectionlist = cmds.ls(sl = True)
            if len(selectionlist) > 0:
                namewindow()

            else:
                cmds.warning('There are no objects selected in scene.')





        objbuttons = []
        def createbuttons(filedirectory, listall, *args):
            if filedirectory == 0 or filedirectory == 'Set Directory' or filedirectory == '0':
                return
            for buttons in objbuttons:

                cmds.deleteUI(buttons, control = True)



            del objbuttons[:]

            global filelist

            filelist = cmds.getFileList(fld = filedirectory)
            if listall == True:
                filedisplaylist = filelist
            if listall == False:
                filedisplaylist = []
                search = cmds.textField(searchbar, q = True, text = True)
                for f in filelist:
                    fstring = str(f)
                    lowerstring = fstring.lower()
                    lowersearch = search.lower()
                    if f.endswith('.ma'):

                        if lowersearch in lowerstring[:-3]:

                            filedisplaylist.append(f)

                    if f.endswith('.png'):
                        if lowersearch in lowerstring[:-4]:

                            filedisplaylist.append(f)







            objects = []
            images = []

            for eachfile in filedisplaylist:
                if eachfile.endswith('.ma'):

                    objects.append(eachfile)


                if eachfile.endswith('.png'):


                    images.append(eachfile)




            global threecolumn
            #threecolumn = cmds.rowColumnLayout(p = scrollLayoutparent, numberOfColumns = 3, w = 600)





            for element in objects:

                for imagename in images:

                    if imagename[:-4] == element[:-3]:



                        buttonimage = filedirectory + '\\' + str(imagename)
                        importobject = filedirectory + '\\' + str(element)
                        label = str(element[:-3])





                        objectbutton = cmds.iconTextButton(label, p = triLayout, bgc = [0.25, 0.3, 0.3], st = 'iconAndTextCentered', i = buttonimage, l = label, c = partial(addtoscene, importobject, label))

                        objbuttons.append(objectbutton)



            cmds.button(addtokitbashbutton, edit = True, c = addtoLibrary)
            cmds.button(directorybutton, edit = True, l = filedirectory)

        def sendtosearch(*args):
            createbuttons(cmds.button(directorybutton, q = True, l = True), False)


        searchbar = cmds.textField(tcc = sendtosearch)
        addtokitbashbutton = cmds.button(l = 'Add to Library.', aop = True, c = setdirwarning)
        if self.directq != 0 and self.directq != 'Set Directory' and self.directq != '0':



            createbuttons(self.directq, True)



        def saveandclose(*args):




            option = cmds.optionVar(sv = ('saveddirect', cmds.button(directorybutton, q = True, l = True)))

            cmds.deleteUI(self.window, window = True)
            if cmds.window('namingwindow', exists = True):
                cmds.deleteUI('namingwindow', window = True)
            if cmds.modelEditor('temppanel1', exists = True):
                cmds.deleteUI('temppanel1', pnl = True)
            if cmds.window('cameraangle', exists = True):
                cmds.delete('test_grp')
                cmds.delete('CameraGroup')
                cmds.deleteUI('cameraangle', window = True)
            if cmds.window('waitwindow', exists = True):
                cmds.deleteUI('waitwindow', window = True)

        cmds.rowColumnLayout(adjustableColumn = True, parent = parentlayout)
        cmds.button(l = 'Close', aop = True, c = saveandclose)
        cmds.separator(h = 5)
        def reset(*args):
            cmds.optionVar(sv = ('saveddirect', 0))
            cmds.deleteUI(self.window)

            KitbashUI()

        cmds.button(l = 'Reset UI', aop = True, c = reset)

        cmds.showWindow()


