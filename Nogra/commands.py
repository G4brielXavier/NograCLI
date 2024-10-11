from Inputron.principal import msg

from os import system
from time import sleep

from Nogra.nograClass import Grades

sourceGrade = Grades()

def interpreter(code):
    statusGrade = None

    match(code):
        case 'new sub':
            sourceGrade.updated = False
            sourceGrade.addMatter()
            
        case 'del sub':
            sourceGrade.updated = False
            sourceGrade.removeMatter()
            
        case 'tab':
            sourceGrade.showTable()

        case 'upd tab':
            sourceGrade.updated = True
            sourceGrade.resetTable()
            
        case 'set grade':
            sourceGrade.updated = False
            sourceGrade.setGrade()
    
        case 'cls' | 'clear':
            system('cls')
    
        case _:
            msg(f'This "{code}" is not exist', 'Nogra', True, True)