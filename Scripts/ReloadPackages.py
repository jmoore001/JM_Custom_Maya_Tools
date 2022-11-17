import sys
import os


# this class is used to reload all the packages in maya because once maya imports it, it doesn't respond to changes made
# to the files. Use this while editing any scripts by making a reference to this class in the script you're editing and 
# call unload packages function before the import statement. If you need to, you can use self.DEFAULT_RELOAD_PACKAGES to
#unload all the packages in this toolkit
class ReloadPackages(object):
    def __init__(self):
        
        self.DEFAULT_RELOAD_PACKAGES = [] 
        script = os.path.realpath(__file__)
        fileName = os.path.basename(__file__)

        direct = script.replace(fileName, "")
        files = os.listdir(direct)
        for f in files:
            if f.endswith('.py'):
                
                self.DEFAULT_RELOAD_PACKAGES.append(f)

        
    def unload_packages(self, silent=True, packages=None):
        if packages is None:
            packages = self.DEFAULT_RELOAD_PACKAGES
            deletePy = True
            print("there are no specified packages")
        else:
            packages = [packages]
            deletePy = False
            print("there are specified packages")
            
        # unload packages
        for p in packages:
            try:
            
                
                for i in sys.modules.keys():
                    if deletePy:
                        compareString  = p[:-3]
                    if not deletePy:
                        compareString  = p
                    if i.startswith(compareString):
                        
                        del(sys.modules[i])
                        if not silent:
                            print("Unloaded: %s" % i)
            except:
                print("Failed to unload: %s" % i)
    