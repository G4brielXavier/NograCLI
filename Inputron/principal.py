from time import sleep
from os import system
from rich import print

# INPUTRON I

# main input to Inputron
def inp():
    ipt = input('<@nogra> ')
    return ipt.lower()

# function that manage message in terminal
def msg(msg:str, about:str = "", space:bool = False, iserror:bool = False):
    print("") if space is True else print()

    if not about == "":
        print(f'{about} Warn - {msg}') if iserror is False else print(f'{about} Error - {msg}')
    else:
        print(f'Warn - {msg}') if iserror is False else print(f'Error - {msg}')

    print("") if space is True else print()

# function that show visual loading
def inputronload(msg, msgComplete, speed: float = 0.1, repeatTimes: int = 10):
    bars = ["|", "/", "-", "\\"]
    
    for _ in range(repeatTimes):
        for i in range(len(bars)): 
            sleep(speed)   
            system('cls')    
            print(f'{bars[i]} > {msg}')
    
    sleep(speed)
    system('cls')
    print(msgComplete)
            
# function that control asks in terminal
def askCustommer(ask:str, space:bool = True, isInt:bool = False, isFloat:bool = False):
    if space is True:
        print('')
     
    try:
        askInp = input(f'    > {ask}: ')
        
        if isInt is True:
            return int(askInp)
        
        if isFloat is True:
            return float(askInp)
        
        return askInp
    
    except Exception as err:
        msg(err, 'Nogra', True, True)
