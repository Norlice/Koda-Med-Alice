import random

hemligt = random.randint(1,25)

print('Gissa ett tal mellan 1 & 25')

gissning = int(input('> '))

while gissning != hemligt:
    if gissning < hemligt:
        print('Gissa högre.')
    else:
        print('Gissa lägre.')

    gissning = int(input('> '))

print('Du gissade rätt! Talet var %s' % (hemligt))
