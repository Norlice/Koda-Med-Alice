print('Välkommen till vän-kalkylatorn!')

print('Skriv in namn 1: ')
namn1 = input('> ')

print('Skriv in namn 2: ')
namn2 = input('> ')

score = 50

for bokstav in namn1:
    if bokstav in 'ultimat' and bokstav in 'supercool':
        score += 20
    if bokstav in 'vänskap':
        score += 5
    if bokstav in 'kul':
        score += 1
    if bokstav in 'drakar':
        score += 1
    if bokstav in namn2:
        score += 5
    if bokstav in 'osams':
        score -= 1

for bokstav in namn2:
    if bokstav in 'vänskap':
        score += 5
    if bokstav in 'kul':
        score += 1
    if bokstav in 'drakar':
        score += 1
    if bokstav in namn1:
        score += 5

print('Vänpoäng: %s' % (score))