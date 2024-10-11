from Inputron.principal import (
    askCustommer,
    msg,
    inputronload,
)

from rich import print
from rich.console import Console
from rich.table import Table
from rich import box

console = Console()
gradeTable = Table(title="Nogra Table", box=box.ROUNDED)

gradeTable.add_column("Matter")
gradeTable.add_column("Sem1")
gradeTable.add_column("Sem2")
gradeTable.add_column("Sem3")
gradeTable.add_column("Sem4")
gradeTable.add_column("Average (All)")


def getAverageSem(bins:list, returnStr:bool = False, qBins:int = 4, averageTarget:float = 6.0):
    average = sum(bins) / qBins
    
    if average >= averageTarget + 2:
        if returnStr is True:
            return f'{average:.1f}'
    if average >= averageTarget:
        if returnStr is True:
            return f'{average:.1f}'
        return average 
    else:
        if returnStr is True:
            return f'{average:.1f}'
        return average
    

class Grades:
    def __init__(self):
        self.grades = {}
        self.bins = 4
        self.updated = True
        self.matters = 0
        
    def __size__(self):
        count = 0
        
        for _, _ in self.grades.items():
            count += 1
            
        return count
    
    def addMatter(self):
        matterName = askCustommer("Matter Name")
        
        try:
            self.grades[matterName] = [0.0, 0.0, 0.0, 0.0]
            
            msg(f'"{matterName}" is created', "Nogra", True)
            matterName = ''
        except Exception as err:
            msg(err, 'Nogra', True, True)
                   
    def removeMatter(self):
        matterName = askCustommer("Matter Name")
        
        try:
            del self.grades[matterName]
            
            msg(f'"{matterName}" is removed', 'Nogra', True)
        except Exception as err:
            msg(err, 'Nogra', True, True)
            
    def showTable(self):
        print()
        print(f'Tip: If the NograTable is not updated, use the command "upd tab"')
        print()
        print('STATUS: NOT UPDATED') if self.updated is False else print('STATUS: UPDATED')
        print(f'QTY: {self.__size__()}')
        print()
        console.print(gradeTable)
        print()
        
    def setGrade(self):
        try:
            matterName = askCustommer("Matter Name")
            semIndex = askCustommer("Column Semestral", True, isInt=True)
            
            self.grades[matterName][semIndex-1] = askCustommer(f'Set Grade > {matterName}[Sem{semIndex}]', isFloat=True)
            msg(f'{matterName} was updated', 'Nogra', True)
            
        except Exception as err:
            msg(err, 'Nogra', True, True)
            
    def resetTable(self):
        global gradeTable
        
        newGradeTable = Table(title="Nogra Table")
        newGradeTable.add_column("Matter")
        newGradeTable.add_column("Sem1")
        newGradeTable.add_column("Sem2")
        newGradeTable.add_column("Sem3")
        newGradeTable.add_column("Sem4")
        newGradeTable.add_column("Average (All)", width=13, justify='center')
                
        try:
            
            for i, v in self.grades.items():
                newGradeTable.add_row(i, str(v[0]), str(v[1]), str(v[2]), str(v[3]), getAverageSem(v, True, self.bins))
            
            inputronload("Updating NograTable", "COMPLETE ✓", repeatTimes=3)
            msg(f'NograTable Updated', 'Nogra', True)
            
            gradeTable = newGradeTable
            
            
        except Exception as err:
            msg(err, 'Nogra', True, True)
            
    