__Program__     = "Gradebook.PrintDefs"    
__Programer__   = "Themadhood Pequot"
__Date__        = "11/20/2023"
__Version__     = "0.0.1"
__Time__        = "0000:00:01: 12:00:00"
__Update__      = ""
__Info__        = ""
TestModual      = [] 

VersionLst = [f"{__Program__}: {__Version__}: {__Time__}"]

def PrintGrade(self):
    #print current grade
    print(F"Current grade: {self._GetPrintPercent(self._CurrentGrade,\
self._CurentMaxGrade)}")
    print()
    #print posible grades
    if self._AssinmentsLeft > 0:
        self._PrintPosibleGrades()

def GetCurrentPercent_(self,grade,Max):
    if Max == 0:
        Max = 1
    return (grade/Max)*100


def GetPrintPercent_(self,grade,Max):
    currentPercent = self._GetCurrentPercent(grade,Max)
    
    gradeFraction = f"{grade}/{Max}"
    
    return f"{gradeFraction} {currentPercent}%"


def CalculatePointsNeeded_(self):
    need = (self._MaxGrade/10)*7
    need -= self._CurrentGrade
    need /= self._AssinmentsLeft
    return need


def PrintPosibleGrade_(self,posibleGrade,persent):
    current = self._CurrentGrade + posibleGrade
    
    print(F"posible grade with {persent}%: {self._GetPrintPercent(current,\
self._MaxGrade)}")


def PrintPosibleGrades_(self):
    need = self._CalculatePointsNeeded()

    persents = list(self._PosibleGrades)
    persents.reverse()
    for p in persents:
        self._PrintPosibleGrade(self._PosibleGrades[p],p)

    print(F"Need minimum of: {need}/{self._PosibleGrades[100]} on rest for 70%")   
















