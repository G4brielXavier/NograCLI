from Inputron.principal import (
    msg,
    inputronload,
    inp,
)

from Nogra.commands import (
    interpreter,
    system,
    sleep
)

import shutil

columns = shutil.get_terminal_size().columns

system('cls')
print("Nogra vI".center(columns))
print("By dotxavierket 2024, All Rights Reserved".center(columns))

msg(f'To Start, use the command "new sub" to add a new Matter', 'Initial')

while True:
    iptHere = inp()
    
    if iptHere == "close":
        system('cls')
        inputronload("Leaving the Nogra", "BYE!", 0.1, 2)
        sleep(1)
        break
    
    interpreter(iptHere)