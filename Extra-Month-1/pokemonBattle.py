import random
import time

print('******* ROBO-BATTLE! ******')

print('Spelare 1, skriv in namnet på din robot: ')
robot1 = input('> ')

print('Spelare 2, skriv in namnet på din robot: ')
robot2 = input('> ')

liv1 = 10
liv2 = 10

fight = True

while fight:
    print()
    print(robot1, 'har', liv1, 'liv kvar')
    print(robot2, 'har', liv2, 'liv kvar')

    attack1 = random.randint(1,4)
    attack2 = random.randint(1,4)
    attack3 = random.randint(1,4)

    print('Vilken attack ska ' + str(robot1) + ' göra? (1,2,3)')
    robot1attack = int(input('> '))

    print('Vilken attack ska ' + str(robot2) + ' göra? (1,2,3)')
    robot2attack = int(input('> '))

    print(str(robot1) + ' attackerar och...')
    time.sleep(1)
    if robot1attack == 1:
        print(str(robot2) + ' tog ' + str(attack1) + ' skada!')
        liv2 -= attack1
    if robot1attack == 2:
        print(str(robot2) + ' tog ' + str(attack2) + ' skada!')
        liv2 -= attack2
    if robot1attack == 3:
        print(str(robot2) + ' tog ' + str(attack3) + ' skada!')
        liv2 -= attack3

    time.sleep(1)
    print()
    print(str(robot2) + ' attackerar och...')
    time.sleep(1)
    if robot2attack == 1:
        print(str(robot1) + ' tog ' + str(attack1) + ' skada!')
        liv1 -= attack1
    if robot2attack == 2:
        print(str(robot1) + ' tog ' + str(attack2) + ' skada!')
        liv1 -= attack2
    if robot2attack == 3:
        print(str(robot1) + ' tog ' + str(attack3) + ' skada!')
        liv1 -= attack3

    if liv1 < 1:
        print()
        print(robot2, 'vann!')
        fight = False

    if liv2 < 1:
        print()
        print(robot1, 'vann!')
        fight = False

    time.sleep(1)

