# Monty Hall Problem Solver

import random

player_won = 0
player_lose = 0

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

print(f'''{bcolors.BOLD}{bcolors.OKBLUE}
<{'-' * 120}>\n\n{' ' * 45}✨ Monty Hall Problem Solver ✨\n\n<{'-' * 120}>{bcolors.ENDC}''')



while True:
    try:
        match = int(input('\n몇판을 돌리실껀가요? (숫자로 입력해주세요) : '))      
    except ValueError:
        print("\n! 숫자가 아닙니다 !")
        continue
    else:
        break 


while True:
    change = str(input('\n바꿀꺼신가요? ("O", "X"로 입력해주세요) : '))

    if change == 'O':
        break
    if change == 'X':
        break
    if change== 'o':
        change = 'O'
        break
    if change== 'x':
        change = 'X'
        break
    else:
        print('\n"O" 또는 "X"로 입력해주세요')
        continue



for x in range(match):
    car_is = opened_door = random.randint(1, 3)
    user = random.randint(1, 3)
    
    while opened_door in (car_is, user):
        opened_door = random.randint(1, 3)

    if change == 'O':
        if (user == 2 and opened_door == 3) or (user == 3 and opened_door == 2):
            user = 1  
        elif (user == 1 and opened_door == 3) or (user == 3 and opened_door == 1):           
            user = 2
        elif (user == 1 and opened_door == 2) or (user == 2 and opened_door == 1):
            user = 3

        if user == car_is:
            player_won += 1

        if not user == car_is:
            player_lose += 1

        

    if change == 'X':

        if (user == 2 and opened_door == 3) or (user == 3 and opened_door == 2):
            pass
        elif (user == 1 and opened_door == 3) or (user == 3 and opened_door == 1):
            pass
        elif (user == 1 and opened_door == 2) or (user == 2 and opened_door == 1):
            pass



        if user == car_is:
            player_won += 1

        if not user == car_is:
            player_lose += 1

if change == 'O':
    print(f'''\n\n\n{bcolors.BOLD}{bcolors.OKGREEN}<{'-' * 120}>\n''')  
    print(f'           {match}번 실행됨, 문을 바꿨을떄 {player_won}번 만큼 차를 고르고 {player_lose}번 만큼 염소를 골랐습니다, 확률 : ({(player_won/match*100)}%)')
    print(f'''\n<{'-' * 120}>{bcolors.ENDC}\n''') 

if change == 'X':
    print(f'''\n\n\n{bcolors.BOLD}{bcolors.OKGREEN}<{'-' * 120}>\n''')    
    print(f'           {match}번 실행됨, 문을 바꾸지 않았을때 {player_won}번 만큼 차를 고르고 {player_lose}번 만큼 염소를 골랐습니다, 확률 : ({(player_won/match*100)}%) ')
    print(f'''\n<{'-' * 120}>{bcolors.ENDC}\n''')