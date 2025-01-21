__Program__     = "Gradebook.__init__"    
__Programer__   = "Themadhood Pequot"
__Date__        = "11/20/2023"
__Version__     = "0.0.1"
__Time__        = "0000:00:00: 00:05:00"
__Update__      = ""
__Info__        = ""
TestModual      = [] 

try:
    from .PrintGrades import *
except:
    from PrintGrades import *



VersionLst += [f"{__Program__}: {__Version__}: {__Time__}"]
