__Program__     = "Gradebook.PrintGrades"    
__Programer__   = "Themadhood Pequot"
__Date__        = "11/20/2023"
__Version__     = "0.0.1"
__Time__        = "0000:00:00: 12:00:00"
__Update__      = ""
__Info__        = ""
TestModual      = []

try:
    from . import PrintDefs as _PD
except:
    import PrintDefs as _PD
    
#compile PYsInfo
VersionLst = [f"{__Program__}: {__Version__}: {__Time__}"]
VersionLst += _PD.VersionLst

class PrintPerdictedGrade:
    PrintGrade = _PD.PrintGrade
    _GetPrintPercent = _PD.GetPrintPercent_
    _PrintPosibleGrade = _PD.PrintPosibleGrade_
    _GetCurrentPercent = _PD.GetCurrentPercent_
    _PrintPosibleGrades = _PD.PrintPosibleGrades_
    _CalculatePointsNeeded = _PD.CalculatePointsNeeded_

    
    def __init__(self,Grades):
        self._Grades = Grades
        self._PosibleGrades = self._BlankPosible()
        self.lstOfAssinments = list(self._Grades)

        self._UpdatePosibleGrades()
        self.PrintGrade()


    def _BlankPosible(self):
        return {0:0,    50:0,   70:0,   75:0,   80:0,   90:0,   100:0}

    
    def _ResetCalculaterHolders(self):
        self._AssinmentsLeft = 0
        self._CurrentGrade = 0
        self._CurentMaxGrade = 0
        self._MaxGrade = 0


    def AddAssinment(self,name,grade=None,PosibleGrade=100):
        self._Grades.update({name:[grade,PosibleGrade]})
        self.lstOfAssinments = list(self._Grades)
        self._UpdatePosibleGrades()


    def _UpdatePosibleGrades(self):
        self._ResetCalculaterHolders()
        for asinment in self.lstOfAssinments:
            asinmentCurrentGrade = self._Grades[asinment][0]
            asinmentMaxGrade = self._Grades[asinment][1]
            self._MaxGrade += asinmentMaxGrade

            if asinmentCurrentGrade != None:
                self._CurrentGrade += asinmentCurrentGrade
                self._CurentMaxGrade += asinmentMaxGrade

            else:
                self._AssinmentsLeft += 1
                self._UpdatePosible(asinmentMaxGrade)


    def _UpdatePosible(self,grade):
        X = grade/10
        self._PosibleGrades[50] += (grade/2)
        self._PosibleGrades[70] += X*7
        self._PosibleGrades[75] += ((grade/4)*3)
        self._PosibleGrades[80] += (X*8)
        self._PosibleGrades[90] += (X*9)
        self._PosibleGrades[100] += grade


    

if __name__ == "__main__":
    #name: [grade,max]
    Grades = {"Quiz 1":[1,1],
              "Quiz 2":[1,1],
              "":[None,1]}

    g = PrintPerdictedGrade(Grades)















