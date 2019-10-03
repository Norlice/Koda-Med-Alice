print('Välkommen till vän-kalkylatorn!')

print('Skriv in namn 1: ')
namn1 = input('> ')

print('Skriv in namn 2: ')
namn2 = input('> ')

score = 0

for character in namn1:
    if character in 'friendship':
        score += 1
    if character in namn2:
        score += 5

print('Vänpoäng: %s' % (score))